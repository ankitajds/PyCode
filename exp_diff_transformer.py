# enter the column name which has integer or float datatype
# raised to the power m and n 
params ={'column_1':'','column_2':'','m': ,'n':}
_helper.tablename='my new filename'


import pandas as pd
import math
import json
import _helper

def main():
    try:
        data = _helper.data() 
        if params['column_1'] in data and params['column_2'] in data :
            data['exp'] = pow(data[params['column_1']],params['m']) - pow(data[params['column_2']],params['n'])
            return _helper.publish(data)
        else:
            print("'column doesn't exist in data")
    except Exception as e:
        _helper.error(e)
