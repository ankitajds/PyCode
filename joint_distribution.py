
# coding: utf-8

# In[ ]:


import _helper
import pandas as pd
import numpy as np
import plotly as py
import plotly.express as px

col1 = 'Temperature'
col2 = 'Humidity'
color_col = ''

def main():
    df = _helper.data()
    fig = px.histogram(df, x=col1, y=col2, color=color_col, marginal="box",hover_data=df.columns)
    cor_fig.write_html('joint_distribution.html',include_plotlyjs = 'cdn',config={'displayModeBar': False}, full_html = False, default_width='65%', default_height='65%')
    
main()

