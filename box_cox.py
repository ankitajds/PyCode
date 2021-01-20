import _helper
from scipy import stats
import pandas as pd
import json
#Enter the column which has integer data type.Column should be >=0
col=''
def main():
    df = _helper.data()
    if col in df:
        if df[col].dtypes=='float64':
            df[col]=df[col].astype(int)
            transform = df[col].values
            # transform values and store as "dft"
            dft = stats.boxcox(transform)
            df['box_cox'] = dft[0]
        elif df[col].dtypes=='int64':
            transform = df[col].values
            # transform values and store as "dft"
            dft = stats.boxcox(transform)
            df['box_cox'] = dft[0]
        return _helper.publish(df)
    else:
        return None

    
        
