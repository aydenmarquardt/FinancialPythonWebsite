import yfinance as yf
import pandas as pd
import mpld3
from matplotlib import pyplot as plt

def closingPrice(Ticker):
    close = pd.DataFrame(yf.download(Ticker, period = "3mo", interval = '1d')["Adj Close"])
    return close

userTicker = "AAPL"
company = closingPrice(userTicker)
plt.plot(company)
plt.show()