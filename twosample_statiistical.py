# Two sample t-test
#Enter column name having numerical values
col_1=''
col_2=''
#enter t_test like Kolmogrov-Smirnov or student t_test, median mood test
t_test=''
import numpy as np
import _helper
from scipy.stats import ttest_ind,ks_2samp, median_test

def main():
    df= pd.read_csv(r'D:\eda\dataset\wineQualityReds.csv')
    if t_test=='student t_test':
        # null hypothesis: expected value =
        t_statistic, p_value = ttest_ind(df[col_1], df[col_2])
    elif t_test=='Kolmogrov-Smirnov':
        # two sample Kolmogrov-Smirnov test t
        z_statistic, p_value = ks_2samp(df[col_1],df[col_2])
    else:
        #two sample median mood test
        stat, p_value,m,tb = median_test(df[col_1],df[col_2])
        p_value = "{:.30f}".format(p_value)
    df[col_1 +'_'+ col_2 + "_p_value"] = p_value
    return _helper.publish(df)
