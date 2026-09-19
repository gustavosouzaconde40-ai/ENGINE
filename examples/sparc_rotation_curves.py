"""Reproduz Fig.1 do seu paper - SPARC"""
from engine.data.sparc_loader import load_sparc
df = load_sparc()
if df is not None:
    print(f"SPARC carregado: {len(df)} entradas")
else:
    print("SPARC nao encontrado - veja docs/data.md")
