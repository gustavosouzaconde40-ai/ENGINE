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
---

### 2. Métodos para Converter para PDF

#### Método A: Pelo Navegador (Sem instalar software adicional)
1. Abra o ficheiro `.html` original em qualquer navegador (Chrome, Firefox, Edge, Safari).
2. Pressione `Ctrl + P` (Windows/Linux) ou `Cmd + P` (macOS).
3. No destino da impressora, selecione **"Guardar como PDF"**.
4. Ajuste as margens se necessário e clique em **Guardar**.

#### Método B: Via Pandoc (Formatação Académica / JOSS)
Se pretender gerar o PDF com o modelo oficial de publicação científica, utilize o **Pandoc** no terminal:

```bash
pandoc paper.md -o paper.pdf --pdf-engine=xelatex
