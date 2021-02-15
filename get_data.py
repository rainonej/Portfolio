#Normal libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#For getting my data 
from pytrends.request import TrendReq
from pytrends import dailydata
from pytrendsdaily import getDailyData
import yfinance as yf

start_year = 2018
end_year = 2019
key_word = 'Ethereum'


search_trend = getDailyData(key_word, start_year, end_year-1)
search_trend = search_trend.reset_index()


#pytrends = TrendReq(hl='en-US', tz=360)

start_date = str(start_year) + '-01-01'
end_date = str(end_year) + '-01-01'



msft = yf.Ticker("ETH-USD")
hist = msft.history(start = start_date, end = end_date)
hist = hist.reset_index()
search_trend = search_trend.rename(columns={"date": "Date"})

dfnew = pd.merge(hist, search_trend, how = 'inner')
dfnew = dfnew.set_index('Date')
pc = dfnew['Open'].pct_change()
pc = pc.to_frame()
pc = pc.rename(columns = {"Open":"Price_Change"})
dfnew = pd.concat([dfnew, pc], axis=1)
dfnew.to_pickle("./df_full.pkl")

dfnew = dfnew[['Ethereum', 'Open', 'Price_Change']]

print(dfnew.corr())

dfgraph = dfnew.loc[:,['Open', 'Ethereum']]

dfgraph.to_pickle("./dfgraph.pkl")