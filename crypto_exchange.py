from binance import Client
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('BINANCE_KEY')
api_secret = os.getenv('BINANCE_SECRET')
print('api_key', api_key)
print('api_secret', api_secret)

client = Client(api_key=api_key, api_secret=api_secret)

def select_exchange(data):
    if 'prefix' in data:
        prefix =  data['prefix']

        if prefix in ["BINANCE", "binance", "Binance"]:
            binance_exchange(data)
        elif prefix in ["OKX", "Okx", "okx"]:
            binance_exchange(data)

def binance_exchange(data):
    get_account_balance()

    basecurrency = ''
    currency = ''

    if 'basecurrency' in data:
        basecurrency =  data['basecurrency']
        print('basecurrency = ', basecurrency)

    if 'currency' in data:
        currency =  data['currency']
        print('currency = ', currency)

    if basecurrency and currency:
        name = basecurrency + currency
        trade_fee = client.get_trade_fee(symbol=name)
        print('Trade Fee = ', trade_fee)
    else:
        print('缺少必要的貨幣資訊')

def get_account_balance():
    account_balance = client.futures_account_balance()

    for balance in account_balance['balances']:
        if float(balance['free']) > 0:
            print(balance['asset'], balance['free'])