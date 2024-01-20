from binance import Client
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('BINANCE_KEY')
api_secret = os.getenv('BINANCE_SECRET')
client = Client(api_key=api_key, api_secret=api_secret)

def select_exchange(data):
    if 'basecurrency' in data:
        basecurrency =  data['basecurrency']

        if basecurrency in ["BINANCE", "binance", "Binance"]:
            binance_exchange(data)
        elif basecurrency in ["OKX", "Okx", "okx"]:
            binance_exchange(data)

def binance_exchange(data):
    status = client.get_account_status()
    print('Account Status = ', status)

# def okx_exchange(data):
#     return True