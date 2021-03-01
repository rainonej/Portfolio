import pickle
start_year = 2016
end_year = 2020
kw_list = ['litecoin', 'LTC-USD']
SYMBLs = ['DOGE', 'LTC', 'ETH', 'BTC', 'VET', 'ZRX', 'ADA', 'BNB', 'USDT', 'DOT1', 'DOT2', 'XRP', 'LINK', 'BCH', 'XLM', 'USDC', 'XEM', 'ATOM1', 'SOL2', 'SOL1', 'EOS', 'BSV', 'TRX', 'MIOTA', 'THETA']

def get_obj(symbl):
	"Gives the object from the .pkl file."
	
	path = "pickles/objects/" + symbl + ".pkl"
	file = open(path,'rb')
	obj = pickle.load(file)
	file.close()
	return obj

def get_search_path(term, year):
	return "pickles/" + term + "_searches_" + str(year) + ".pkl"


#SYMBLs = list(map(lambda s: s + '-USD', SYMBLs))
#key_words = ['Dogecoin', 'Ethereum', 'crypto market']
key_words = ['0xproject', 'Cardano', 'Tether', 'Polkadot', 'XRP', 'Litecoin', 'Chainlink', 'BitcoinCash', 'Stellar', 'USDCoin', 'Bitcoin', 'NEM USD', 'Cosmos USD', 'Solana', 'EOS', 'BitcoinSV', 'TRON USD', 'IOTA USD', 'THETA USD', 'BinanceCoin']


#from get_suggestions import new_words

#key_words = new_words(kw_list)
#key_word = key_words[0]