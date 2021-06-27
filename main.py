from configs import *
from serviceMercadoBTC import getTicker

from Wallet import Wallet
from pprint import pprint
from agent import agent



def main():
    isTesting = input("voce deseja usar a carteira de testes e simular as taxas? S/N  ")
    if(isTesting == "S" or isTesting == "s"):
        isTesting = True
    else:
        isTesting = False
    
    myWallet = Wallet()
    if(not isTesting):
        myWallet("Sei la ainda não fiz kkkk, tem que pegar os dados antes",testing = False)
    print()
    print(myWallet)
    print()
    
    time = 0
    
    
    while True:
        ticker = getTicker("BTC") # coloque como segundo parametro True, caso queria ver o endereço que esta sendo chamado
        if(ticker is None):
            continue
        if(ticker.date - time >= 10):
            time = ticker.date
            print()
            print(ticker)
            
            
            decision = agent(ticker, myWallet)
            myWallet.execute_operation(operation = decision[0],qtd = decision[1], date = ticker.date,price= ticker.last)

        myWallet.save()
if __name__ == "__main__":
    main()