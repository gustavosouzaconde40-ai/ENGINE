import numpy as np

def lambda_eff(Z0, grad_I_norm, model="exponential"):
    """Lambda_eff(Z0, ∇I) = Z0 f(|∇I|) - Eq.1"""
    if model == "exponential":
        return Z0 * (1 - np.exp(-grad_I_norm**2))
    return Z0 * np.tanh(grad_I_norm)
