from crypto_class import Crypto
import pickle
from key_words import SYMBLs


#symbl_list = ['DOGE', 'LTC', 'ETH', 'BTC', 'VET', 'ZRX', 'ADA', 'BNB', 'USDT', 'DOT1', 'DOT2', 'XRP', 'LINK', 'BCH', 'XLM', 'USDC', 'XEM', 'ATOM1', 'SOL2', 'SOL1', 'EOS', 'BSV', 'TRX', 'MIOTA', 'THETA']

Cryptos = {}

for symbl in SYMBLs:
	Cryptos[symbl] = Crypto(symbl)
	pickle.dump(Cryptos[symbl], open(Cryptos[symbl].path, "wb"))

Cryptos['DOGE'].add_search_terms(['dogecoin stock', 'dogecoin price'])


#Cryptos = {}
#pickle.dump(symbl_list, open("pickles/objects/test.pkl", "wb"))
#['Cardano', 'Tether', 'Polkadot', 'XRP', 'Litecoin', 'Chainlink', 'BitcoinCash', 'Stellar', 'USDCoin', 'Bitcoin', 'NEM USD', 'Cosmos USD', 'Solana', 'EOS', 'BitcoinSV', 'TRON USD', 'IOTA USD', 'THETA USD', 'BinanceCoin']

#doge = Crypto('DOGE', name = 'Dogecoin', search_terms = ['Dogecoin', 'dogecoin stock', 'dogecoin price'])
#lite = Crypto('LTC', name = 'Litecoin', search_terms = ['Litecoin'])
#eth = Crypto('ETH', name = 'Litecoin', search_terms = ['Ethereum', 'ETH-USD', 'ethereum price'])
#bit = Crypto('BTC', name = 'Bitcoin')
#veChain = Crypto('VET')
#zer0X = Crypto('ZRX', name = '0x')
#cardano = Crypto('ADA')
#bnb = Crypto('BNB')
#usdt = Crypto('USDT')

#Generate objects
#for symbl in symbl_list:
#	Cryptos[symbl] = Crypto(symbl)

#Suppliment objects