import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
df = pd.DataFrame(np.random.randn(5, 4), columns=['A', 'B', 'C', 'D'])
#plt.close("all")


plt.figure()

ax = df.plot(secondary_y = ['A', 'B'])
ax.set_ylabel('C scale')
ax.right_ax.set_ylabel('AB scale')
plt.show()


'''
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
'''