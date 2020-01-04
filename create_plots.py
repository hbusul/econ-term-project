# This file will create plots for daily demands

from os import mkdir
from functools import reduce
import matplotlib.pyplot as plt

filename = "data.inc"

if __name__ == "__main__":
    try:
        mkdir("plots")
    except FileExistsError:
        pass
    except:
        print("Unexpected error")
        exit(1)

    with open(filename, "rt") as f:
        daily_averages = []
        f.readline()  # first line is header
        for line in f:
            data = [int(i) for i in line.split()]
            day = data[0]
            data = data[1:]
            daily_averages.append(reduce((lambda x, y: x + y), data) / 24)
            fig, ax = plt.subplots()
            plt.bar(range(24), data)
            plt.xticks(range(24), [str(i) for i in range(24)])
            fig.savefig(f'plots/day_{day}.png')
            plt.close()
        print(daily_averages)
