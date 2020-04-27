# An example of calling LAMMPS with the variable specifying the starting configuration.
mpiexec -np 4 lmp_mpi -in shear.in -var file_name morse_input_phi0.1586.lmp