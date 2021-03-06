import pytrends as pt
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)


kw_list = ["ETH-USD", "Ethereum"]

def new_words(words):
	# input words: [str1, str2, ...]	
	pytrends.build_payload(words, cat=0, timeframe='today 5-y', geo='', gprop='')

	kw_blist = words
	q = pytrends.related_queries() 
	#print(q)
	for i in q:
		df = q[i]['top']
		#print(df.info())
		filt = (df['value'] > 50 )
		kw_blist += list(df.loc[filt,'query'])

	kw_blist = list(set(kw_blist))

	return kw_blist