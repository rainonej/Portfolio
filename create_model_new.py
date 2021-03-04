import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from key_words import get_obj

#df1 = pd.read_pickle("pickles/LTC-USD_price_2019.pkl")
#df2 = pd.read_pickle("pickles/Litecoin_searches_2019.pkl")
#df2 = df1.rename(columns = {'Open':'Litecoin'})
#df3 = pd.read_pickle("pickles/LTC USD_searches_2018.pkl")
#df3 = pd.concat([df1, df2], axis = 1)
#df = df3.loc['2019-01-07':'2019-12-31', ['Open', 'Litecoin']]

p=7
a = get_obj('DOGE')
start_date = '2017-08-07'
end_date = '2020-01-31'
def get_data(obj, search_terms, start_date, end_date):
	"returns the df file"

	df = obj.get_price_df(start_date, end_date)

	for term in search_terms:
		df = pd.concat([df, obj.get_search_df(start_date, end_date, term, outside = True)], axis = 1)
	print(df)
	return(df)

df = get_data(a,['Litecoin'], start_date, end_date )
df = df.drop_duplicates()
df = df.dropna()

def split_data(df, percent = .8):
	"Given a dataframe it splits the data into two unequal parts."

	df[df.columns[1]] = df['Open'] #To get rid of the dependence of the search term

	size = df.shape[0]
	split = int(size*percent) 
	split0 = df.index[split]
	split1 = df.index[split+1]
	df_train = df.loc[:split0, :]
	df_test = df.loc[split1:, :]
	return(df_train, df_test)

(df_train,df_test) = split_data(df, percent = .2)

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
		#print('Orignal inputs are')
		#print(df_observations)
		df_observations = df_observations.diff().dropna()
		#print(df_observations)
		inputs = df_observations.values[-p:]
		#print('inputs are = ')
		#print(inputs)
		return model_fitted.forecast(inputs, steps = 1)
		
	return model


	#return model_fitted



model = create_VARp_model(df_train, p, verbose = False)

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
		#return inputs
		#print('we got stuck on model(inputs)')
		temp = model(inputs)
		#print('we got stucj on output.loc[output.index[i], :] = temp ')
		output.loc[output.index[i], :] = temp
		#print('info for model(inputs) =', model(inputs))
		#print('info for output =', output.info())
		#print(output)
		#if (i == 5): break
	return output

original_inputs = df_test.loc[df_test.index[0:p+0+1], :]
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

	df_price = df_test['Open']

	df_obs = df_test.diff().dropna()
	mean = df_predict['Open'].apply(abs).mean()
	print('means =', mean)
	#print(df_predict)
	df_invest = df_predict['Open']
	df_invest = df_invest.to_frame()
	df_invest = df_invest.div(df_price, axis = 0)
	df_invest = df_invest['Open']
	i = 0
	while ((df_invest.apply(abs).mean() / mean_investment) < .9) or ((df_invest.apply(abs).mean() / mean_investment) > 1.1):
		#keep applying the mean thing until it works, or until the time runs out
		i += 1
		if i > 10:
			break
		mean = df_invest.apply(abs).mean()
		df_invest = df_invest.apply(lambda x: x * mean_investment / mean)

	new_mean = df_invest.apply(abs).mean()
	print('the new mean is =', new_mean)
	print(df_invest)
	df_invest = df_invest.apply(ceiling)
	if long_only: df_invest = df_invest.apply(floor)
	
	a = df_obs['Open'].to_frame()
	b = df_invest.to_frame()
	print('Actual obeservations', a)
	print('Investments', b)
	df_profit = df_invest * df_obs['Open'] 
	df_profit = df_profit.div(df_price, axis=0)
	c = df_profit
	print('Daily profits', c)
	df_profit = df_profit.cumsum()
	return (a,b,c,df_profit)

(daily_changes, daily_investments, daily_profit, df_profit) = get_profits(df_predict, df_test, long_only = False, max_investment = 500)
print(df_profit)
#df_profit.plot()
#plt.show()


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
