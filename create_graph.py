import pandas as pd
import matplotlib.pyplot as plt
from key_words import SYMBL, start_year, end_year, key_word

#SYMBL = 'ETH-USD'
#start_year = 2017
#end_year = 2021
#key_word = 'Ethereum'

file_name =  SYMBL + key_word + str(start_year)[2:] + '-' + str(end_year)[2:]

df = pd.read_pickle("./pickles/" + file_name + ".pkl")

searches = df.keys()[0]
stock_shift = df.keys()[1]

df = df.rename(columns = {searches: key_word, stock_shift: 'Shifted Stock Price', 'Open': 'Stock Price'})
searches = key_word
stock_shift = 'Shifted Stock Price'
plt.figure()
df[searches].plot(legend = True, ylabel = 'Google Searches')
#temp = 'Open-25'
#ax.set_ylabel('Google Searches')

df[stock_shift].plot(secondary_y=True, style='g', legend = True)
#df.plot(secondary_y=True, style='g')


file_name = SYMBL + '.png'
#file_name = 'test.png'
plt.savefig(file_name)
plt.show()
