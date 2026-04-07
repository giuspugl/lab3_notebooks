import numpy as np

# chi2
def chi_squared(y_obs, y_exp, errors):
    return np.sum(((y_obs - y_exp) / errors) ** 2)

# reduced chi2
def red_chi_squared(y_obs, y_exp, errors, n_params):
    """
    - y_obs :observed values
    - y_exp : expected theoretical values from model
    - errors : errors on y_obs
    - n_params : number of parameters being fitted
    """
    return np.sum(((y_obs - y_exp) / errors) ** 2) / (y_obs.size - n_params - 1)

def gaussian(x, A, mu, sigma):
    return A * np.exp(-(x - mu)**2 / 2 / (sigma**2))

def double_gaussian(x, A1, mu1, sigma1, A2, mu2, sigma2):
    return gaussian(x, A1, mu1, sigma1) + gaussian(x, A2, mu2, sigma2)

def powerlaw(x, A, alpha):
    return A * x**alpha

def exponential_decay(x, A, lam):
    """Exponential decay/absorption: A * exp(-x / lam)"""
    return A * np.exp(-x / lam)

def double_gaussian_with_bg(x, A1, mu1, sigma1, A2, mu2, sigma2, m, c):
    """Double Gaussian + linear background."""
    return double_gaussian(x, A1, mu1, sigma1, A2, mu2, sigma2) + m * x + c
