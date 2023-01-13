import yfinance as yf
import pandas as pd
import mpld3
from matplotlib import pyplot as plt
import cryptocmd as ccmd



def test():
    Ticker = "BTC"
    
    scraper = ccmd.CmcScraper(Ticker, "15-10-2014", "15-10-2022")
    
    Data = scraper.get_dataframe()
    
    closingPrice = Data["Close"]
    
    Date = Data["Date"]

    plt.plot(Date, closingPrice)
    plt.show()

test()