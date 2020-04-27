# Bulk creep Molecular Dynamics simulations

Implementing bulk creep dynamics requires application of a constant shear stress.

Shear can be done using the SLLOD equations of motion, however these impose a homogeneous flow profile to the sample. It would be better to control the shear by modifying the shear rate based on a feedback loop which measures the stress at each timestep. We then need to add DPD dynamics to adsorb some of the energy created by the shear and prevent velocity drift.

### Contents
The *gel_setup* folder contains a Python script to initialise a configuration of a polydisperse gel described by a Morse potential. It is easier to create a LAMMPS dump file and read this in than define this potential entirely using a LAMMPS script.

The *lammps_scripts* folder contains example scripts for equilibrating and shearing a gel configuration at constant stress. This is the method used in  https://doi.org/10.1039/C8SM01432A

The *strain_wrapping* folder contains a script for unwrapping the measured strain from LAMMPS output files for analysis.