import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

#gives the graph of Stock Price and Google Searches

SYMBL = 'LTC-USD'
KEYWORDS = ['litecoin', 'bitcoin']
#KEYWORDS = ['litecoin']
START_DATE = '2018-06-01'
END_DATE = '2020-12-30'
WIN_SIZE = 7

#Getting the right Data Frames
start_year = START_DATE[:4]
end_year = END_DATE[:4]

price_df = pd.DataFrame({})
searches_df = pd.DataFrame({})

#Get Price Data
for year in range(int(start_year), int(end_year)+1):
	price_file = "pickles/" + SYMBL + "_price_" + str(year) + ".pkl"
	price_df = pd.concat([price_df, pd.read_pickle(price_file)])
price_df = price_df.loc[START_DATE:END_DATE]

#Getting the columns we want and Calculating the Rolling Average
price_df = price_df.loc[:, "Open"]
price_df = price_df.rolling(WIN_SIZE).sum()
price_df = price_df.to_frame()


Search_Data_List = []
best_r = -1

for KEYWORD in KEYWORDS:

	#Get Search Data
	for year in range(int(start_year), int(end_year)+1):
		search_file = "pickles/" + KEYWORD + "_searches_" + str(year) + ".pkl"
		searches_df = pd.concat([searches_df, pd.read_pickle(search_file)])
	
	searches_df = searches_df.loc[START_DATE:END_DATE]


	searches_df = searches_df.loc[:, KEYWORD]
	searches_df = searches_df.rolling(WIN_SIZE).sum()
	searches_df = searches_df.to_frame()

	Search_Data_List.append(searches_df)

	graph_df = searches_df.join(price_df)
	corr = graph_df.corr()
	corr = corr.loc['Open', KEYWORD]
	best_r = max(best_r, corr)
#print("Correlation factor of " + corr)
best_r = str(np.round(best_r, 3))


#Creating the Graph
title = str(WIN_SIZE) + " Day Rolling Average\n" + "Best Correlation r = " + best_r
color1 = 'tab:red'
color2 = 'tab:blue'
color_list = ['tab:blue', 'tab:green']

fig = plt.figure(figsize = (15,5)) #Instantiate the Figure
gs = fig.add_gridspec(1, 1) #Choose the grid size for the number of graphs

ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(graph_df["Open"], color = color1)
ax1.set_xlabel('Date')
ax1.set_ylabel('Price in USD', color = color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.legend(["LTC"], loc = "upper left")

ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis
for i in range(len(KEYWORDS)):
	ax2.plot(Search_Data_List[i], color = color_list[i])
	#ax2.legend(['"'+KEYWORD+'"'], loc = "upper right")
#ax2.plot(graph_df[KEYWORD], color = color2)
#ax2.plot(graph_df['litecoin'], color = color2)
ax2.legend(labels = KEYWORDS, loc = "upper right")
ax2.set_ylabel('Google Searches per Day', color = color2)
ax2.tick_params(axis='y', labelcolor=color2)

plt.title(title)
plt.show()
