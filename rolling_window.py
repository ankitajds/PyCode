#Enter column names in the list defined below
#column = [ ]
#win size is the number of observations used for calculating the statistic.
#Provide a window type like boxcar , hamming ,triang , blackman.
#Provide a operation like sum or mean.

params={'columns':[],'window_size':,'window_type':,'operation': }
import _helper
_helper.tablename='my new filename'

import pandas as pd
import numpy as np
import re
from pandas import read_csv
import json


def main():
    du = _helper.data()
    for col in params['columns']:
        if params['operation'] =="sum":
            du[col+"_sum"] = du[col].rolling(params['window_size'],win_type = params['window_type']).sum()
        elif params['operation'] =="mean":
            du[col+"_mean"] = du[col].rolling(params['window_size'], win_type = params['window_type']).mean()



    return _helper.publish(du)
        
try:
    if main() != None:
        _helper.status(_helper.fileid, 2,'Completed')
except Exception as e:
    _helper.status(_helper.fileid, -2,str(e))
        

   
  
