import numpy as np
import matplotlib.pyplot as plt

from get_unmodified_graph import graph_df

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



'''

fig = plt.figure(figsize = (10, 5))
ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(3, 9 , (1,9))
#ax = plt.subplots()
print(type(fig))
print(type(ax1))

ax1.plot(np.random.rand(20))
ax2.plot(np.random.rand(50))
plt.show()
'''


'''
fig, ax = plt.subplots()
ax.plot(np.random.rand(20))
ax.set_title('test title')
plt.show()
'''


'''
n_rows = 2
n_cols = 2
fig, axes = plt.subplots(n_rows, n_cols)
for row_num in range(n_rows):
    for col_num in range(n_cols):
        ax = axes[row_num][col_num]
        ax.plot(np.random.rand(20))
        ax.set_title(f'Plot ({row_num+1}, {col_num+1})')
fig.suptitle('Main title')
fig.tight_layout()
plt.show()
'''