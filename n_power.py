#Enter column names in the list defined below
columns=[]
# pass the integer value in n variable for find square
n=
import _helper
import pandas as pd
import math
import json

def main():
    df = _helper.data()
    for col in columns:
        if col in df.columns:
            df[col+"_n_root"]=pd.to_numeric(df[col])**n
            return _helper.publish(df)
        else:
            return None

    
                    
