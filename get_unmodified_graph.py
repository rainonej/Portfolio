import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

#gives the graph of Stock Price and Google Searches

SYMBL = 'LTC-USD'
KEY_WORD = 'litecoin'
START_DATE = '2017-06-01'
END_DATE = '2020-12-30'
WIN_SIZE = 3

#Getting the right Data Frames
start_year = START_DATE[:4]
end_year = END_DATE[:4]

price_df = pd.DataFrame({})
searches_df = pd.DataFrame({})

for year in range(int(start_year), int(end_year)+1):
	price_file = "pickles/" + SYMBL + "_price_" + str(year) + ".pkl"
	search_file = "pickles/" + KEY_WORD + "_searches_" + str(year) + ".pkl"
	price_df = pd.concat([price_df, pd.read_pickle(price_file)])
	searches_df = pd.concat([searches_df, pd.read_pickle(search_file)])

price_df = price_df.loc[START_DATE:END_DATE]
searches_df = searches_df.loc[START_DATE:END_DATE]


#Getting the columns we want and Calculating the Rolling Average
price_df = price_df.loc[:, "Open"]
price_df = price_df.rolling(WIN_SIZE).sum()
price_df = price_df.to_frame()

searches_df = searches_df.loc[:, KEY_WORD]
searches_df = searches_df.rolling(WIN_SIZE).sum()
searches_df = searches_df.to_frame()

graph_df = searches_df.join(price_df)
corr = graph_df.corr()
corr = corr.loc['Open', KEY_WORD]
corr = str(np.round(corr, 3))

print("Correlation factor of " + corr)



#Renaming things and drawing the graph
#price_df = price_df.rename(columns = )


plt.figure(figsize = (10,5))
plt.title("Correlation factor of " + corr)
graph_df[KEY_WORD].plot(legend = True, ylabel = 'Google Searches')
graph_df["Open"].plot(secondary_y = True, legend = True)

'''
#searches.plot(ylabel = 'Google Searches')
searches_df.plot(legend = True, ylabel = 'Google Searches')
#price.plot(secondary_y = True)
price_df.plot(secondary_y=True, style='r', legend = True)
#priceroll['Open'].plot(secondary_y=True, style='g', legend = True)

#price['Open'].plot(legend = True, ylabel = 'Price')
#searches['litecoin_unscaled'].plot(secondary_y=True, style='g', legend = True)
'''

plt.show()


