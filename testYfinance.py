import yfinance as yf
import pandas as pd
import mpld3
from matplotlib import pyplot as plt

def closingPrice(Ticker):
    Asset = pd.DataFrame(yf.download(Ticker, period = "3mo", interval = '1d')["Adj Close"])
    return Asset

#userChoice = input("What Companies closing cost would you like to look at?\n")

AAPL = closingPrice("AAPL")
TSLA = closingPrice("TSLA")

plt.plot(TSLA)
plt.plot(AAPL)

plt.show()

