#Enter column names in the list defined below
# pass the integer value in n variable for find square

params={'column':[],'m':}
_helper.tablename='my new filename'

import pandas as pd
import math
import json
import _helper
def main():
    df = _helper.data()
    for col in params['column']:
        try:
            df[col+"_n_root"]=df[col]**params['m']
            return _helper.publish(df)

        except:
            return 'Enter column names which have float  datatype'

    return _helper.publish(df)
        
try:
    if main() != None:
        _helper.status(_helper.fileid, 2,'Completed')
except Exception as e:
    _helper.status(_helper.fileid, -2,str(e))

    
                    
