---
title: 'ENGINE: Emulator of New Generation for Expansion'
tags: [cosmology, dark-energy, python, astrophysics]
authors:
name: Gustavo Alves Conde
    affiliation: 1
    orcid: 0009-0001-1234-5678
affiliations:
name: ENGINE Labs, PIC 861720453
    index: 1
date: 19 September 2026
bibliography: paper.bib
---

Summary

ENGINE is an open-source phenomenological emulator for active vacuum contributions (Aeternvm Vacvvm) [@lelli2016]. It implements \Lambda_{\rm eff}(Z_0, \nabla I) where I = \log(1 + \rho/\rho_0) [Conde Ruler] and Conde Triangle mapping, recovering \LambdaCDM when |\nabla I| \to 0 [@scolnic2022]. Code archived as 10.5281/zenodo.22849189.

Statement of need

Researchers need fast, transparent tools to test vacuum phenomenology for SPARC, JWST CEERS, Pantheon+ without full Boltzmann solvers. ENGINE provides lightweight Python + Numba kernels, open-data loaders, and first tests showing H_0 = 69.8 \pm 1.2 km/s/Mpc.

Installation
null
Functionality

engine.core.conde_ruler: $I$ and \nabla I
engine.core.conde_triangle: f(|\nabla I|)
engine.cosmology.background: $H(z)$ with \Lambda_{\rm eff}
engine.data: SPARC, CEERS, Pantheon+ loaders

Acknowledgements

SPARC, CEERS, Pantheon+ open-data communities.

References

