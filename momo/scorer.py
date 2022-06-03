import pandas as pd

import momo.collector as collector
import momo.config as config



def scorer(data=collector.collect()):
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

    return {
        'scores':scores,
        'portfolio':df
    }
    










