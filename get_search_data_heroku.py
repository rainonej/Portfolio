import pandas as pd
from pytrendsdaily import getDailyData
from os import path



def get_search_df(term, start_date, end_date, edited = True, verbose = True, save = True):
	""" 
	input
	start_date, end_date = string(YYYY-MM-DD)
	term = string
	edited, verbose, save = bool

	output
	df = panda dataframe of the search files form those years"
	"""
	start_year = int(start_date[:4])
	end_year = int(end_date[:4])

	df = pd.DataFrame({})

	for year in range(start_year, end_year+1):
		filename = "pickles/" + term + '_searches_' + str(year) + '.pkl'
		if path.exists(filename):
			search_trend = pd.read_pickle(filename)
		else:
			search_trend = getDailyData(term, year, year, wait_time = 0, verbose = verbose)
			search_trend = search_trend.reset_index()
			search_trend = search_trend.rename(columns={"date": "Date"})
			search_trend = search_trend.set_index('Date')
			if save: search_trend.to_pickle(filename)
		df = pd.concat([df, search_trend])

	df = df.loc[start_date:end_date, :]

	print('you searched for', term)
	if verbose: print(df)
	if edited:
		df = df.loc[:, term]
		df = df.to_frame()

	return df

a = get_search_df('Block Chain', '2018-01-01', '2018-12-31', save = True)