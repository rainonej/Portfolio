import pytrends as pt
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)


kw_list = ["ETH-USD", "Ethereum"]

def new_words(words):
	pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

	kw_blist = kw_list
	q = pytrends.related_queries() 
	for i in q:
		df = q[i]['top']
		filt = (df['value'] > 50 )
		kw_blist += list(df.loc[filt,'query'])

	kw_blist = list(set(kw_blist))

	return kw_blist