import yfinance as yf
import pandas as pd
import mpld3
from matplotlib import pyplot as plt

def closingPrice(Ticker):
    close = pd.DataFrame(yf.download(Ticker, period = "3mo", interval = '1d')["Adj Close"])
    return close

#userChoice = input("What Companies closing cost would you like to look at?\n")

amtOfStocks = input("How many stocks would you like to add?\n")

amtOfStocks = int(amtOfStocks)

while amtOfStocks > 0:
    userTicker = input("Company youd like to add\n")
    company = closingPrice(userTicker)
    plt.plot(company)

    amtOfStocks -= 1

plt.show()
