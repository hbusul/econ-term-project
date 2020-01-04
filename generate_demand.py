# This a code for our Economics for Engineer Term Project
# creating consumer demand for an imaginary enterprise
# This python file will create hourly consumer data for a month
# 24 hour system used instead of am/pm
# To keep things simple it is assumed consumers arrive with poisson
# distribution. And also it is assumed between
# 00:00 - 06:00 100 consumers will arrive on average hourly
# 06:00 - 12:00 500 consumers will arrive on average hourly
# 12:00 - 18:00 700 consumers will arrive on average hourly
# 18:00 - 24:00 800 consumers will arrive on average hourly
# The file generated will be called data.inc
# each line will start with the number of the day
# and will be follewed by 24 numbers represent hourly demands

from numpy.random import poisson
from numpy.random import seed
from numpy import concatenate as concat
from functools import reduce

d_0_6 = 100
d_6_12 = 500
d_12_18 = 700
d_18_24 = 300

num_of_days_to_simulate = 30

filename = "data.inc"

seed(seed=1234)


def write_hours(file_handle):
    file_handle.write("   ")
    file_handle.write(
        reduce(lambda x, y: "{:<3} {:<3}".format(x, y), range(24)))
    file_handle.write("\n")


if __name__ == '__main__':
    with open(filename, "wt") as f:
        write_hours(f)
        for day in range(num_of_days_to_simulate):
            demand = reduce((lambda x, y: concat((x, y), 0)), [poisson(demand, 6)
                                                               for demand in [d_0_6, d_6_12, d_12_18, d_18_24]]).tolist()
            f.write("{:<2} ".format(day + 1))
            f.write(
                reduce(lambda x, y: "{:<3} {:<3}".format(x, y), demand) + "\n")
