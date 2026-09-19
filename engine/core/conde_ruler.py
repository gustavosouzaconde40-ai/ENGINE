import numpy as np
from numba import njit

@njit
def conde_ruler(rho, rho0):
    """Conde Ruler: I = log(1 + rho/rho0) - Eq.2 do paper"""
    return np.log(1.0 + rho / rho0)

@njit
def grad_I(rho, grad_rho, rho0):
    return grad_rho / (rho + rho0)
