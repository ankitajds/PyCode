#Enter column which has integer or float data type
column=''
import _helper
import pandas as pd
import math
import numpy as np
import json

def main():
    data = _helper.data() 
    #Enter the integer or float column
    if column in data:
        data['logarithm_base10'] = np.log10(data[column])
        return  _helper.publish(data)

    else:
        return None
  
        
