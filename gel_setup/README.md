# Creating polydisperse gel configurations

This script provides a way to create starting configurations of a polydisperse gel described by a Morse potential. This seven component gel is the same mixture used in Griifiths et al. 2017 (https://aip.scitation.org/doi/10.1063/1.4973351)

Since we want to use the gel as part of a molecular dynamics simulation in LAMMPS (https://lammps.sandia.gov/), it would be convenient to define the gel in a LAMMPS input script. However, the LAMMPS input language is hard to work with so instead we do the heavy lifting in Python and create a LAMMPS dump file which defines an initial configuration which is then read in at the start of the simulation.

The script produces a configuration with overlapping particles so it is important that at the start of the simulation a short energy minimisation is conducted to remove the overlaps before starting the time stepping.

The script creates a cubic simulation box, the side length set by the specified number density of the particles.

The script takes the parameters:
* Epsilon - the Morse well depth
* Number density - used to set the size of the simulation box relative to the number of particles
* Rho_0 - the Morse interaction distance
* Number of particles - the number of particles to put in the simulation box

By default the script sets the morse interaction cutoff to 1.4