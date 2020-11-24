params ={'column':''}
_helper.tablename='my new filename'

from scipy import stats
import pandas as pd
import json
import _helper
def main():
    try:
        df = _helper.data()
        if params['column'] in df:
            transform = df[params['column']].values
            # transform values and store as "dft"
            dft = stats.boxcox(transform)
            df['box_cox'] = dft[0]
            return _helper.publish(df)
        else:
            return 'Column does not exist'
        
    except Exception as e:
        print(e)
