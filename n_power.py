import _helper
import pandas as pd
import math
import json
#Enter column names in the list defined below
columns=[]
# pass the integer value in n variable for find square
n=
def main():
    df = _helper.data()
    for col in columns:
        try:
            df[col+"_n_root"]=df[col]**n
            return _helper.publish(df)

        except:
            return 'Enter column names which have float  datatype'

    return _helper.publish(df)

    
                    
