import pandas as pd
import numpy as np
from scipy import stats

gdp = pd.read_csv("gdp.csv", index_col="Country")
cpi = pd.read_csv("cpi.csv", index_col="Country")

def describe(df, label):
    print(f"\n--- {label} ---")
    for country in df.index:
        row = df.loc[country].dropna().values
        print(f"{country}: mean={np.mean(row):.2f}, "
              f"var={np.var(row):.2f}, "
              f"skew={stats.skew(row):.2f}")

def correlate(df, label):
    print(f"\n--- {label} Correlation ---")
    print(df.T.corr().round(2))

describe(gdp, "GDP Growth")
describe(cpi, "Inflation")
correlate(gdp, "GDP")
correlate(cpi, "CPI")