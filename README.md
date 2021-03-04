# Stock Correlation Project
https://cryptic-badlands-45250.herokuapp.com/

## How strong is the correlation between the Google searches of last week and the stock prices of today?

### Elevator Pitch
Create a website where day traders can test whether their knowledge of industry "chatter" can reliably be leveraged into profit. "Chatter" is a measure of public interest in a stock or cryptocurrency. Day traders are interested in knowing when and what type of "chatter" drives markets versus reacting to markets. The website will display this information in a clear way using multiple visualizations. Currently "chatter" is measured by daily Google searched for specific key words, but will incorporate metrics from Twitter, News articles, and Subreddits. 

### Who are the End Users?
Any private person who is buying and selling stocks or cryptocurrencies on the daily to several-months time-scale. Day traders who have specific knowledge of the industry they are trading in (meaning, they know the terminology) will find this tool especially useful because it can quantify the feeling of "excitement" a particular industry feels about company/stock/cryptocurrency/etc... 

### How will success be measured?
Users who are interested in using a tool like this will likely be measuring its utility to them in terms of increased profit and reduced risk. If users were to pay for this service, then their investments would be recorded and compared against a simulated similar investment strategy which doesn't use "chatter".

### Details about the Current Version
Users enter a Stock or Cryptocurrency Symbol, a search term, a time frame. 3 graphs are then displayed. 
1. The first is a bar chart showing the correlation between stock prices of day T and google searches on day T-5, T-4, ..., T+4, T+5. If the correlation factor is higher on the left side of the chart than the right, that means that "chatter" predicts/drives the market rather than reacting to it. 
2. The second graph shows the stock price and the google searches on the same timescale. The y-axis are adjusted are adjusted to make it easier to read. This allows users to see where the correlation is coming from. Is it because the two graphs move together? Or is it because the value of the stock doesn't change and there are approximately 0 searches per day for the selected search word.
3. The third graph shows the profits over time if one were to invest every day in this stock based on market predictions using both chatter and stock prices versus using just stock prices. Both models are Autoregression models using training data from the previous 6 months. Even if the model is accurate, the investment strategy is not meant to be a realistic one. It is only meant to show if profits can be increased using this additional "chatter" information.

### Future Developments
As of now, the framework is already in place (things are on Github, but not Heroku) to add an option for multiple search terms and to investigate non-linear correlations between the search terms and stock price. Beyond this, I hope to include other sources of "chatter", specifically the number of distinct "Twitter Threads" and a Sentiment Analysis of comments in subreddits related to the stock. 

### Why the emphasis on Cryptocurrency?
The methods used here easily extend to anything publicly traded such as stock or commodities. However this method works especially well on cryptocurrencies for a number of reasons.

1. Cryptocurrencies are usually not reflecting the value of a company or a country. Their value is based solely on the market. This means there are few hidden variables that control the price of the currency.

2. Compared to the stock market, there are relatively few high-volume traders. Assuming that each trade is accompanied by at least 1 google search, there is a higher 'Google-search-to-money-traded' ratio for cryptocurrencies than for normal stocks. 

3. Cryptocurrencies day-traders engage in cult-like behavior. They discuss their trades freely and air their feelings for the market in several internet communities.  

### Similarities to Existing Projects
Several research papers (http://www.ccom.ucsd.edu/~cdeotte/papers/GoogleTrends.pdf) have been written on using the google trends, twitter, reddit, news articles, etc... to predict the market. Some investment firms most likely have developed their own algorithms which take into account "chatter". However, as far as I'm aware, there are no tools like this that are available to private day traders. This is why the emphasis of my project is on conveying the information in a concise visual manor, as opposed to a more dense though possibly more comprehensive technical read-out.  
