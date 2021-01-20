#Enter column names in the list defined below
columns = [ ]
#window size is the number of observations used for calculating the statistic.
win_size=
#Provide a window type like boxcar , hamming ,triang , blackman.
window_type=''
#Provide a operation like sum or mean.
operation=''
import _helper
import pandas as pd
import numpy as np
import re
from pandas import read_csv
import json


def main():
    du = _helper.data()
    for col in columns :
        if operation =="sum":
            du[col+"_sum"] = du[col].rolling(window_size = win_size, win_type = window_type).sum()
        elif operation =="mean":
            du[col+"_mean"] = du[col].rolling(window_size = win_size, win_type = window_type).mean()


    return _helper.publish(du)
        

   
  
