# Crypto Correlations

## How strong is the correlation between the Google searches of last week and the stock prices of today?

### Goal/Deliverables
Users will be able to enter a cryptocurrency symbl and optional search words. The program will then suggest additional search words. A graph will be displayed relating the price of the cryptocurrency and each search word, along with displaying a calculated correlation factor. The program will also calculate the expected number of days that spikes in Google search results for these search words will effect the market.

### Method
Use API's to obtain Google Trends data and cryptocurrency price data. We preform a phaseshift on the cryptocurrency price data (shifting it by a number of days between 1 and 30). We also preform a non-linear transformation on the Google Trends data (we raise the number of results to the power of p, where p is between .25 and 4.0). 
The value of the phaseshift and the p-power are optimized to maximize the correlation. We don't have to worry about over-fitting the data since we are reducing an object that has hundreds of dimensions by only two.  

### Why Cryptocurrency?
The methods used here easily extend to anything publicly traded such as stock or commodities. However this method works especially well on cryptocurencies for a number of reasons.

1. Cryptocurrencies are usually not reflecting the value of a company or a country. Their value is based solely on the market. This means there are few hidden variables that control the price of the currency.

2. Compared to the stock market, there are relatively few high-volume traders. Assuming that each trade is accompanied by at least 1 google search, there is a higher 'Google-search-to-money-traded' ratio for cryptocurrencies than for normal stocks. 

3. Cryptocurrencies day-traders engage in cult-like behavior. They discuss their trades freely and air their feelings for the market in several internet communities.  

