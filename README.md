# Crypto Correlations

## Using Google Trends data to predict jumps in the prices of cryptocurrencies

### How strong is the correlation between google searches of last week and the stock price of today?

#### What is the method?

Once the Google trends data is obtained, it is compared to the stock price (and the percent daily change of the stock price) to calculate the correlation. Then we preform two transforms to the google trends data. The first is raising it to the p^th power, where p is a value between (1/4, and 4). The second is shifting the data back between 1 and 30 days. We optimize these values to obtain the strongest correlation to stock price. 



Why Cryptocurrency?
The methods used here easily extend to anything publicly traded such as stock or commodities. However this method works especially well on cryptocurencies for a number of reasons.

1. Cryptocurrencies are usually not reflecting the value of a company or a country. Their value is based solely on the market. This means there are few hidden variables that control the price of the currency.

2. Compared to the stock market, there are relatively few high-volume traders. Assuming that each trade is accompanied by at least 1 google search, there is a higher 'google-search-to-money-traded' ratio for cryptocurrencies than for normal stocks. 

3. Cryptocurrencies day-traders engage in cult-like behavior. They discuss their trades freely and air the feelings for the market in several internet communities. When 

