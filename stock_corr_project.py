import yfinance as yf
import pandas as pd
#import matplotlib
import numpy as np
import matplotlib.pyplot as plt
plt.close("all")

from pytrends.request import TrendReq
from pytrends import dailydata
from pytrendsdaily import getDailyData

svi = getDailyData('Ethereum', 2018, 2018)
svi = svi.reset_index()
pytrends = TrendReq(hl='en-US', tz=360)

start = '2018-01-01'
end = '2018-12-30'
kw = 'Ethereum'
kw_list = [kw]
pytrends.build_payload(kw_list, cat=0, timeframe= start + ' ' + end, geo='', gprop='')
df = pytrends.interest_over_time()
#df2 = pytrends.get_historical_interest(kw_list, year_start=2018, month_start=1, day_start=1, year_end=2019, month_end=1, day_end=1,  cat=0, geo='', gprop='', sleep=0)
#filt = df2[]

#df3 = dailydata.get_daily_data('cinema', 2019, 1, 2019, 10, verbose = False, geo = 'US')

#print(df)
msft = yf.Ticker("ETH-USD")
hist = msft.history(start = start, end = end)
hist = hist.reset_index()
svi = svi.rename(columns={"date": "Date"})

dfnew = pd.merge(hist, svi, how = 'inner')

dfnew = dfnew[['Date', 'Open', 'Ethereum']]
dfnew = dfnew.set_index('Date')
pc = dfnew['Open'].pct_change()
pc = pc.to_frame()
pc = pc.rename(columns = {"Open":"Price_Change"})
dfnew = pd.concat([dfnew, pc], axis=1)
print(dfnew.corr())

dfgraph = dfnew.loc[:,['Open', 'Ethereum']]


plt.figure()
ax = df.plot(secondary_y = ['Ethereum'])
ax.set_ylabel('Google Searches')
ax.right_ax.set_ylabel('Stock Price')
plt.show()


#search_results = list(df[kw])
#eth_price = list(hist['Open'])

#n = len(eth_price)
#m = len(search_results)
#print(n)
#print(m)

#x = list(range(n))

#plt.plot(x,search_results, x, eth_price)
#plt.scatter(search_results, eth_price)
#plt.show()

'''


# get stock info
#msft.info

# get historical market data
hist = msft.history(period="max")



import matplotlib.dates as mdates
import matplotlib.cbook as cbook

plt.plot([1,2,3],[2,3,4], [1,2,3], [5,9,2])

'''
#dfa = pd.DataFrame({'left': ['foo', 'bar']})
#dfb = pd.DataFrame({'right': [7, 8]})