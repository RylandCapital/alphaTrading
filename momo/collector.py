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

def accounts_report():

    #pull any assets waiting in spot (if any)
    spot = pd.DataFrame(config.kucoin.fetch_balance()['info']['data'])
    spot[['balance', 'available']] = spot[['balance', 'available']].astype(float)
    spot = spot[spot['balance']>0].set_index('currency')

    spot_values = pd.DataFrame(columns=['usdt_rate'])
    for c in spot.index:
        time.sleep(1)
        spot_values.loc[c,'usdt_rate'] = config.kucoin.fetch_ohlcv(c+'/'+'USDT','1m')[-1][4]

    spot = spot.join(spot_values)
    spot['usdt_value'] = spot['usdt_rate']*spot['balance']
    spot['account_value'] = spot['usdt_value'].sum()

    #pull futures account info and position status
    futures = pd.DataFrame(config.kucoin_futures.fetch_balance()['info'])[['data']]
    futures_positions = pd.DataFrame(config.kucoin_futures.fetch_positions())

    return {
        'spot':{
            'value':spot['account_value'].iloc[0],
            'holdings':spot
        },
        'futures':{

            'value': futures.loc['accountEquity'],
            'available_balance': futures.loc['availableBalance'],
            'position_margin': futures.loc['positionMargin'],
            'unrealised_pnl': futures.loc['unrealisedPNL'],
            'positions':futures_positions

        },
        'total':{
            'value': futures.loc['accountEquity'] + spot['account_value'].iloc[0]
        }
    }







