import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from key_words import get_obj, get_search_path
from os import path

#gives the graph of Stock Price and Google Searches

a = get_obj('LTC')
START_DATE = '2018-01-01'
END_DATE = '2020-12-30'

def quote(string):
	return '"' + string + '"'

def get_corr(s1, s2, fun = lambda x: x):
	"""
	input
	s1 = series
	s2 = series
	fun = function
	"""
	s2 = s2.apply(fun)
	s2= s2.to_frame()
	s1 = s1.to_frame()
	c1 = s1.columns[0]
	c2 = s2.columns[0]

	df = s1.join(s2)
	corr = df.corr()
	return corr.loc[c1, c2]


def best_corr(price_ser, search_ser):
	"""
	input
	price_ser = series (price of stuff)
	search_ser = series (search results)

	runs through a bunch of functions and finds the best transformation

	output 
	best correlation factor
	best modified search_ser
	"""

	#p^th power
	search_mod = None
	max_corr = 0
	best_p = 0
	for i in range(1, 601):
		p = i/100
		corr = get_corr(price_ser, search_ser, lambda x: x**p)
		if (abs(corr)>= abs(max_corr)):
			max_corr = corr
			search_mod = search_ser.apply(lambda x: x**p)
			best_p = p

	print('best p = ', best_p)
	print('r = ', max_corr)
	return (search_mod, best_p)

def censure_search_terms(obj, start_date, end_date, search_terms, extra_terms, verbose = True):
	#Check that we have sufficient data
	start_year = int(start_date[:4])
	end_year = int(end_date[:4])

	if (start_year in obj.price_data):
		if verbose: print('We have the price data')
	else:
		if verbose: print("Do no have the price data")
		return ":("

	for year in range(start_year, end_year+1):
		for term in search_terms:
			if ((year not in obj.search_data[term]) and (term in search_terms)):
				if verbose: print('Removed', term, 'from search_terms because of insufficient data')
				search_terms.remove(term)

		for term in extra_terms:
			if (not path.exists(get_search_path(term, year)) and (term in extra_terms)):
				if verbose: print('Removed', term, 'from extra_terms because of insufficient data')
				extra_terms.remove(term)

	search_terms = search_terms + extra_terms
	if verbose: print('search terms are now', search_terms)
	return search_terms


def get_rvalue_graph(obj, start_date, end_date, win_size = 1, verbose = True, boundary = (-5, 5), search_terms = 'Default', extra_terms = [], graph = True, modified = True):
	"This is input an object and output a graph"

	if search_terms == 'Default':
		search_terms = obj.search_terms

	#Check that we have sufficient data
	search_terms = censure_search_terms(obj, start_date, end_date, search_terms, extra_terms, verbose = verbose)
	

	## Price Data
	price_df = obj.get_price_df(start_date, end_date, edited = True) 	#Get the price data 
	#return price_df
	price_df = price_df.rolling(win_size).sum()   #Calculate the rolling average
	(predict, react) = boundary	#Preform shifts
	for i in range(predict, react+1):
		temp = price_df['Open'].shift(i)
		temp = temp.to_frame()
		temp = temp.rename(columns = {'Open': 'T=' + str(i)})
		price_df = pd.concat([price_df, temp], axis = 1)
	price_df = price_df.drop(columns = 'Open')

	# Search Data and Correlation
	data_list = []
	for term in search_terms:
		print(term)
		search_df = obj.get_search_df(start_date, end_date, term, outside = True)

		if modified:
			s2 = search_df[term]
			s1 = price_df['T=0']
			(s2, tp) = best_corr(s1, s2)
			search_df = s2.to_frame()

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
		x = np.arange(len(xlabels))  # the label locations

		for i in range(n):
			ax.bar(x - .5 + (i + space/2 + .5) * width, data_list[i], width, label = labels[i])

		ax.set_ylabel('r Value')
		if modified: title = 'Correlation of ' + obj.name + ' price with (modified) Google Searches\n Shifted by T = No. of Days'
		else:
			title = 'Correlation of ' + obj.name + ' price with Google Searches\n Shifted by T = No. of Days'
		if (win_size != 1): title += '\n Rolling average taken over ' + str(win_size) + ' days'
		ax.set_title(title)
		ax.set_xticks(x)
		ax.set_xlabel('Google Predicts Market       <---------       T = # of days       --------->       Google Reacts to Market')
		ax.set_xticklabels(xlabels)
		ax.legend()
		#ax.annotate('Something', xy=(-0.05, 1.05), xycoords='axes fraction')
		plt.show()


'''
b = get_rvalue_graph(a, START_DATE, END_DATE, win_size = 3, extra_terms = ['Bitcoin'], graph = False)




s1 = a.get_price_df(START_DATE, END_DATE)
s1 = s1['Open']
s1 = s1.shift(-2)
s2 = a.get_search_df(START_DATE, END_DATE, 'Litecoin', outside = True)
s2 = s2['Litecoin']
best_corr(s1, s2)
'''