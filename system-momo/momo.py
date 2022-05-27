import time
import os
import ccxt   
 
import pandas as pd 
from dotenv import load_dotenv

load_dotenv()

KUCOIN_FUTURES_KEY = os.getenv("KUCOIN_FUTURES_KEY")
KUCOIN_FUTURES_SCRT = os.getenv("KUCOIN_FUTURES_SCRT")

kucoin = ccxt.kucoin({
    'apiKey': KUCOIN_FUTURES_KEY,
    'secret': KUCOIN_FUTURES_SCRT,
})


