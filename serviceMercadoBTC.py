import requests
from requests import status_codes
from configs import DATA_BASEURL

class Ticker:
    def __init__(self,high = 0,low = 0, vol = 0,last = 0,buy = 0,sell = 0,open_d = 0,date = 0):
        self.high = float(high)
        self.low = float(low)
        self.vol = float(vol)
        self.last = float(last)
        self.buy = float(buy)
        self.sell = float(sell)
        self.open = float(open_d)
        self.date = int(date)

    def __str__(self):
        return f'last = {self.last}, buy = { self.buy}, sell = {self.sell}, open = {self.open}, date = {self.date} '
def getTicker(currency = "BTC",debug = False):
    if(debug):
        print("requesting to "+DATA_BASEURL+currency + "/ticker")
    ret = requests.get(DATA_BASEURL+currency + "/ticker")
    if(ret.status_code != 200):
        print("ERRO: "+ str(ret.status_code))
        return None
    ret = ret.json()['ticker']
    data = Ticker(ret["high"],ret["low"],ret["vol"],ret["last"],ret["buy"],ret["sell"],ret["open"],ret["date"])
    return data
