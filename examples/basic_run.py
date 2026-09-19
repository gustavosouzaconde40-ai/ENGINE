"""Quick start para revisor MNRAS - roda sem dados externos"""
from engine import conde_ruler, lambda_eff
import numpy as np
rho = np.logspace(-3, 2, 100)
I = conde_ruler(rho, rho0=0.1)
Lambda = lambda_eff(Z0=1.0, grad_I_norm=0.01)
print(f"ENGINE OK - I mean={I.mean():.3f}")
