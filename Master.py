import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pytrendsdaily import getDailyData
import yfinance as yf

#### Set Key Words
start_year = 2020
end_year = 2021
key_words = ['Dogecoin']
SYMBL = 'DOGE-USD'

start_date = str(start_year) + '-01-01'
end_date = str(end_year) + '-01-01'


### Get Data
print('This will take about a while (about 90 secs). Google does not like too many requests at once.')

msft = yf.Ticker(SYMBL)
hist = msft.history(start = start_date, end = end_date)
hist = hist.reset_index()
hist = hist.set_index('Date')
pc = hist['Open'].pct_change()
pc = pc.to_frame()
pc = pc.rename(columns = {"Open":"Price_Change"})
hist = pd.concat([hist, pc], axis=1)

files = {}
for key_word in key_words:
	
	search_trend = getDailyData(key_word, start_year, end_year-1, wait_time = 5.0)
	search_trend = search_trend.reset_index()
	search_trend = search_trend.rename(columns={"date": "Date"})
	search_trend = search_trend.set_index('Date')
	files[key_word] = search_trend


### Modify the Data
for key_word in key_words:
	df = hist.join(files[key_word])
	df = df[['Open', key_word, 'Price_Change']]
	
	df_mod = df
	max_shift = 0
	shift_start = -30
	for i in range(shift_start, max_shift+1):
		temp = df['Open'].shift(i)
		temp = temp.to_frame()
		temp = temp.rename(columns = {'Open':'Open' + str(i)})
		df_mod = df_mod.join(temp)

	ser = df[key_word]
	start_p_slice = 4
	stop_p_slice = 40
	for p in range(start_p_slice, stop_p_slice+1):
		p = p/10
		temp = ser.apply(lambda x: np.sign(x) * np.absolute(x)**p )
		temp = temp.to_frame()
		temp = temp.rename(columns = {key_word:key_word + 'p' + str(int(p*10))})
		df_mod = df_mod.join(temp)

	### Optimize the Data for strongest correlation
	corr = df_mod.corr()
	start_slice = 'Open' + str(shift_start)
	stop_slice = 'Open' + str(max_shift)
	start_p_slice = key_word + 'p' + str(start_p_slice)
	stop_p_slice = key_word + 'p' + str(stop_p_slice)
	corr2 = corr.loc[start_slice:stop_slice, start_p_slice:stop_p_slice]


	max_list = corr2.idxmax()
	max_list = max_list.to_frame()
	max_list = max_list.reset_index()
	
	[lis, max_val, final_shift, final_p] = [[], 0, '' ,'']
	n = len(max_list) 

	for i in range(n):
		p_val = max_list.loc[i, 'index']
		shift_val = max_list.loc[i,0]
		val = corr2.loc[shift_val, p_val]
		lis.append(val)
		if (val>= max_val):
			final_shift = shift_val
			final_p = p_val
			max_val = val

	print('best correlation is ' + final_p + ' and ' + final_shift + ' at ' + str(max_val))

	df_graph = df_mod[[final_p, final_shift, 'Open']]
	columns = {final_p: "'" + key_word + "'" + ' Searches', final_shift: 'Shifted ' + key_word + ' Price', 'Open': 'Original ' + key_word + ' Price'}
	graph = df_graph.rename(columns = columns)

	searches = key_word
	stock_shift = 'Shifted Stock Price'
	plt.figure()
	graph[columns[final_p]].plot(legend = True, ylabel = 'Google Searches')
	#temp = 'Open-25'
	#ax.set_ylabel('Google Searches')

	graph[columns[final_shift]].plot(secondary_y=True, style='g', legend = True)
	#df.plot(secondary_y=True, style='g')


	#file_name = SYMBL + '.png'
	#file_name = 'test.png'
	#plt.savefig(file_name)
	plt.show()




