import pandas as pd
from pytrendsdaily import getDailyData
from os import path
from key_words import key_words, start_year, end_year

for key in key_words:
	for year in range(start_year, end_year+1):
		filename = key + '_searches_' + str(year) + '.pkl'
		if path.exists("pickles/" + filename):
			print(filename + ' already exists')
		else:
			try:
				search_trend = getDailyData(key, year, year, wait_time = 0)
				search_trend = search_trend.reset_index()
				search_trend = search_trend.rename(columns={"date": "Date"})
				search_trend = search_trend.set_index('Date')

				search_trend.to_pickle("pickles/" + filename)
				print(filename + ' stored')
			except:
				print('Google prevented ' + filename + ' from being stored')


