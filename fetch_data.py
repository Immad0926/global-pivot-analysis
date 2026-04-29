import wbgapi as wb
import pandas as pd
import time

# Use 3-letter codes for better API stability
COUNTRIES = ["USA", "GBR", "IND", "CAN", "DEU", "JPN"]
YEARS = range(2019, 2025)

def fetch_with_retry(indicator, name):
    print(f"Fetching {name} data...")
    try:
        # We fetch one at a time to avoid overwhelming the API
        df = wb.data.DataFrame(indicator, COUNTRIES, time=YEARS)
        df.index.name = "Country"
        return df
    except Exception as e:
        print(f"Error fetching {name}: {e}")
        return None

if __name__ == "__main__":
    # Fetch GDP
    gdp_df = fetch_with_retry("NY.GDP.MKTP.KD.ZG", "GDP Growth")
    
    # Wait 2 seconds to let the API "breathe"
    time.sleep(2)
    
    # Fetch Inflation
    cpi_df = fetch_with_retry("FP.CPI.TOTL.ZG", "Inflation")

    if gdp_df is not None and cpi_df is not None:
        gdp_df.to_csv("gdp.csv")
        cpi_df.to_csv("cpi.csv")
        print("\n--- DATA LOADED SUCCESSFULLY ---")
        print(gdp_df.head())
    else:
        print("\nStill having API issues. Check your internet connection.")