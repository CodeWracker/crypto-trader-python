import pandas as pd
import numpy as np
from serviceMercadoBTC import Ticker
from Wallet import Wallet
last_price = 0
def agent(ticker: Ticker, wallet: Wallet):
    global last_price
    if(last_price == 0):
        last_price = ticker.last
        return [ 2, wallet.balance.brl.available/ticker.high]
    last_price = ticker.last
    relacao = 100*ticker.last/last_price - 100
    print(relacao)
    if(relacao >= 1):
        print(myWallet)
        return [ 1, wallet.balance.btc.available]
    else:
        if(relacao<= -0.5):
            print(myWallet)
            return [ 0, wallet.balance.brl.available/ticker.high]
            
        else:
            return [ 2, wallet.balance.brl.available/ticker.high]
    

