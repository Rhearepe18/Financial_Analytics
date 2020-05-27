
from datetime import date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf

import pandas as pd

#Select portfolio of stocks
stocks = ['AAPL']  #can add more to portfolio later...


#For example, AAPL stock data from 2000 to 2020  
start_date = '2000-01-01'
end = date.today()   #Current date


def get_data(ticker):
        stock_data = pdr.get_data_yahoo(ticker, start=start_date, end=end)#default is daily data
        return(stock_data)


stockdata = get_data(stocks)

stockdata.to_csv (r'stocks.csv', header=True)


stockdata['Close'].plot()
plt.ylabel("Close price")
plt.show()

