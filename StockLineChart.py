import yfinance as yf
import pandas as pd
import mpld3
from matplotlib import pyplot as plt
from multipledispatch import dispatch

@dispatch(str)
def test(Ticker):
    stockData = yf.download(Ticker)   
    plt.plot(stockData["Close"])
    plt.show()

@dispatch(str, str, str)
def test(Ticker, Start, End):
    stockData = yf.HistocalPrices()
    
    print(stockData)


Ticker = "AMZN"
start="2017-01-01"
end="2017-04-30"
Interval = "5d"
test(Ticker)