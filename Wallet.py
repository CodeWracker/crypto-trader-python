from configs import TEST_WALLET
class CurrencyBalance :
    def __init__(self,available = 0,total = 0,amount_open = 0):
        self.available = available
        self.total = total
        self.amount_open_orders = amount_open

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
    def __init__(self,wallet_data = TEST_WALLET):
        self.balance = Balance(brl=wallet_data["balance"]["brl"],btc=wallet_data["balance"]["btc"],eth=wallet_data["balance"]["eth"])

    def __str__(self):
        string = "Balance:\n    brl: %s,\n    btc: %s,\n    eth: %s"%(self.balance.brl.available,self.balance.btc.available,self.balance.eth.available)
        return string

