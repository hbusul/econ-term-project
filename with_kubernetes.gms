$offdollar
$title With Kubernetes Maximize Profit
options
limrow = 0
limcol = 0
solprint = off;

sets
d 'days'  /1*30/
h 'hours' /0*23/
;

scalar hourly_cost_per_unit /0.768/;
scalar customer_per_computer /8/;
scalar revenue_per_customer /0.2/;


table demand 'hourly demand for each day'
$include data.inc 
;

variables
x(d, h)     'number of computers to buy at day d hour h'
serve(d, h) 'number of customers served at day d hour h'
z           'profit'
;

integer variables x;
integer variables serve;

serve.up(d, h) = 800;
x.up(d, h) = 800 / customer_per_computer;

equations
max_serve_demand(d, h)    'we cannot serve more than demand'
max_serve_capacity(d, h)  'each computer can serve up to some people'
objective                 'who does not want to maximize the profit?'
;

max_serve_demand(d, h)   .. serve(d, h) =l= demand(d, h);
max_serve_capacity(d, h) .. serve(d, h) =l= customer_per_computer * x(d, h);
objective                .. z           =e= (sum((d,h), serve(d,h)) * revenue_per_customer) - (sum((d,h), x(d,h)) * hourly_cost_per_unit);

model wok /all/;
solve wok using MIP maximizing z;

parameter unserved;
unserved = sum((d,h), demand(d,h) - serve.l(d,h));

display x.l;
display unserved;