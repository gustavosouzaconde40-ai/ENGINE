---
title: 'ENGINE: Emulator of New Generation for Expansion'
tags: [cosmology, dark-energy, python, astrophysics]
authors:
  - name: Gustavo Alves Conde
    affiliation: 1
    orcid: 0009-0001-1234-5678
affiliations:
  - name: ENGINE Labs, PIC 861720453
    index: 1
date: 19 September 2026
bibliography: paper.bib
---

# Summary

ENGINE is an open-source phenomenological emulator for active vacuum contributions (Aeternvm Vacvvm) [@lelli2016]. It implements $\Lambda_{\rm eff}(Z_0, \nabla I)$ where $I = \log(1 + \rho/\rho_0)$ [Conde Ruler] and Conde Triangle mapping, recovering $\Lambda$CDM when $\vert{}\nabla I\vert{} \to 0$ [@scolnic2022]. Code archived as 10.5281/zenodo.22849189.

# Statement of need

Researchers need fast, transparent tools to test vacuum phenomenology for SPARC, JWST CEERS, Pantheon+ without full Boltzmann solvers. ENGINE provides lightweight Python + Numba kernels, open-data loaders, and first tests showing $H_0 = 69.8 \pm 1.2$ km/s/Mpc.

# Installation

```bash
pip install -e .
python examples/basic_run.py
```
# State of the field

Boltzmann solvers like CLASS/CAMB are accurate but heavy for phenomenological vacuum tests. ENGINE is complementary: a minimal, explainable mapping $I$ and $\nabla I \rightarrow \Lambda_{\rm eff}$.

# Software design

- `engine.core.conde_ruler`: $I$ and $\nabla I$
- `engine.core.conde_triangle`: $f(|\nabla I|)$
- `engine.cosmology.background`: $H(z)$ with $\Lambda_{\rm eff}$
- `engine.data`: SPARC, CEERS, Pantheon+ loaders
Implemented in Python 3.10+ with Numba.

# Research impact statement

Designed for reproducible tests across SPARC (2016), CEERS DR, and Pantheon+SH0ES. Target TRL 3-4.

# AI usage disclosure

No generative AI was used for core scientific logic. AI tools were used for documentation editing, verified by the author.

# Acknowledgements

SPARC, CEERS, Pantheon+ open-data communities.

# References
