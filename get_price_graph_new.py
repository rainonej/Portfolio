import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from key_words import get_obj, get_search_path
from os import path
from get_rvalue_graph_new import censure_search_terms, best_corr
# prints out the line graph 

def get_graph(obj, start_date = 'DEFAULT', end_date = 'DEFAULT', search_terms = 'DEFAULT', extra_terms = [], win_size = 1, modified = True, verbose = True, graph = True):
	"Prints out the graph"

	#Change default values
	if start_date == 'DEFAULT':
		start_date = str(min(list(obj.price_data)))
		start_date += '-01-01'
	if end_date == 'DEFAULT':
		end_date = str(max(list(obj.price_data)))
		end_date += '-12-31'
	if search_terms == 'DEFAULT':
		search_terms = obj.search_terms

	#Correct the search terms
	search_terms = censure_search_terms(obj, start_date, end_date, search_terms, extra_terms, verbose)

	#Get Data
	price_df = obj.get_price_df(start_date, end_date, edited = True)
	price_df = price_df.rolling(win_size).sum() 

	#print(price_df)
	search_df = price_df.drop(columns =['Open'])
	#print(search_df)
	if modified: Ps = []
	for term in search_terms:
		temmp_df = obj.get_search_df(start_date, end_date, term, edited = True, outside = True, verbose = False)
		temmp_df = temmp_df.rolling(win_size).sum() 
		if modified:
			s1 = price_df['Open']
			s2 = temmp_df[term]
			(temmp_df, p) = best_corr(s1, s2)
			Ps.append(p)
			temmp_df = temmp_df.to_frame()
		search_df = search_df.join(temmp_df)  
	#return search_df

	#Graph
	if graph:

		fig, ax1 = plt.subplots(figsize = (10,5))
		ax2 = ax1.twinx()

		#ax1.plot(search_df['Litecoin'])
		#search_df['Litecoin'].plot(ax = ax1)
		search_df.plot(ax = ax1)
		print(price_df)
		price_df.plot(ax = ax2, color = 'tab:red')
		#ax2.plot(price_df['Open'], color = 'tab:red')
		
		#plt.figure()
		#search_df['Litecoin'].plot()
		#fig = plt.figure(figsize = (5,5)) #Instantiate the Figure
		#gs = fig.add_gridspec(1, 1) #Choose the grid size for the number of graphs
		ax1.set_title('Graph')	
		if modified:
			ax1.set_ylabel('Google Searches* per day')	
		else:
			ax1.set_ylabel('Google Searches per day')
		ax2.set_ylabel('Price')
		ax2.legend(loc = "upper right")

		if modified:
			L = list(search_df.columns)
			L2 = []
			script = 'Google Searches were taken to the power of p where \n'
			for i in range(len(L)):
				L2.append(L[i] + (i+1) * '*')
				script += 'p' + (i+1)*'*' + ' = ' + str(Ps[i]) + '\n'
			ax1.legend(L2, loc = "upper left")

			ax1.annotate(script, xy=(0.05, -0.35), xycoords='axes fraction')
		else:
			ax1.legend(loc = "upper left")

		plt.show()


START_DATE = '2018-10-20'
END_DATE = '2018-12-30'
a = get_obj('LTC')
b = get_graph(a, start_date = START_DATE, end_date = END_DATE, win_size = 1, search_terms = ['Litecoin'])