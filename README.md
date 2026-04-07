# Physics Laboratory III — Data Analysis with Python

This repository contains Jupyter notebooks for the Physics Laboratory III course (2nd term, University of Catania). The notebooks introduce Python tools for modern physics data analysis.

## Notebooks

| Notebook | Topic |
|----------|-------|
| `lesson_0.ipynb` | NumPy arrays, linear algebra, symbolic math (SymPy), integration, root finding, curve fitting |
| `lesson_1.ipynb` | File I/O (CSV, MCA), reading spectra, fitting a double Gaussian to Cobalt-60 peaks |
| `lesson_2.ipynb` | Random distributions (uniform, normal, Poisson), rejection sampling, inverse transform sampling |

## Shared Utilities

`lab3_utils.py` — common functions (`chi_squared`, `red_chi_squared`, `gaussian`, `double_gaussian`, `powerlaw`) imported by all notebooks.

## Using Google Colab
Load any notebook here: https://colab.research.google.com/

## Running Locally

Make sure you have an up-to-date conda installation:
```bash
conda update python && conda update conda
```

Create a new environment and install the required packages:
```bash
conda create -n astrolab
conda activate astrolab
conda install numpy scipy matplotlib jupyter sympy
conda install -c conda-forge jupyterlab
pip install wget
```
