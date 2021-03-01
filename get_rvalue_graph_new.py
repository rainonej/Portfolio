import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from key_words import get_obj
#gives the graph of Stock Price and Google Searches

a = get_obj('ZRX')
START_DATE = '2019-01-01'
END_DATE = '2020-12-30'

def quote(string):
	return '"' + string + '"'


def get_rvalue_graph(obj, start_date, end_date, win_size = 1, verbose = True, boundary = (-5, 5), search_terms = 'Default', graph = True):
	"This is input an object and output a graph"

	if search_terms == 'Default':
		search_terms = obj.search_terms

	#Check that we have sufficient data
	start_year = int(start_date[:4])
	end_year = int(end_date[:4])

	if (start_year in obj.price_data):
		if verbose: print('We have the price data')
	else:
		if verbose: print("Do no have the price data")

	#temp = search_terms
	for year in range(start_year, end_year+1):
		for term in search_terms:
			print(term)
			print(year)
			print(search_terms)
			print(obj.search_data)
			if ((year not in obj.search_data[term]) and (term in search_terms)):
				if verbose: print('Removed', term, 'from search_terms because of insufficient data')
				search_terms.remove(term)
				

	if verbose: print('search terms are now', search_terms)

	## Price Data
	price_df = obj.get_price_df(start_date, end_date) 	#Get the price data 
	price_df = price_df.rolling(win_size).sum()   #Calculate the rolling average
	(predict, react) = boundary	#Preform shifts
	for i in range(predict, react+1):
		temp = price_df['Open'].shift(i)
		temp = temp.to_frame()
		temp = temp.rename(columns = {'Open': 'T=' + str(i)})
		price_df = pd.concat([price_df, temp], axis = 1)
	price_df = price_df.drop(columns = 'Open')
	


	# Search Data
	data_list = []
	for term in search_terms:
		print(term)
		search_df = obj.get_search_df(start_date, end_date, term)

		#print(search_df)
		#print(search_df.info())
		#print(price_df)
		#print(price_df.info())
		#return (price_df, search_df)
		Df = search_df.join(price_df)
		corr = Df.corr()
		if verbose: print(corr.loc[:, term])
		data_list.append(list(corr.loc[:, term])[1:])

	#Create the bar graph
	if graph:
		fig, ax = plt.subplots(figsize = (10,5))
		xlabels = list(map(str, range(predict, react+1)))
		labels = list(map(quote, search_terms))
		n = len(search_terms)
		space = 1
		width = 1/(n+space)
		#width = 1  # the width of the bars
		x = np.arange(len(xlabels))  # the label locations

		for i in range(n):
			ax.bar(x - .5 + (i + space/2 + .5) * width, data_list[i], width, label = labels[i])
		#ax.bar(x , corr_data[0], width, label = quote(KEYWORD))
		#ax.bar(labels, Corr_list, )
		#ax.bar(x + width/2, corr_data[1], width, label = 'Control')

		ax.set_ylabel('r Value')
		ax.set_title('Correlation of ' + obj.name + ' price with Google Searches\n Shifted by T = No. of Days')
		ax.set_xticks(x)
		ax.set_xlabel('Google Predicts Market       <---------       T = # of days       --------->       Google Reacts to Market')
		ax.set_xticklabels(xlabels)
		ax.legend()
		#ax1 = fig.add_subplot(gs[0, 0])
		#ax1.plot(graph_df["Open"], color = color1)

		plt.show()



b = get_rvalue_graph(a, START_DATE, END_DATE)
