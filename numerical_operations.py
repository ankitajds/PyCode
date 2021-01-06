params =  {"columns" : [],'oper':''}
_helper.tablename='my new filename'


import pandas as pd
import json
import _helper


def main():
    try:
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
          
        _helper.status(fileid,2,'')
        return _helper.publishbot(df)
        
    except Exception as e:
        _helper.status(fileid,-2,e)
         
