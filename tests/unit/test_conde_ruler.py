def test_ruler_zero():
    from engine.core.conde_ruler import conde_ruler
    assert conde_ruler(0.0, 1.0) == 0.0

def test_lambda_recovers_lcdm():
    from engine.core.conde_triangle import lambda_eff
    # Quando grad_I -> 0, Lambda_eff -> 0, recupera LCDM
    assert lambda_eff(Z0=1.0, grad_I_norm=0.0) < 1e-9
