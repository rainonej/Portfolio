import pandas as pd
import matplotlib.pyplot as plt


SYMBL = 'ETH-USD'
start_year = 2017
end_year = 2021
key_word = 'Ethereum'
file_name =  SYMBL + key_word + str(start_year)[2:] + '-' + str(end_year)[2:]

df = pd.read_pickle("./pickles/" + file_name + ".pkl")


plt.figure()
df.Ethereump3.plot(label = 'testefwef')
temp = 'Open-25'
#ax.set_ylabel('Google Searches')

df['Open'].plot(secondary_y=True, style='g')
'''
df.
ax = df.plot(secondary_y = ['Ethereum'])
ax.set_ylabel('Google Searches')
ax.right_ax.set_ylabel('Stock Price')
df.plot()
'''
#plt.savefig('foo.png')
plt.show()
