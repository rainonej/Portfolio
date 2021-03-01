import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_pickle("pickles/LTC-USD_price_2018.pkl")
df2 = pd.read_pickle("pickles/Litecoin_searches_2018.pkl")
#df2 = df1.rename(columns = {'Open':'Litecoin'})
#df3 = pd.read_pickle("pickles/LTC USD_searches_2018.pkl")
df3 = pd.concat([df1, df2], axis = 1)
df = df3.loc['2018-01-07':'2018-12-31', ['Open', 'Litecoin']]

p=7

def split_data(df, percent = .8):
	"Given a dataframe it splits the data into two unequal parts."
	size = df.shape[0]
	split = int(size*percent) 
	split0 = df.index[split]
	split1 = df.index[split+1]
	df_train = df.loc[:split0, :]
	df_test = df.loc[split1:, :]
	return(df_train, df_test)

(df_train,df_test) = split_data(df)

import statsmodels
from statsmodels.tsa.api import VAR

def create_VARp_model(df_train, p, verbose = False):
	"Given the training data, it returns the model. The model then inputs the test data and outputs a forecast. The forecast is then tested against the test data."
	"We will ignore differencing for now."

	#Operates on the differenced data
	df_differenced = df_train.diff().dropna()

	model = VAR(df_differenced)
	'''
	maxlags = 12
	for i in range(1, maxlags+1):
		result = model.fit(i)
		print('Lag Order =', i)
		print('AIC : ', result.aic)
		print('BIC : ', result.bic)
		print('FPE : ', result.fpe)
		print('HQIC: ', result.hqic, '\n')
	x = model.select_order(maxlags=12)
	print(x.summary())
	return x
	'''
	model_fitted = model.fit(p)
	if verbose: print(model_fitted.summary())

	def model(df_observations):
		"predicts tomorrows change in stock price"
		#print(df_observations)
		df_observations = df_observations.diff().dropna()
		#print(df_observations)
		inputs = df_observations.values[-p:]
		return model_fitted.forecast(inputs, steps = 1)
		
	return model


	#return model_fitted



model = create_VARp_model(df_train,p, verbose = False)

#lag_order = model_fitted.k_ar
#print(lag_order)  #> 4

a = model(df_train)

def get_predictions(model, p, df_observations):
	"input the model function and the df_observations, including the last p days of the training data. Output a dataframe of the predictions (differenced)."

	output = df_observations.drop(df_observations.index[:p+1])
	n = len(output)
	for i in range(n):
		inputs = df_observations.loc[df_observations.index[i:p+i+1], :]
		#print(inputs)
		#print(list(model(inputs)))
		#print(output.loc[output.index[i], :])
		output.loc[output.index[i], :] = model(inputs)
		#print(output)
	return output
	
df_predict =  get_predictions(model, p, df_test)
print(df_predict)

def get_profits(df_predict, df_test, mean_investment = 100, max_investment = float('inf'), long_only = False):
	"returns the profits as a function of time"

	def ceiling(num):
		if (abs(num)> max_investment):
			return np.sign(num) * max_investment
		else:
			return num

	def floor(num):
		if num<0: 
			return 0
		else:
			return num

	df_obs = df_test.diff().dropna()
	mean = df_predict['Open'].apply(abs).mean()
	#print(df_predict)
	df_invest = df_predict['Open'].apply(lambda x: x * mean_investment / mean)
	print(df_invest)
	df_invest = df_invest.apply(ceiling)
	if long_only: df_invest = df_invest.apply(floor)
	df_profit = df_invest * df_obs['Open']
	df_profit = df_profit.cumsum()
	return df_profit

df_profit = get_profits(df_predict, df_test, long_only = True)
print(df_profit)
df_profit.plot()
plt.show()


#a = model_fitted.forecast(df_train.values[-8:], steps = 10)

'''
import inspect

for i in inspect.getmembers(model_fitted):
    # Ignores anything starting with underscore 
    # (that is, private and protected attributes)
    if not i[0].startswith('_'):
        # Ignores methods
        if inspect.ismethod(i[1]):
            print(i)
'''
#print(model_fitted.forecast(df_train.values[-3:], 100))
#model_fitted.plot_forecast(100)
#plt.show()