import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#from get_unmodified_graph import graph_df

'''
fig = plt.figure()
gs = fig.add_gridspec(2, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
# spans two rows:
ax3 = fig.add_subplot(gs[:, 1])

ax1.plot(np.random.rand(20))
ax2.plot(np.random.rand(50))
ax3.plot(range(10))
plt.show()
'''
SYMBL = 'LTC-USD'
KEY_WORD = 'litecoin'
START_DATE = '2017-06-01'
END_DATE = '2018-06-05'
WIN_SIZE = 1

#Getting the right Data Frames
start_year = START_DATE[:4]
end_year = END_DATE[:4]

price_df = pd.DataFrame({})
searches_df = pd.DataFrame({})

print('starting the loop')
import time
timeout = time.time() + 10  # 5 minutes from now
test = 0
while True:
    test += 1
    if time.time() > timeout:
        break
print('That took ', test, ' steps!')

'''
for year in range(int(start_year), int(end_year)+1):
	price_file = "pickles/" + SYMBL + "_price_" + str(year) + ".pkl"
	search_file = "pickles/" + KEY_WORD + "_searches_" + str(year) + ".pkl"
	price_df = pd.concat([price_df, pd.read_pickle(price_file)])
	searches_df = pd.concat([searches_df, pd.read_pickle(search_file)])

price_df = price_df.loc[START_DATE:END_DATE]
searches_df = searches_df.loc[START_DATE:END_DATE]

labels = list(map(str, price_df.index))
labels = ['a', 'b', 'c', 'd', 'e']
print(labels)

df = price_df['Open']
#pd.plotting.lag_plot(df)
pd.plotting.autocorrelation_plot(df)
plt.show()
'''
'''
fig = plt.figure(figsize = (5,5)) #Instantiate the Figure
gs = fig.add_gridspec(1, 1) #Choose the grid size for the number of graphs

#ax = fig.add_axes(list(price_df["Open"]))
ax = fig.add_axes([0,0,1,1])
ax.bar(labels, price_df["Open"])
#ax1 = fig.add_subplot(gs[0, 0])
#ax1.plot(graph_df["Open"], color = color1)

plt.show()
'''