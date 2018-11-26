# When undergoing shear, lammps wraps the periodic boundaires if the strain becomes greater
# than 0.5 or less than -0.5. The problem with this is that this makes it hard to plot the
# strain. This sscript reads in a LAMMPS thermodynamic output file and unwraps the strain to
# give the true strain value.

import numpy as np
from sys import argv, exit

if len(argv) != 2:
    print("Missing argument, use: ./strain_wrapping.py filename_to_convert.thermo")
    exit(1)

filename = argv[1]
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
    np.savetxt(filename.rstrip("thermo") + "wrapped.thermo", data, header=inputfile.readline().rstrip())
