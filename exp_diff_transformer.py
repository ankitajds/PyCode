# enter the column name which has integer or float datatype
column_1=''
column_2=''
#Enter the exponent values for the two columns
m =
n =
import _helper
import pandas as pd
import math
import json

def main():
    data = _helper.data() 
    if column_1 in data.columns and column_2 in data.columns : #Enter column 1 and column 2
        data['exp'] = pow(pd.to_numeric(data[column_1]),m) - pow(pd.to_numeric(data[column_2]),n)
        return _helper.publish(data)
    else:
        return None

    
