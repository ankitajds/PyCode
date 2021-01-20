# enter the column name which has integer or float datatype
# raised to the power m and n 

import _helper
import pandas as pd
import math
import json

#Enter the exponent values for the two columns
m =
n =

def main():
    data = _helper.data() 
    if 'column_1' in data.columns and 'column_2' in data.columns : #Enter column 1 and column 2
        data['exp'] = pow(data['column_1'],m]) - pow(data['column_2'],n])
        return _helper.publish(data)
    else:
        return None

    
