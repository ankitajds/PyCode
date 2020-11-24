params={'column':''}
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
               
    except Exception as e:
          print(e)
        
