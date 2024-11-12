import tle
import equation
import alternate
import hohhman
import tensorflow as tf
import numpy as np
from astropy import units as u

satellite_id = 43039
api_key = 'AVZC8R-BJMGXU-RVBHGP-5C1S'
risk_factor_model = tf.keras.models.load_model('risk_factor.keras')
risk_vs_hohhman = tf.keras.models.load_model('risk_vs_hohhman.keras')


def get_equation(satellite_id, api_key):
    l1, l2 = tle.fetch_tle_data(satellite_id, api_key)

    l2[4] = float(l2[4]) * (10**(-len(l2[4])))
    l2 = [float(x) for x in l2]

    mean_motion = l2[7] * np.pi * 2 * u.rad / u.day
    eccentricity = l2[4] * u.one
    raan = l2[3] * u.deg
    inclination = l2[2] * u.deg
    arg_perigee = l2[5] * u.deg
    mean_anomaly = l2[6] * u.deg

    positions, semi_major_axis, semi_minor_axis = equation.get_orbit(mean_motion, eccentricity, raan, inclination, arg_perigee, mean_anomaly)
    print(f"Ellipse equation in orbital plane: (x / {semi_major_axis.value:.6f})^2 + (y / {semi_minor_axis:.6f})^2 = 1")
    return positions, semi_major_axis.value, semi_minor_axis, eccentricity.value


def just_one_call(satellite_id, api_key):
    positions, semi_major_axis, semi_minor_axis, eccentricity = get_equation(satellite_id, api_key)
    variations = alternate.generate_orbital_variations(semi_major_axis, eccentricity)
    orbit_params = [np.array([x['parameters']['semi_major_axis'], x['parameters']['eccentricity'], x['periapsis'], x['apoapsis'], 0, 0, 0, 0, 0, 0]).reshape(1, 10, 1) for x in variations]
    risk_factors = [float(risk_factor_model.predict(x)[0][0]) for x in orbit_params]
    hohhman_transfers = [hohhman.hohhman_transfer(semi_major_axis, orbit['parameters']['semi_major_axis']) for orbit in variations]

    regressed = []
    ret_index = 0

    for i in zip(risk_factors, hohhman_transfers):
        regressed.append(float(risk_vs_hohhman.predict(np.array(i).reshape(1, 2))[0][0]))
    for i in range(len(regressed)):
        if regressed[i] < regressed[ret_index]:
            ret_index = i

    print(regressed, ret_index)

    return {
        'Equation': f'(x / {semi_major_axis:.6f})^2 + (y / {semi_minor_axis:.6f})^2 = 1',
        'Alternate Equations': [[risk_factors[i], hohhman_transfers[i], variations[i]['equation']] for i in range(len(variations))],
        'Chosen Index': ret_index,
        'Optimal Transfer Energy': hohhman_transfers[ret_index]
    }


print(just_one_call(satellite_id, api_key))
