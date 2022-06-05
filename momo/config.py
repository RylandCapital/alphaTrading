import os
import ccxt   

import numpy as np
 
from scipy import stats
from dotenv import load_dotenv

load_dotenv()

#env vars you must have if using kucoin
KUCOIN_FUTURES_KEY = os.getenv("KUCOIN_FUTURES_KEY")
KUCOIN_FUTURES_SCRT = os.getenv("KUCOIN_FUTURES_SCRT")
KUCOIN_FUTURES_PASSWORD = os.getenv("KUCOIN_FUTURES_PASSWORD")
KUCOIN_SPOT_KEY = os.getenv("KUCOIN_SPOT_KEY")
KUCOIN_SPOT_SCRT = os.getenv("KUCOIN_SPOT_SCRT")
KUCOIN_SPOT_PASSWORD = os.getenv("KUCOIN_SPOT_PASSWORD")

#define any apis to be used
kucoin_futures = ccxt.kucoinfutures({
    'apiKey': KUCOIN_FUTURES_KEY,
    'secret': KUCOIN_FUTURES_SCRT,
    'password': KUCOIN_FUTURES_PASSWORD
})
kucoin_futures_markets = kucoin_futures.load_markets()

kucoin = ccxt.kucoin({
    'apiKey': KUCOIN_SPOT_KEY,
    'secret': KUCOIN_SPOT_SCRT,
    'password': KUCOIN_SPOT_PASSWORD
})
kucoin_markets = kucoin.load_markets()

#define your universe (tickers)
universe = [i.split(':')[0] for i in list(kucoin_futures_markets.keys())]

#define chosen momentum formula , volatility formulas, portfolio inputs
momentum_window = 90
minimum_momentum = -100
portfolio_size = 10

def volatility(ts, window=20):
    return ts.pct_change().rolling(window).std().iloc[-1]

def momentum_score(ts):
    """
    Input:  Price time series.
    Output: Annualized exponential regression slope, 
            multiplied by the R2
    """
    # Make a list of consecutive numbers
    x = np.arange(len(ts)) 
    # Get logs
    log_ts = np.log(ts) 
    # Calculate regression values
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, log_ts)
    # Annualize percent
    annualized_slope = (np.power(np.exp(slope), 252) - 1) * 100
    #Adjust for fitness
    score = annualized_slope * (r_value ** 2)
    return score
