import pandas as pd
import numpy as np
from key_words import start_year, end_year, key_words

large_data = pd.read_pickle("./large_data.pkl")

'''
df_full = pd.read_pickle("./df_full.pkl")
df = df_full[[key_word, 'Open', 'Price_Change']]

df_shifts = df
max_shift = 30
shift_start = -10
for i in range(shift_start, max_shift+1):
	trends = df[key_word].shift(i)
	trends = trends.to_frame()
	trends = trends.rename(columns = {key_word:key_word + str(i)})
	df_shifts = df_shifts.join(trends)

corr = df_shifts.corr()

start_slice = key_word + str(shift_start)
stop_slice = key_word + str(max_shift)
nums = corr.loc[start_slice:stop_slice, 'Price_Change']
nums2 = corr.loc[start_slice:stop_slice, 'Open']

#df_shifts = df
ser = df.Price_Change
start_p_slice = 5
stop_p_slice = 30
for p in range(start_p_slice, stop_p_slice+1):
	p = p/10
	temp = ser.apply(lambda x: np.sign(x) * np.absolute(x)**p )
	temp = temp.to_frame()
	temp = temp.rename(columns = {'Price_Change':'Price_Change' + 'p' + str(int(p*10))})
	df_shifts = df_shifts.join(temp)

corr = df_shifts.corr()

start_p_slice = 'Price_Change' + 'p' + str(start_p_slice)
stop_p_slice = 'Price_Change' + 'p' + str(stop_p_slice)
corr2 = corr.loc[start_slice:stop_slice, start_p_slice:stop_p_slice]

corr2.idxmax()
'''