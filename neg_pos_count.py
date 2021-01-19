params =  {"var" : ""}
import _helper
_helper.tablename='my new filename'

import pandas as pd
import math
import numpy as np
import json


def main():
    data = _helper.data()
    if params["var"]   == 'positive':
        data['positive_count'] = data.select_dtypes(include='int64' or 'float64').ge(0).sum(axis=1)
    elif params["var"] == 'negative':
        data['negative_count'] = data.select_dtypes(include='int64' or 'float64').lt(0).sum(axis=1)
    elif params["var"] == 'both':
        data['positive_count'] = data.select_dtypes(include='int64' or 'float64').ge(0).sum(axis=1)
        data['positive_count'] = data.select_dtypes(include='int64' or 'float64').lt(0).sum(axis=1)

    return _helper.publish(data)
        
try:
    if main() != None:
        _helper.status(_helper.fileid, 2,'Completed')
except Exception as e:
    _helper.status(_helper.fileid, -2,str(e))
