import pandas as pd
import numpy as np

import insyded.collector as collector


def insyde(x):

    df = x.iloc[-3:-1]
    df['insyde'] = np.where((df['high']<df['high'].shift(1)) & (df['low']>df['low'].shift(1)), 1, 0)
    df=df.iloc[-1]

    return df


data = collector.collect()['data']
scan = data.groupby('symbol').apply(lambda x: insyde(x)).sort_values(by='insyde', ascending=False)
print(scan)

