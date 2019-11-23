
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[2]:

df_2019 = pd.read_csv("./input/2019 Survey Result.csv")
df_2019['Year'] = '2019'


# In[3]:

df_2019_lang_used = df_2019[['Respondent','LanguageWorkedWith']]


# In[4]:

def splitter(values):
    return list(itertools.product( *[str(v).split(';') for v in values]))

def expand(df):
    tuples=list()
    for i,row in df.iterrows():
        tuples.extend(splitter(row))
    return  pd.DataFrame.from_records(tuples,columns=df.columns)


# In[5]:

df_2019_lang_used = expand(df_2019_lang_used)


# In[6]:

df_2019_lang_used = pd.DataFrame(df_2019_lang_used['LanguageWorkedWith'].value_counts().reset_index())
df_2019_lang_used.rename(columns={'index':'LanguageWorkedWith','LanguageWorkedWith':'count'}, inplace=True)
df_2019_lang_used = df_2019_lang_used.sort_values('count', ascending=True)
df_2019_lang_used['perc'] = (df_2019_lang_used['count']/len(df_2019[df_2019['LanguageWorkedWith'].notnull()]))*100


# In[7]:

def plot_barh(df,x_col,y_col):
    x_pos = [i for i, _ in enumerate(df[x_col])]
    plt.figure(figsize=(10,10))
    plt.barh(x_pos,df[y_col])
    plt.yticks(x_pos, df[x_col])
    plt.show()


# In[8]:

plot_barh(df_2019_lang_used,'LanguageWorkedWith','perc')


# ### Language Users

# In[9]:

df_2019_lang_user = df_2019[['Respondent','LanguageWorkedWith','DevType']]
df_2019_lang_user = df_2019_lang_user[df_2019_lang_user['DevType'].notnull()]
df_2019_lang_user = expand(df_2019_lang_user)


# In[12]:

df_2019_lang_user = df_2019_lang_user.groupby(['LanguageWorkedWith','DevType']).size().reset_index().rename(columns={0:'count'}).sort_values('count', ascending=False)


# In[13]:

df_2019_lang_user[df_2019_lang_user['LanguageWorkedWith']=='JavaScript']


# In[14]:

df_2019_lang_user[df_2019_lang_user['LanguageWorkedWith']=='Python']


# In[ ]:



