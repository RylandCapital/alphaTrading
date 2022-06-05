import pandas as pd
import numpy as np

import momo.collector as collector
import momo.config as config



def scorer(data=collector.ohlc ()):
    print('...scoring current universe')

    scores = data['data'].groupby('symbol').apply(
        lambda x: config.momentum_score(x['close'])
        ).sort_values(ascending=False).iloc[:config.portfolio_size]

    volas = data['data'].groupby('symbol').apply(
        lambda x: config.volatility(x['close'])
        ).sort_values(ascending=False)

    df = pd.DataFrame(scores).join(
        pd.DataFrame(volas), rsuffix='_vola'
    )
    df.columns = ['scores', 'volatility']

    df['vol_weighted_sizing'] = 1 / df['volatility']
    sum_inverse = np.sum(df['vol_weighted_sizing'])         
    df['vol_weighted_sizing'] = df['vol_weighted_sizing'] / sum_inverse

    return {
        'scores':scores,
        'model':df
    }
    










