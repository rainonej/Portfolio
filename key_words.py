
start_year = 2016
end_year = 2020
kw_list = ['litecoin', 'LTC-USD']
SYMBLs = ['DOGE', 'LTC', 'ETH', 'BTC', 'VET', 'ZRX', 'ADA', 'BNB', 'USDT', 'DOT1', 'DOT2', 'XRP', 'LINK', 'BCH', 'XLM', 'USDC', 'XEM', 'ATOM1', 'SOL2', 'SOL1', 'EOS', 'BSV', 'TRX', 'MIOTA', 'THETA']
SYMBLs = list(map(lambda s: s + '-USD', SYMBLs))
#key_words = ['Dogecoin', 'Ethereum', 'crypto market']
key_words = ['Cat', 'Pasta']


from get_suggestions import new_words

#key_words = new_words(kw_list)
#key_word = key_words[0]