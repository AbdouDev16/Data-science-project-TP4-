import numpy as np
import pandas as pd

def generate_month_dates(year=2025):
    return pd.date_range(start=f"{year}-01-01", periods=12, freq='MS')

def generate_random_sales(min_val, max_val, size, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(min_val, max_val+1, size=size)

def generate_initial_dataframe(year=2025, seed=None):
    dates = generate_month_dates(year)
    n = len(dates)
    A = generate_random_sales(50, 100, n, seed=seed)
    B = generate_random_sales(30, 80, n, seed=None if seed is None else seed+1)
    C = generate_random_sales(20, 60, n, seed=None if seed is None else seed+2)
    D = generate_random_sales(10, 50, n, seed=None if seed is None else seed+3)
    df = pd.DataFrame({
        'Date': dates,
        'Product_A': A,
        'Product_B': B,
        'Product_C': C,
        'Product_D': D
    })
    return df
