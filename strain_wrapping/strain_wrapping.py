import sys

import numpy as np


def main():
    filename = sys.argv[1]
    data = np.loadtxt(filename, skiprows=1)
    num_data_points = data.shape[0]

    num_flips = np.zeros(num_data_points)
    for row_number in range(num_data_points-1):
        num_flips[row_number + 1] = num_flips[row_number]
        if data[row_number, 6] - data[row_number + 1, 6] > 0.5:
            num_flips[row_number + 1] += 1
        elif data[row_number, 6] - data[row_number + 1, 6] < -0.5:
            num_flips[row_number + 1] -= 1

    data[:, 6] += num_flips

    with open(filename, 'r') as inputfile:
        np.savetxt(filename.rstrip("thermo") + "wrapped.thermo", data,
                   header=inputfile.readline().rstrip())


if __name__ == '__main__':
    if sys.argv != 2:
        raise SyntaxError( "Missing argument, use: ./strain_wrapping.py filename_to_convert.thermo")
