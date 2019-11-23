
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[2]:

df_2018 = pd.read_csv("./input/2018 Survey Result.csv")
df_2018['Year'] = '2018'


# In[3]:

df_2018_lang_used = df_2018[['LanguageWorkedWith','ConvertedSalary']]
df_2018_lang_used= df_2018_lang_used[df_2018_lang_used['ConvertedSalary'].notnull()]


# In[4]:

def splitter(values):
    return list(itertools.product( *[str(v).split(';') for v in values]))

def expand(df):
    tuples=list()
    for i,row in df.iterrows():
        tuples.extend(splitter(row))
    return  pd.DataFrame.from_records(tuples,columns=df.columns)


# In[5]:

df_2018_lang_used = expand(df_2018_lang_used)


# In[12]:

df_2018_lang_used['ConvertedSalary'] = (pd.to_numeric(df_2018_lang_used['ConvertedSalary'])).astype(int)


# In[26]:

df_2018_group = pd.to_numeric(df_2018_lang_used['ConvertedSalary']).groupby(df_2018_lang_used['LanguageWorkedWith'])


# In[27]:

df_2018_group = df_2018_group.median().reset_index()


# In[28]:

def plot_barh(df,x_col,y_col):
    x_pos = [i for i, _ in enumerate(df[x_col])]
    plt.figure(figsize=(10,10))
    plt.barh(x_pos,df[y_col])
    plt.yticks(x_pos, df[x_col])
    plt.show()


# In[29]:

df_2018_group = df_2018_group[df_2018_group['ConvertedSalary']!='nan']


# In[30]:

df_2018_group = df_2018_group.sort_values('ConvertedSalary',ascending=True)


# In[31]:

plot_barh(df_2018_group,'LanguageWorkedWith','ConvertedSalary')


# In[ ]:



