import _helper
from scipy import stats
import pandas as pd
import json
from sklearn.preprocessing import PowerTransformer

col=[]
def main():
    df = _helper.data()
    for c in col:
        if c in df:
            df[c] =df[c].astype('int64')
            features = df[[c]]
            pt = PowerTransformer(method='yeo-johnson', standardize=True,) 
            #Fit the data to the powertransformer
            pt_yeojohnson = pt.fit(features)
            #Transform the data 
            pt_yeojohnson = pt.transform(features)
            #Pass the transformed data into a new dataframe 
            df_xt = pd.DataFrame(data=pt_yeojohnson, columns=[c + '_yeojohn'])
            df=df.join(df_xt)
            

        else:
            return None
    
    
    return _helper.publish(df)

