# crypto-trader-python

A python script to trade cryptocurrency

# How to start this

if you don't have pipenv installed, istall it with `pip install pipenv`

- Create a `configs.py` file and follow the instructions here, and in the `configs.example.py` file to fill up the variables
- `pipenv shell`
- `pipenv install`
- `python main.py`

## Configurations secrets

### TAPI_ID

I don't remember where to get it now, but when I start to use it I will put it here

### TAPI_SECRET

Same as the above

### TAXA_COMPRA and TAXA_VENDA

those are the tax percentage you pay for the type of transaction

### TEST_WALLET

Is a fake wallet with a amount of money to start trading on test mode

# My Next goals

- Build a Neural Network to select the operation (BUY,SELL or HOLD)
- Select by a genetic algorithm the best neural net to operate in the simulation
- See how this Net goes in time
- Give it my real money
- Be happy (I guess)
