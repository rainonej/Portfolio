import pandas as pd
import numpy as np
from key_words import start_year, end_year, key_words, SYMBL

key_word = 'Ethereum'
#Import Data
search_data = pd.read_pickle("./large_data.pkl")
key_words = search_data.keys()
file_name = SYMBL + str(start_year)[2:] + '-' + str(end_year)[2:]
stock_tick = pd.read_pickle("./pickles/" + file_name + ".pkl")


df_full = search_data['Ethereum']
df = df_full[['Open', 'Ethereum', 'Price_Change']]


#Shift the stocks by up to 10 days. So that hopefully the search results predict the prices

#Open or Price Change?
oop = 'Open'
#oop = 'Price_Change'

df_mod = df
max_shift = 0
shift_start = -30
for i in range(shift_start, max_shift+1):
	temp = df[oop].shift(i)
	temp = temp.to_frame()
	temp = temp.rename(columns = {oop:oop + str(i)})
	df_mod = df_mod.join(temp)

corr = df_mod.corr()

start_slice = oop + str(shift_start)
stop_slice = oop + str(max_shift)
#nums = corr.loc[start_slice:stop_slice, 'Price_Change']
#nums2 = corr.loc[start_slice:stop_slice, 'Open']

#Raise the 
#df_mod = df
ser = df[key_word]
start_p_slice = 3
stop_p_slice = 30
for p in range(start_p_slice, stop_p_slice+1):
	p = p/10
	temp = ser.apply(lambda x: np.sign(x) * np.absolute(x)**p )
	temp = temp.to_frame()
	temp = temp.rename(columns = {key_word:key_word + 'p' + str(int(p*10))})
	df_mod = df_mod.join(temp)

corr = df_mod.corr()

start_p_slice = key_word + 'p' + str(start_p_slice)
stop_p_slice = key_word + 'p' + str(stop_p_slice)
corr2 = corr.loc[start_slice:stop_slice, start_p_slice:stop_p_slice]

max_list = corr2.idxmax()
max_list = max_list.to_frame()
max_list = max_list.reset_index()

lis = []
n = len(max_list) 
max_val = 0
final_shift = ''
final_p = ''
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

file_name = SYMBL + key_word + str(start_year)[2:] + '-' + str(end_year)[2:]

df_graph.to_pickle("./pickles/" + file_name + ".pkl")
