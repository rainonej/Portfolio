import pandas as pd
from pytrendsdaily import getDailyData
from os import path
from key_words import key_words, start_year, end_year, SYMBLs, get_obj


# Look into this: https://stackoverflow.com/questions/2831775/running-a-python-script-for-a-user-specified-amount-of-time

def search_path(term, year):
	"returns the path you wanted in a string form"
	return "pickles/" + term + '_searches_' + str(year) + '.pkl'


def get_search_data(obj, verbose = True, very_verbose = True):
	"Given a crypto object, it will request the search data for all the search terms starting from the start year"
	for term in obj.search_terms:
		for year in range(obj.start_year, 2021):
			filepath = search_path(term, year)
			if path.exists(filepath):
				if verbose: print(filepath, 'already exists')
			else:
				try:
					if verbose: print('Attempting to get', term,  year)
					search_trend = getDailyData(term, year, year, wait_time = 0, verbose = very_verbose)
					search_trend = search_trend.reset_index()
					search_trend = search_trend.rename(columns={"date": "Date"})
					search_trend = search_trend.set_index('Date')
					search_trend.to_pickle(filepath)
					obj.update_search_files()


					if verbose: print(filepath + ' stored')
				except:
					if verbose: print('Google prevented ' + filepath + ' from being stored')

a = get_obj('BTC')
get_search_data(a)

'''
import random

years = list(range(start_year, end_year+1))

print('key words = ')
#print(key_words)

duration = 5 #number of mins it will run for
verbose = True
very_verbose = False
updates = True
update_time = 15 # 15 seconds
shuffle = False

import time
timeout = time.time() + 60*duration  

if shuffle:
	random.shuffle(key_words)
	random.shuffle(years)
	print(key_words)
	print(years)
else:
	print(key_words)




while True:

	if updates: print('New cycle started')

	succeeded = 0
	failed = 0
	update = time.time()

	for key in key_words:
		for year in years:
			filename = key + '_searches_' + str(year) + '.pkl'
			if path.exists("pickles/" + filename):
				if verbose: print(filename + ' already exists')
			else:
				try:
					if verbose: print('Attempting to get', key,  year)
					search_trend = getDailyData(key, year, year, wait_time = 0, verbose = very_verbose)
					search_trend = search_trend.reset_index()
					search_trend = search_trend.rename(columns={"date": "Date"})
					search_trend = search_trend.set_index('Date')

					search_trend.to_pickle("pickles/" + filename)
					if verbose: print(filename + ' stored')
					succeeded += 1
				except:
					if verbose: print('Google prevented ' + filename + ' from being stored')
					failed += 1

			if updates:
				if (time.time() > update):
					update = time.time() + update_time
					print(succeeded, ' succeeded, and ', failed, ' failed so far in this cycle')
					minus = ''
					if (timeout - time.time())<0:
						minus = '-'
					mins = int((timeout - time.time())/60)
					secs = int((timeout - time.time())%60)
					print(minus, mins, ':', secs, ' remain')

			if time.time() > timeout:
				break
		if time.time() > timeout:
			break
	if time.time() > timeout:
		if (updates or verbose):
			print('Timed out.')
		break

	if (failed == 0):
		if (updates or verbose):
			print('Finished!')
		break

	if updates: print('Cycle finished.\n', succeeded, ' succeeded, and ', failed, ' failed this cycle')


'''