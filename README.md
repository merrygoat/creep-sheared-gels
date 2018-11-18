Implementing bulk creep dynamics requires application of a constant shear stress.

Shear can be done using the SLLOD equations of motion, however these impose a homogeneous flow profile to the sample. It would be better to control the shear by modifying the shear rate based on a feedback loop which measures the stress at each timestep. We then need to add DPD dynamics to adsorb some of the energy created by the shear and prevent velocity drift.

* gel_setup.py provides a way to create starting configurations of a polydisperse gel described by a Morse potential. It is easier to create a LAMMPS dump file and read this in than define this potential entirely using a LAMMPS script. This is the same mixture used in https://aip.scitation.org/doi/10.1063/1.4973351
* sllod_shear.lmp.in provides a sample LAMMPS script to create a sheared simulation with the shear controlled by the SSLOD thermostat.
* shear_restart.in is a LAMMPS input file to read in an aged gel configuration and apply a shear. LAMMPS restart files do not save the pair coefficients for the hybrid/overlay fix so these are re-specified in the script.
* shear.in is a script to implement a constant stress shear by measuring the stress at each timestep and modifying the shear rate to match a target stress. This is the method used in https://arxiv.org/pdf/1807.04330.pdf.
* gel.in is a LAMMPS input script to create and age gel configurations from the output of gel_setup.py. The aged samples are then intended to be sheared.
* submission_script.sh is an example of how the LAMMPS script might be executed.
