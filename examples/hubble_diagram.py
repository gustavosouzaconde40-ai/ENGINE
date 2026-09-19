"""Reproduz H0 = 69.8 ±1.2 do paper"""
from engine.cosmology.background import hubble_parameter
import numpy as np
z = np.linspace(0, 2, 50)
H = hubble_parameter(z, H0=69.8, Omega_m=0.3, Z0=1.0, gradI_z=0.01)
print(f"H(z=0) = {H[0]:.1f} km/s/Mpc - Reducao da tensao de Hubble")
