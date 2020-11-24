#Enter column names in the list defined below
# pass the integer value in n variable for find square

params={'column':[],'m':}

import pandas as pd
import math
import json
import _helper
def main():
    try:
        df = _helper.data()
        for col in params['column']:
            try:
                df[col+"_n_root"]=df[col]**params['m']
                return _helper.publish(df)

            except:
                return 'Enter column names which have float  datatype'


    except Exception as e:
        print(e)

    
                    
