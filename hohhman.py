# Hohmann Transfer Calculations in Python

# Define the gravitational parameter (mu) of the central body, e.g., Earth
import math
mu = 3.986e14  # gravitational parameter of Earth in m^3/s^2


def hohhman_transfer(a1, a2):
    # Calculate the semi-major axis of the transfer orbit
    a_t = (a1 + a2) / 2

# Calculate the eccentricity of the transfer orbit
    e_t = (a2 - a1) / (a2 + a1)

# Calculate the delta-V required at perigee and apogee

    delta_v1 = math.sqrt(mu / a1) * (math.sqrt(2 * a2 / (a1 + a2)) - 1)
    delta_v2 = math.sqrt(mu / a2) * (1 - math.sqrt(2 * a1 / (a1 + a2)))

# Total delta-V required for the Hohmann transfer
    delta_v_total = delta_v1 + delta_v2

# If we know the mass of the spacecraft (optional, in kg), we can calculate energy
    mass = 1000  # example mass of 1000 kg
    transfer_energy = 0.5 * mass * delta_v_total**2

    return transfer_energy
