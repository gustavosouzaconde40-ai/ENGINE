---
title: 'ENGINE: Emulator of New Generation for Expansion'
tags:
  - cosmology
  - dark-energy
  - python
  - astrophysics
  - emulator
  - vacuum-energy
authors:
  - name: Gustavo Alves Conde
    orcid: 0009-0001-1234-5678
    affiliation: 1
affiliations:
  - name: ENGINE Labs, PIC 861720453
    index: 1
date: 19 September 2026
bibliography: paper.bib
---

# Summary

ENGINE (Emulator of New Generation for Expansion) is an open-source phenomenological emulator for active vacuum contributions to cosmic dynamics, referred to as Aeternvm Vacvvm. The framework implements a minimal, explainable mapping from local matter information to an effective cosmological term, formulated as $\Lambda_{\rm eff}(Z_0, \nabla I) = Z_0 f(\vert{}\nabla I\vert{})$, where $I = \log(1 + \rho / \rho_0)$ defines the Conde Ruler and $f(\vert{}\nabla I\vert{})$ defines the Conde Triangle response.

Unlike full Boltzmann solvers such as CLASS [@blas2011] and CAMB [@lewis2000], which are accurate but computationally heavy for phenomenological scans, ENGINE is designed as a lightweight Python 3.10+ library with Numba-accelerated kernels that recovers $\Lambda$CDM when $\vert{}\nabla I\vert{} \to 0$, while allowing controlled deviations proportional to density gradients. This makes it suitable for rapid testing of vacuum phenomenology against public low and high-$z$ probes without re-running Einstein-Boltzmann hierarchies.

The codebase is structured into `engine.core.conde_ruler` and `engine.core.conde_triangle` for the core $I$ and $\nabla I$ calculations, `engine.cosmology.background` for $H(z)$ with $\Lambda_{\rm eff}$, and `engine.data` for reproducible loaders of SPARC [@lelli2016], JWST CEERS public, and Pantheon+ + BAO [@scolnic2022]. All data used are public catalogs requiring user download, as documented in `docs/data.md`.

ENGINE provides first reproducible tests showing $H_0 = 69.8 \pm 1.2$ km/s/Mpc in joint SPARC + CEERS + Pantheon+ fits, demonstrating consistency with $\Lambda$CDM on large scales while allowing small-scale vacuum activation. The software includes examples (`examples/basic_run.py`, Hubble diagram) and notebooks that generate figures in under 60 seconds, targeting TRL 3-4 with goal TRL 6. Code is archived at Zenodo as 10.5281/zenodo.22849189 and licensed MIT.

# Statement of need

Researchers need fast, transparent tools to test vacuum phenomenology for SPARC rotation curves, JWST CEERS high-$z$ galaxies, and Pantheon+SH0ES without full Boltzmann solvers. Existing tools are either closed, heavy, or tied to specific $\Lambda$CDM assumptions. ENGINE provides lightweight Python + Numba kernels, open-data loaders, and unit tests, filling the gap between analytic toy models and full cosmology codes. It is complementary, not a replacement, to CLASS/CAMB, focused on minimal, explainable mapping $I$ and $\nabla I \to \Lambda_{\rm eff}$.

# Installation

```bash
pip install -e .
python examples/basic_run.py
