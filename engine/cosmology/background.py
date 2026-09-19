import numpy as np
from..core.conde_triangle import lambda_eff

def hubble_parameter(z, H0, Omega_m, Z0, gradI_z):
    Lambda = lambda_eff(Z0, gradI_z)
    Omega_L = Lambda / (3*H0**2)
    Ez2 = Omega_m * (1+z)**3 + Omega_L
    return H0 * np.sqrt(Ez2)
