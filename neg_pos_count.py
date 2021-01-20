#Enter the positive or negative or both in var
var=''
import _helper
import pandas as pd
import math
import numpy as np
import json


def main():
    data = _helper.data()
    if var == 'positive':
        data['positive_count'] = data.select_dtypes(include='int64' or 'float64').ge(0).sum(axis=1)
        return _helper.publish(data)
    elif var == 'negative':
        data['negative_count'] = data.select_dtypes(include='int64' or 'float64').lt(0).sum(axis=1)
        return _helper.publish(data)
    elif var == 'both':
        data['positive_count'] = data.select_dtypes(include='int64' or 'float64').ge(0).sum(axis=1)
        data['positive_count'] = data.select_dtypes(include='int64' or 'float64').lt(0).sum(axis=1)
        return _helper.publish(data)
    else:
        return None
