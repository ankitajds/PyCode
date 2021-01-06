params={'column':''}
_helper.tablename='my new filename'

import pandas as pd
import math
import numpy as np
import json
import _helper
def main():
    try:
        data = _helper.data() 
        if params['column'] in data:
            data['logarithm_base10'] = np.log10(data[params['column']])
            return  _helper.publish(data)
          
        else:
            print("column doesn't exist")
               
        _helper.status(fileid,2,'')
        return _helper.publishbot(df)
        
    except Exception as e:
        _helper.status(fileid,-2,e)
        
