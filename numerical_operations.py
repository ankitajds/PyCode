params =  {"columns" : [],'oper':''}
import _helper
import pandas as pd
import json

def main():
    df = _helper.data()
    for col in params['columns'][0:1]:
        if params['oper']=='add':
            df['add'] = df[col]
        elif params['oper']=='sub':
            df['sub'] = df[col]
        elif params['oper']=='mul':
            df['mul'] = df[col]
        elif params['oper']=='div':
            df['div'] = df[col]
        for col in params['columns'][1:]:
            if params['oper']=='add':
                df['add'] += df[col]
            elif params['oper']=='sub':
                df['sub'] -= df[col]
            elif params['oper']=='mul':
                df['mul'] *= df[col]
            elif params['oper']=='div':
                df['div'] /= df[col]

    return _helper.publish(df)
        
try:
    if main() != None:
        _helper.status(_helper.fileid, 2,'Completed')
except Exception as e:
    _helper.status(_helper.fileid, -2,str(e))
         
