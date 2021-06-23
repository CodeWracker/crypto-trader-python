from configs import TEST_WALLET,TAXA_COMPRA,TAXA_VENDA
import pandas as pd
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
    
    def buy(self,price = 1,rel = 1,currency = "BTC",date = 0):
        if(self.testing_mode):
            val = self.balance.brl.available
            print(val)
            aux = val/price
            print("Comprando " + str(aux) + currency )
            self.balance.brl.available-= val
            if(currency == "BTC"):
                self.balance.btc.available+=val* (1-TAXA_COMPRA/100)/price
            self.history.append([self.balance.brl.available,self.balance.btc.available,currency,date,"compra"])
        else:
            print("Ainda não implementado o modo pra valer")
        return
    
    def sell(self,price = 1,rel = 1,currency = "BTC",date = 0):
        val = 0
        if(self.testing_mode):
            if(currency == "BTC"):
                val = self.balance.btc.available
            print(val)
            print("Vendendo " + str(val) + currency )
            self.balance.btc.available-= val
            self.balance.brl.available+=val* (1- TAXA_VENDA/100)/price
            self.history.append([self.balance.brl.available,self.balance.btc.available,currency,date,"venda"])
            
        else:
            print("Ainda não implementado o modo pra valer")
        return
    
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
    

