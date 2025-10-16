import yfinance as yf
import pandas as pd

def fetch_prices():
    commodity = yf.download("CL=F", start="2025-01-01", end="2025-10-01")
    commodity.reset_index(inplace=True)
    commodity = commodity[["Date", "Close"]]
    commodity.to_csv("data/commodity_prices.csv", index=False)
    print("Commodity prices fetched!")

if __name__ == "__main__":
    fetch_prices()
