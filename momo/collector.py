import pandas as pd
import datetime as dt
import time

import momo.config as config

def ohlc():
    errors = []
    dfs = []
    for c in config.universe:
        try:
            data = pd.DataFrame(

                config.kucoin.fetch_ohlcv(c,'1d'),
                columns=['date', 'open', 'high', 'low', 'close', 'volume']
                
                )
            
            data['date'] = data['date'].apply(
                lambda x: dt.datetime.utcfromtimestamp(x / 1000)
                )
            
            data['symbol'] = c
            data['num_observations'] = len(data)
            data = data.set_index('date')

            if len(data)>config.momentum_window:
                dfs.append(data.iloc[:config.momentum_window])
        
        except:
            print('Symbol: {0} was not collected, check api symbols offered'.format(c))
            errors.append(c)

    print('{0} successfully collected, {1} assets were removed'.format(len(dfs), len(errors)))
    return {
        'data': pd.concat(dfs), 
        'not_included': errors
        }

# returns information on status of the account to be traded (kukcoin futures for us)
def account_report():

    #pull futures account info and position status
    futures = pd.DataFrame(config.kucoin_futures.fetch_balance()['info'])[['data']]
    futures_positions = pd.DataFrame(config.kucoin_futures.fetch_positions())

    return {
            'value': futures.loc['accountEquity'],
            'available_balance': futures.loc['availableBalance'],
            'position_margin': futures.loc['positionMargin'],
            'unrealised_pnl': futures.loc['unrealisedPNL'],
            'positions':futures_positions
    }







