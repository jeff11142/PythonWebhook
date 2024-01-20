from binance import Client
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('BINANCE_KEY')
api_secret = os.getenv('BINANCE_SECRET')
print('api_key', api_key)
print('api_secret', api_secret)

client = Client(api_key=api_key, api_secret=api_secret)
trade_fee = client.get_trade_fee(symbol='BTCUSDT')
print('Trade Fee = ', trade_fee)

def select_exchange(data):
    if 'basecurrency' in data:
        basecurrency =  data['basecurrency']

        if basecurrency in ["BINANCE", "binance", "Binance"]:
            binance_exchange(data)
        elif basecurrency in ["OKX", "Okx", "okx"]:
            binance_exchange(data)

def binance_exchange(data):
    status = client.get_account()
    print('Account Status = ', status)
    return status

# def okx_exchange(data):
#     return True