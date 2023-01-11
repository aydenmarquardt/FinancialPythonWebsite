from matplotlib import pyplot as plt
from Historic_Crypto import HistoricalData
import pandas as pd

def CryptoClosingPrice(Ticker):
    closing = HistoricalData(ticker = Ticker, granularity = 86400, start_date = '2020-06-01-00-00', end_date = '2022-06-01-00-00', verbose = False).retrieve_data()

    closing = closing["Close"]

    return closing

ticker = "BTC" + "-USD"

cryptoHistoricalPrice = CryptoClosingPrice(ticker)

print(cryptoHistoricalPrice)
