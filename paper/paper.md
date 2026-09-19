---
title: 'ENGINE: Emulator of New Generation for Expansion'
tags:
    - cosmology
    - dark energy
    - python
    - astrophysics
authors:
    - name: Gustavo Alves Conde
    affiliation: 1
    orcid: 0009-0000-0000-0000
affiliations:
    - name: ENGINE Labs, PIC 861720453, Brazil / EU
    index: 1
date: 19 September 2026
bibliography: paper.bib
---

# Summary

ENGINE is an open-source phenomenological emulator for active vacuum contributions (Aeternvm Vacvvm). It implements Lambda_eff(Z0, ∇I) = Z0 f(|∇I|) with I = log(1 + rho/rho0) [Conde Ruler] and Conde Triangle mapping. Recovers ΛCDM when |∇I|→0. Code: https://github.com/gustavosouzaconde40-ai/ENGINE, archived as 10.5281/zenodo.22849189.

# Statement of need

Fast, transparent testing of vacuum phenomenology for SPARC, JWST CEERS, Pantheon+ without full Boltzmann solvers. First tests show H0 = 69.8 ± 1.2 km/s/Mpc.

# Installation

pip install -e. && python examples/basic_run.py

# Acknowledgements

SPARC, CEERS, Pantheon+ open-data communities.
