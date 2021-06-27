from configs import TEST_WALLET,TAXA_COMPRA,TAXA_VENDA
import pandas as pd
import numpy as np
class CurrencyBalance :
    def __init__(self,available = 0,total = 0,amount_open = 0):
        self.available = float(available)
        self.total = float(total)
        self.amount_open_orders = int(amount_open)

class Balance: 
    def __init__(self,brl,btc,eth):
        self.brl =  CurrencyBalance(available = brl["available"],total = brl["total"])
        self.btc =  CurrencyBalance(available = btc["available"],total = btc["total"], amount_open= btc["amount_open_orders"])
        self.eth =  CurrencyBalance(available = eth["available"],total = eth["total"], amount_open= eth["amount_open_orders"])
  
'''
  withdrawal_limits?: {
    bch?: CurrencyBalance;
    brl?: CurrencyBalance;
    btc?: CurrencyBalance;
    eth?: CurrencyBalance;
    ltc?: CurrencyBalance;
    xrp?: CurrencyBalance;
  };
'''
class Wallet:
    def __init__(self,wallet_data = TEST_WALLET,testing = True):
        self.balance = Balance(brl=wallet_data["balance"]["brl"],btc=wallet_data["balance"]["btc"],eth=wallet_data["balance"]["eth"])
        self.testing_mode = testing
        self.history = []
    def __str__(self):
        string = "Balance:\n    brl: %s,\n    btc: %s,\n    eth: %s"%(self.balance.brl.available,self.balance.btc.available,self.balance.eth.available)
        return string

    def execute_operation(self, operation = 0,qtd = 1,currency = "BTC",date = 0,price = 1):
        operations = [self.buy,self.sell,self.hold]
        operations[operation](qtd,currency,date,price)

    def buy(self,qtd = 1,currency = "BTC",date = 0,price = 1):
        if(self.testing_mode):
            print("Comprando " + str(qtd) + currency + " por " + str(qtd * price) )
            self.balance.brl.available-= qtd * price
            if(currency == "BTC"):
                self.balance.btc.available+= qtd* (1-TAXA_COMPRA/100)
            self.history.append([self.balance.brl.available,self.balance.btc.available,currency,date,"compra"])
        else:
            print("Ainda não implementado o modo pra valer")
        return
    
    def sell(self,qtd = 00.1,currency = "BTC",date = 0,price = 1):
        if(self.testing_mode):
            print("Vendendo " + str(qtd) + currency + " por " + str(qtd * price) )
            self.balance.btc.available-= qtd
            self.balance.brl.available+=qtd* (1- TAXA_VENDA/100)*price
            self.history.append([self.balance.brl.available,self.balance.btc.available,currency,date,"venda"])
            
        else:
            print("Ainda não implementado o modo pra valer")
        return
    def hold(self,operation = 0,qtd = 1,currency = "BTC",date = 0,price = 1):
        print("Hold")
    
    def save(self):
        brl = []
        cash = []
        currency = []
        data = []
        op = []
        for tr in self.history:
            brl.append(tr[0])
            cash.append(tr[1])
            currency.append(tr[2])
            data.append(tr[3])
            op.append(tr[4])
        df = pd.DataFrame()
        df["Saldo BRL"] = brl
        df["Saldo Coin"] = cash
        df["Moeda"] = currency
        df["Timestamp"] = data
        df["Operação"] = op
        df.to_csv("transacoes.csv")
    

