import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

#gives the graph of Stock Price and Google Searches

SYMBL = 'LTC-USD'
KEY_WORD = 'litecoin'
START_DATE = '2017-06-01'
END_DATE = '2020-12-30'
WIN_SIZE = 7

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
#print("Correlation factor of " + corr)


#Creating the Graph
title = str(WIN_SIZE) + " Day Rolling Average\n" + "r = " + corr
color1 = 'tab:red'
color2 = 'tab:blue'

fig = plt.figure(figsize = (10,5)) #Instantiate the Figure
gs = fig.add_gridspec(1, 1) #Choose the grid size for the number of graphs

ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(graph_df["Open"], color = color1)
ax1.set_xlabel('Date')
ax1.set_ylabel('Price in USD', color = color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.legend(["LTC"], loc = "upper left")

ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis
ax2.plot(graph_df[KEY_WORD], color = color2)
ax2.set_ylabel('Google Searches per Day', color = color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.legend(['"Litecoin"'], loc = "upper right")

plt.title(title)
plt.show()
