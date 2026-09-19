# ENGINE

**Open-source phenomenological emulator for active vacuum contributions to cosmic dynamics**

ENGINE is a lightweight computational emulator designed to explore controlled phenomenological extensions to the standard cosmological model. It implements a parametric effective term and allows fast, transparent numerical experiments against public datasets.

> This project is an **emulator / exploratory tool**. It is **not** proposed as a replacement for ΛCDM.

## Features

- Phenomenological effective term with clear recovery of ΛCDM limit
- Interfaces for public datasets (SPARC rotation curves, Pantheon+, JWST CEERS candidates)
- Hybrid Python implementation (Numba-accelerated kernels)
- Fully open-source and reproducible

## Installation

git clone https://github.com/gustavosouzaconde40-ai/ENGINE.git
cd ENGINE
pip install -e .

## Quick start

python examples/basic_run.py

## Current status

- Technology Readiness Level (TRL): 3–4
- Code and documentation under active development
- Aimed at becoming a community-usable tool (target TRL 6)

## Citation

If you use this software, please cite the repository and any associated Zenodo records.

## License

MIT License
