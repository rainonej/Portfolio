import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

#gives the graph of Stock Price and Google Searches

SYMBL = 'LTC-USD'
KEYWORDS = ['litecoin', 'bitcoin', 'Pasta']
#KEYWORD = 'crypto market'
START_DATE = '2018-06-01'
END_DATE = '2020-12-30'
WIN_SIZE = 7

def quote(string):
	return '"' + string + '"'

#Getting the right Data Frames
start_year = START_DATE[:4]
end_year = END_DATE[:4]

corr_data = []

for KEYWORD in KEYWORDS:

	price_df = pd.DataFrame({})
	searches_df = pd.DataFrame({})

	for year in range(int(start_year), int(end_year)+1):
		price_file = "pickles/" + SYMBL + "_price_" + str(year) + ".pkl"
		search_file = "pickles/" + KEYWORD + "_searches_" + str(year) + ".pkl"
		price_df = pd.concat([price_df, pd.read_pickle(price_file)])
		searches_df = pd.concat([searches_df, pd.read_pickle(search_file)])

	price_df = price_df.loc[START_DATE:END_DATE]
	searches_df = searches_df.loc[START_DATE:END_DATE]


	#Getting the columns we want and Calculating the Rolling Average
	price_df = price_df.loc[:, "Open"]
	price_df = price_df.rolling(WIN_SIZE).sum()
	price_df = price_df.to_frame()

	searches_df = searches_df.loc[:, KEYWORD]
	searches_df = searches_df.rolling(WIN_SIZE).sum()
	searches_df = searches_df.to_frame()

	graph_df = searches_df.join(price_df)


	corr = graph_df.corr()
	corr = corr.loc['Open', KEYWORD]
	corr = str(np.round(corr, 3))
	print("Correlation factor of " + corr)

	#df_mod = graph_df
	shift_start = -5
	max_shift = 5
	Corr_list = []

	for i in range(shift_start, max_shift+1):
		print(i)
		temp = graph_df['Open'].shift(i)
		temp = temp.to_frame()
		temp = temp.rename(columns = {'Open':'Open' + str(i)})
		#df_mod = df_mod.join(temp)
		temp = pd.concat([temp, searches_df], axis = 1)
		temp = temp.corr()
		Corr_list.append(temp.loc[KEYWORD,'Open' + str(i)])

	print(Corr_list)
	corr_data.append(Corr_list)

#print('About to calculate Correlation Matrix')
#corr = df_mod.corr()
print(Corr_list)
xlabels = list(map(str, range(shift_start, max_shift+1)))
#fig = plt.figure(figsize = (5,5)) #Instantiate the Figure
#gs = fig.add_gridspec(1, 1) #Choose the grid size for the number of graphs

#ax = fig.add_axes(list(price_df["Open"]))
#ax = fig.add_axes([0,0,1,1])


fig, ax = plt.subplots(figsize = (10,5))

labels = list(map(quote, KEYWORDS))
n = len(KEYWORDS)
space = 1
width = 1/(n+space)
#width = 1  # the width of the bars
x = np.arange(len(xlabels))  # the label locations

for i in range(n):
	ax.bar(x - .5 + (i + space/2 + .5) * width, corr_data[i], width, label = labels[i])
#ax.bar(x , corr_data[0], width, label = quote(KEYWORD))
#ax.bar(labels, Corr_list, )
#ax.bar(x + width/2, corr_data[1], width, label = 'Control')

ax.set_ylabel('r Value')
ax.set_title('Correlation of LTC price with Google Searches\n Shifted by T = No. of Days')
ax.set_xticks(x)
ax.set_xlabel('Google Predicts Market       <---------       T = # of days       --------->       Google Reacts to Market')
ax.set_xticklabels(xlabels)
ax.legend()
#ax1 = fig.add_subplot(gs[0, 0])
#ax1.plot(graph_df["Open"], color = color1)

plt.show()


'''


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
ax2.plot(graph_df[KEYWORD], color = color2)
ax2.set_ylabel('Google Searches per Day', color = color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.legend(['"'+KEYWORD+'"'], loc = "upper right")

plt.title(title)
plt.show()
'''