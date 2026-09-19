def load_sparc(path="data/raw/SPARC_Lelli2016.csv"):
    import pandas as pd
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print("Baixe SPARC em https://... - instrucoes em docs/data.md")
        return None
