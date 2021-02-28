from os import path
import pandas as pd
import yfinance as yf
import pickle
import datetime

class Crypto(object):
	"""docstring for Crypto"""
	def __init__(self, symbl, name = 'NONE', verbose = True):
		#super(Crypto, self).__init__()
		self.name = name
		self.symbl = symbl
		self.symblUSD = symbl + '-USD'
		self.search_terms = []
		self._verbose = verbose

		self.path = 'pickles/objects/' + self.symbl + '.pkl'

		self.__get_info__()
		self.search_terms = list(set(self.search_terms))

		self.__get_price_files__()
		self.__get_search_files__()

		if self._verbose: 
			print(self.name, 'search terms', self.search_terms)
			print(self.name, ' or ', self.symbl, ' is done')

	def __get_price_files__(self):
		"Creates the dictionary to access the price filenames."

		self.price_data = {} #key = year, val = filename
		year = self.start_year
		while (year <= 2021):
			filename = "pickles/" + self.symblUSD + '_price_' + str(year) + '.pkl'
			if path.exists(filename):
				self.price_data[year] = filename
			year += 1

	def __get_search_files__(self):
		"Creates the dictionaries to access search filenames"
		self.search_data = {} #key = word, val = {year:file_name}
		for term in self.search_terms:
			self.search_data[term] = {}
			year = self.start_year
			while (year <= 2021):
				filename = "pickles/" + term + '_searches_' + str(year) + '.pkl'
				if path.exists(filename):
					self.search_data[term][year] = filename		
				year +=1		
	
	def __get_info__(self):
		#if self._verbose: print('about to summon ticker')

		#tick = yf.Ticker(self.symblUSD)
		self.tick = yf.Ticker(self.symblUSD)
		tick = self.tick

		start_date = self.tick.info['startDate']
		start_date = datetime.datetime.fromtimestamp(start_date)
		self.start_year = start_date.year
		start_date = str(start_date)
		self.start_date = start_date[:10]

		if self.name == 'NONE':
			self.name = tick.info['name']


		self.description = tick.info['description']
		terms = tick.info['companyOfficers']

		for atrb in ['twitter', 'name']:
			if atrb in tick.info:
				terms.append(tick.info[atrb])

		terms.append(self.symbl + ' USD')
		self.search_terms += terms

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
			df = pd.concat([df, pd.read_pickle(filename) ])

		df = df.loc[start_date:end_date, :]

		if edited:
			df = df.loc[:, 'Open']
			df = df.to_frame()

		return df

	def update(self):
		"updates the pickle file"
		pickle.dump(self, open(self.path, "wb"))

	def add_search_terms(self, words):
		"adds the list of search terms to the object, and updates it."
		self.search_terms += words
		self.search_terms = list(set(self.search_terms))
		self.__get_search_files__()
		self.update()

	def update_search_files(self):
		"updates the search files"
		self.__get_search_files__()
		self.update()


		
#a = Crypto('lite', 'LTC', search_terms = ['litecoin'])
		