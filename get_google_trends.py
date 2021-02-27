import pandas as pd
from pytrendsdaily import getDailyData
from os import path
from key_words import key_words, start_year, end_year, SYMBLs

print('key words = ')
print(key_words)

duration = 1 #number of mins it will run for
import time
timeout = time.time() + 60*duration  

verbose = True
updates = True
update_time = 15 # 15 seconds


while True:

	if updates: print('New cycle started')

	succeeded = 0
	failed = 0
	update = time.time()

	for key in key_words:
		for year in range(start_year, end_year+1):
			filename = key + '_searches_' + str(year) + '.pkl'
			if path.exists("pickles/" + filename):
				if verbose: print(filename + ' already exists')
			else:

				if verbose: print('Attempting to get', key,  year)
				search_trend = getDailyData(key, year, year, wait_time = 5, verbose = verbose)
				try:
					if verbose: print('Attempting to get', key,  year)
					search_trend = getDailyData(key, year, year, wait_time = 0, verbose = verbose)
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
					mins = int((timeout - time.time())/60)
					secs = int((timeout - time.time())%60)
					print(mins, ':', secs, ' remain')

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


