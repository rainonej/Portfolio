import pandas as pd
import yfinance as yf
from os import path
from os import remove
from key_words import SYMBLs, start_year, end_year, get_obj
import pickle

def check_size(string):
	file = open(string, 'rb')
	obj = pickle.load(file)
	#file.close()
	return (obj.size != 0)

#SYMBLs = ['LTC']
for SYMBL in SYMBLs:
	obj = get_obj(SYMBL)
	start_year = obj.start_year

	for year in range(start_year, end_year+1):
		filename = "pickles/" + obj.symblUSD + '_price_' + str(year) + '.pkl'
		
		if path.exists(filename):
			if check_size(filename):
				print(filename + ' already exists')
			else:
				remove(filename)
				print(filename, "is wrong")

		else:
			start_date = str(year) + '-01-01'
			end_date = str(year+1) + '-01-01'

			tick = yf.Ticker(obj.symblUSD)
			hist = tick.history(start = start_date, end = end_date)
			hist = hist.reset_index()
			hist = hist.set_index('Date')
			pc = hist['Open'].pct_change()
			pc = pc.to_frame()
			pc = pc.rename(columns = {"Open":"Price_Change"})
			hist = pd.concat([hist, pc], axis=1)
			if (hist.size != 0):
				hist.to_pickle(filename)
				print(filename + ' stored')

	obj.__get_price_files__()
	obj.update()
