from configs import *
from serviceMercadoBTC import getTicker

from Wallet import Wallet
from pprint import pprint


last_price = 0

def operation_handler(opt,price):
    global last_price
    print(opt)
    last_price = price
def main():
    isTesting = input("voce deseja usar a carteira de testes e simular as taxas? S/N  ")
    if(isTesting == "S" or isTesting == "s"):
        isTesting = True
    else:
        isTesting = False
    
    myWallet = Wallet()
    if(not isTesting):
        myWallet("Sei la ainda não fiz kkkk, tem que pegar os dados antes")
    print()
    print(myWallet)
    print()
    
    time = 0
    global last_price
    while True:
        ticker = getTicker("BTC")
        if(ticker is None):
            continue
        if(ticker.date - time >= 10):
            time = ticker.date
            print()
            print(ticker)
            if(last_price == 0):
                last_price = ticker.last
                continue
            
            relacao = 100*ticker.last/last_price - 100
            print(relacao)
            if(relacao >= 1):
                operation_handler("Vender",ticker.last)
            else:
                if(relacao<= -0.5):
                    operation_handler("Comprar",ticker.last)
                else:
                    print("Hold")
if __name__ == "__main__":
    main()