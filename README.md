[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22849189.svg)](https://doi.org/10.5281/zenodo.22849189)
# ENGINE – Emulator of New Generation for Expansion

Phenomenological computational framework for active vacuum contributions (Aeternvm Vacvvm).

**Paper:** MNRAS Submission - Manuscript ID Draft
**Author:** Gustavo Alves Conde, ENGINE Labs (PIC 861720453)
**TRL:** 3-4 (target TRL 6)
**License:** MIT

### Model
Lambda_eff(Z0, ∇I) = Z0 f(|∇I|)
I = log(1 + rho/rho0) [Conde Ruler]
Conde Triangle mapping for vacuum contribution.

### Quick start for MNRAS reviewers (60s)
pip install -e.
python examples/basic_run.py

### Data
Public catalogs only - user must download:
- SPARC (Lelli et al 2016)
- JWST CEERS public
- Pantheon+ + BAO
See docs/data.md

### Structure
engine/core/ -> Conde Ruler & Triangle
engine/cosmology/ -> background.py
engine/data/ -> loaders
examples/ -> reproducible figures
tests/ -> pytest

Code, notebooks and Zenodo records: https://github.com/gustavosouzaconde40-ai/ENGINE
