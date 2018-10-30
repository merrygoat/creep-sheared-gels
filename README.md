Implementing bulk creep dynamics requires application of a constant shear stress.

Shear can be done using the SLLOD equations of motion, however thse impose a homogeneous flow profile to the sample. It would be better to control the shear by modifyibng the shear rate based on a feedback loop which measures the stress at each timestep. We then need to add DPD dynamics to adsorb some of the energy created by the shear and prevent velocity drift.

* gel_setup.py provides a way to create starting configurations of a polydispers gel described by a Morse potential. It is easier to create a lammps dump file and read this in thean define this potential entirely using a lammps script. This is the same mixture used in https://aip.scitation.org/doi/10.1063/1.4973351
* sllod_shear.lmp.in provides a sample lammps script to create a sheared simulation with the shear controlled buy the SSLOD thermostat.
* shear_lmp.in is a script to implement a constant stress shear by measuring the stress at each timestep and modifying the shear rate to match a target stress. This is the method used in https://arxiv.org/pdf/1807.04330.pdf.
* submission_script.sh is an example of how the lammps script might be executed.
