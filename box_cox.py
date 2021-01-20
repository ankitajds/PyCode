import _helper
from scipy import stats
import pandas as pd
import json

def main():
    df = _helper.data()
    #Enter the column which has integer data type
    if 'column' in df:
        transform = df['column'].values
        # transform values and store as "dft"
        dft = stats.boxcox(transform)
        df['box_cox'] = dft[0]
        return _helper.publish(df)
    else:
        return 'Column does not exist'

    return _helper.publish(df)
        
