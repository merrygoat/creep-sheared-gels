# October 2018
# Writing a LAMMPS input file for a system with Morse interaction and gaussian polydispersity

import numpy as np
from scipy.stats import norm
import sys


def main(epsilon: float = 5, number_density: float = 0.2, rho: float = 33,
         num_particles: int = 1000):
    """Main function
    :param epsilon: Morse potential well depth.
    :param number_density: Density of particles.
    :param rho: Morse interaction distance.
    :param num_particles: Number of particles in simulation box.
    """
    r_cut_coeff = 1.4               # Morse cutoff
    pd = 0.04                       # Polydispersity gaussian sigma
    num_types = 7                   # Number of different particle species in polydisperse mixture
    # If turned on, "dpd_thermostat" will add "Morse" to the interaction potential to allow use
    # of the hybrid/overlay style
    dpd_thermostat = True

    box_volume = num_particles/number_density
    side_len = box_volume ** (1/3)

    # Set up the particle diameters
    half_num_types = np.floor(num_types/2)
    bin_edges = np.arange(1 - (half_num_types * pd), 1 + (half_num_types * pd) + pd, pd) - pd / 2.
    bin_centers = (np.arange(-half_num_types, half_num_types + 1) * pd) + 1

    # Set up the Gaussian from which particle species are drawn
    cumulative = norm.cdf(bin_edges, 1, pd)
    # Set the limits of the Gaussian to be 0 and 1.
    cumulative[0] = 0
    cumulative[-1] = 1

    # Determine the particle species
    random_num = np.random.rand(num_particles)
    # Return the indices of the bins to which each value in random_num belongs
    particle_species = np.digitize(random_num, cumulative)

    # Create random particle coordinates
    x = np.random.uniform(0, side_len, size=num_particles)
    y = np.random.uniform(0, side_len, size=num_particles)
    z = np.random.uniform(0, side_len, size=num_particles)

    packing = 0
    for i in range(num_particles):
        packing += np.pi / 6 * (bin_centers[particle_species[i] - 1] ** 3) / box_volume

    print(f"* The packing fraction is {packing:.4f}")

    filename = "morse_input_phi%.4f.lmp" % packing

    with open(filename, 'w') as ouptut_file:
        # Write the LAMMPS file header
        ouptut_file.write("LAMMPS Description\n\n")
        ouptut_file.write("{} atoms\n\n".format(num_particles))

        # Write the box size
        ouptut_file.write("{} atom types\n".format(num_types))
        ouptut_file.write("0 {:.6f} xlo xhi\n"
                          "0 {:.6f} ylo yhi\n"
                          "0 {:.6f} zlo zhi\n\n".format(side_len, side_len, side_len))

        # Write the particle masses, the particle types all have mass density = 1
        ouptut_file.write("Masses\n\n")
        for i in range(num_types):
            ouptut_file.write("%d %g\n" % (i + 1, np.pi / 6 * bin_centers[i] ** 3))
        ouptut_file.write("\n")

        # If the hybrid/overlay command is used, need to specify the type of the potential
        if dpd_thermostat:
            keyword = " morse "
        else:
            keyword = ""

        # Specify the interaction coefficient for the Morse potential:
        # in LAMMPS's documentation they are: d0 alpha r0 cutoff
        ouptut_file.write("PairIJ Coeffs\n\n")
        for type_1 in range(num_types):
            for type_2 in range(type_1, num_types):
                diam_i = bin_centers[type_1]
                diam_j = bin_centers[type_2]
                mixed_diam = 0.5 * (diam_i + diam_j)
                ouptut_file.write(f"{type_1 + 1:d} {type_2 + 1:d}{keyword:s}{epsilon:g} {rho:g} "
                                  f"{mixed_diam:g} {r_cut_coeff * mixed_diam:g}\n")

        # Write coordinates
        ouptut_file.write("\nAtoms\n\n")
        for i in range(num_particles):
            ouptut_file.write(f"{i + 1:d} {particle_species[i]:d} {x[i]:g} {y[i]:g} {z[i]:g}\n")


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 5:
        raise SyntaxError("Incorrect syntax.\nUse python gel_setup.py epsilon number_density "
                          "rho_0 num_particles")
    epsilon = float(sys.argv[1])
    number_density = float(sys.argv[2])
    rho_0 = float(sys.argv[3])
    num_particles = int(sys.argv[4])
    main(epsilon, number_density, rho_0, num_particles)