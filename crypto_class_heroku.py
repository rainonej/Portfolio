from os import path
import pandas as pd
import yfinance as yf
import pickle
import datetime
from key_words import get_search_path

def get_obj(symbl, save = False):
	filename = 'pickles/objects/' + symbl + '.pkl'
	if path.exists(filename): 
		file = open(filename,'rb')
		obj = pickle.load(file)
		file.close()
	else:
		obj = Crypto(symbl, save = save)
	return obj

class Crypto(object):
	"""docstring for Crypto"""
	def __init__(self, symbl, name = 'NONE', verbose = True, save = False):
		self.name = name
		self.symbl = symbl
		self.verbose = verbose
		self.path = 'pickles/objects/' + self.symbl + '.pkl'

		self.__get_info__() #Creates the name and generates the stock ticker used to get the price data
		self.__get_price_files__() #Creates the price files if they didn't already exists

		if self.verbose: print(self.name, ' or ', self.symbl, ' is done')
		if save: self.update()

	def __get_info__(self):
		#if self.verbose: print('about to summon ticker')

		#tick = yf.Ticker(self.symbl)
		self.tick = yf.Ticker(self.symbl)
		tick = self.tick

		start_date = self.tick.info['startDate']
		start_date = datetime.datetime.fromtimestamp(start_date)
		self.start_year = start_date.year
		start_date = str(start_date)
		self.start_date = start_date[:10]

		if self.name == 'NONE':
			self.name = tick.info['name']

		self.description = tick.info['description']
		

	def __get_price_files__(self):
		"Looks up to see if the price data has already been accessed. If it hasn't, then it requests it."
		"Creates the dictionary to access the price filenames."

		self.price_data = {} #key = year, val = filename
		year = self.start_year
		while (year <= 2021):
			filename = "pickles/price/" + self.symbl + str(year) + '.pkl'
			if path.exists(filename):
				self.price_data[year] = filename
			else:
				start_date = str(year) + '-01-01'
				end_date = str(year+1) + '-01-01'

				tick = self.tick
				hist = tick.history(start = start_date, end = end_date)
				hist = hist.reset_index()
				hist = hist.set_index('Date')
				pc = hist['Open'].pct_change()
				pc = pc.to_frame()
				pc = pc.rename(columns = {"Open":"Price_Change"})
				hist = pd.concat([hist, pc], axis=1)
				if (hist.size != 0):
					hist.to_pickle(filename)
					self.price_data[year] = filename
					if self.verbose: print(filename + ' stored')
			year += 1

	def get_price_df(self, start_date, end_date, edited = True):
		""" 
		input
		start_date = string(2016-01-30)
		end_date = string(2018-06-24)
		edited = bool

		output
		df = panda dataframe of the price files form those years"
		"""
		start_year = int(start_date[:4])
		end_year = int(end_date[:4])

		df = pd.DataFrame({})

		for year in range(start_year, end_year+1):
			filename = self.price_data[year]
			df_year = pd.read_pickle(filename) 
			df = pd.concat([df, df_year ])

		df = df.loc[start_date:end_date, :]

		if edited:
			df = df.loc[:, 'Open']
			df = df.to_frame()

		return df

	def update(self):
		"updates the pickle file"
		pickle.dump(self, open(self.path, "wb"))

		