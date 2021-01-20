params ={'column':''}
import _helper
#_helper.tablename='my new filename'
from scipy import stats
import pandas as pd
import json

def main():
    df = _helper.data()
    if params['column'] in df:
        transform = df[params['column']].values
        # transform values and store as "dft"
        dft = stats.boxcox(transform)
        df['box_cox'] = dft[0]
        return _helper.publish(df)
    else:
        return 'Column does not exist'

    return _helper.publish(df)
        
try:
    if main() != None:
        _helper.status(_helper.fileid, 2,'Completed')
except Exception as e:
    _helper.status(_helper.fileid, -2,str(e))
