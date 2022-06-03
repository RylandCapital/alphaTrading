import os
import ccxt   

import numpy as np
 
from scipy import stats
from dotenv import load_dotenv

load_dotenv()

#env vars
KUCOIN_FUTURES_KEY = os.getenv("KUCOIN_FUTURES_KEY")
KUCOIN_FUTURES_SCRT = os.getenv("KUCOIN_FUTURES_SCRT")
KUCOIN_SPOT_KEY = os.getenv("KUCOIN_SPOT_KEY")
KUCOIN_SPOT_SCRT = os.getenv("KUCOIN_SPOT_SCRT")

#define any apis to be used
kucoin_futures = ccxt.kucoinfutures({
    'apiKey': KUCOIN_FUTURES_KEY,
    'secret': KUCOIN_FUTURES_SCRT,
})
kucoin_futures_markets = kucoin_futures.load_markets()

kucoin = ccxt.kucoin({
    'apiKey': KUCOIN_SPOT_KEY,
    'secret': KUCOIN_SPOT_SCRT,
})
kucoin_markets = kucoin.load_markets()
