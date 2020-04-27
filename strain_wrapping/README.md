# Strain wrapping for analysis
 
When outputting data from a simulation undergoing shear, LAMMPS wraps the periodic boundaries if the strain becomes greater than 0.5 or less than -0.5. The problem with this is that this makes it hard to plot the strain. This script reads in a LAMMPS thermodynamic output file and unwraps the strain to give the true strain value.

This will only work usefully if the strain is changing by less than 1, each output time step since numbers greater than 1 would be interpreted as X modulo 1.