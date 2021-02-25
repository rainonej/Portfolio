import pandas as pd
import yfinance as yf
from os import path
from key_words import SYMBLs, start_year, end_year

for SYMBL in SYMBLs:
	for year in range(start_year, end_year+1):
		filename = SYMBL + '_price_' + str(year) + '.pkl'
		
		if path.exists("pickles/" + filename):
			print(filename + ' already exists')
		
		else:
			start_date = str(year) + '-01-01'
			end_date = str(year+1) + '-01-01'

			tick = yf.Ticker(SYMBL)
			hist = tick.history(start = start_date, end = end_date)
			hist = hist.reset_index()
			hist = hist.set_index('Date')
			pc = hist['Open'].pct_change()
			pc = pc.to_frame()
			pc = pc.rename(columns = {"Open":"Price_Change"})
			hist = pd.concat([hist, pc], axis=1)
			hist.to_pickle("pickles/" + filename)
			print(filename + ' stored')
