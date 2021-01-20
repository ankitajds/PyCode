params={'column':''}
import _helper
#_helper.tablename='my new filename'
import pandas as pd
import math
import numpy as np
import json

def main():
    data = _helper.data() 
    if params['column'] in data:
        data['logarithm_base10'] = np.log10(data[params['column']])
        return  _helper.publish(data)

    else:
        print("column doesn't exist")


    return _helper.publish(data)
        
try:
    if main() != None:
        _helper.status(_helper.fileid, 2,'Completed')
except Exception as e:
    _helper.status(_helper.fileid, -2,str(e))
        
