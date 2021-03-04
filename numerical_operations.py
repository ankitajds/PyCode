#Enter the column name in a list columns
columns=[]
#Enter 'add' or'sub'or'mul' or 'div' in oper
oper=''
import _helper
import pandas as pd
import json

def main():
    df = _helper.data()
    for col in columns[0:1]:
        if oper =='add':
            df['add'] = df[col].astype('int64')
        elif oper =='sub':
            df['sub'] = df[col].astype('int64')
        elif oper =='mul':
            df['mul'] = df[col].astype('int64')
        elif oper =='div':
            df['div'] = df[col].astype('int64')
        else:
            return None
        
        for col in columns[1:]:
            if oper =='add':
                df['add'] += df[col].astype('int64')
                
            elif oper =='sub':
                df['sub'] -= df[col].astype('int64')
                
            elif oper =='mul':
                df['mul'] *= df[col].astype('int64')
                
            elif oper =='div':
                df['div'] /= df[col].astype('int64')
                
            else:
                return None
            
    return _helper.publish(df)
         
