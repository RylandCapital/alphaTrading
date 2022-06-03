import pandas as pd
import datetime as dt

import momo.config as config

def collect():
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

            
            dfs.append(data)
        
        except:
            print('Symbol: {0} was not collected, check api symbols offered'.format(c))
            errors.append(c)

    print('{0} successfully collected, {1} assets were removed'.format(len(dfs), len(errors)))
    return {
        'data': pd.concat(dfs), 
        'not_included': errors
        }

