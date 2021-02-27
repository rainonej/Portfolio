from os import path



class Crypto(object):
	"""docstring for Crypto"""
	def __init__(self, name, symbl):
		#super(Crypto, self).__init__()
		self.name = name
		self.symbl = symbl
		self.symblUSD = symbl + '-USD'

		self.__get_price_files__()

	def __get_price_files__(self):

		self.price_years = []
		self.search_years = []

		self.price_files = []
		self.search_files = []

		year = 2015
		while (year <= 2021):

			price_filename = "pickles/" + self.symblUSD + '_price_' + str(year) + '.pkl'
			if path.exists(price_filename):
				self.price_years.append(year)
				self.price_files.append(price_filename)

			year += 1
	


		