
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[2]:

df_2016 = pd.read_csv("./input/2016 Stack Overflow Survey Responses.csv")
df_2017 = pd.read_csv("./input/2017 Survey Result.csv")
df_2018 = pd.read_csv("./input/2018 Survey Result.csv")
df_2019 = pd.read_csv("./input/2019 Survey Result.csv")


# In[16]:

df_2016 = df_2016[df_2016['tech_do'].notnull()]
df_2017 = df_2017[df_2017['HaveWorkedLanguage'].notnull()]
df_2018 = df_2018[df_2018['LanguageWorkedWith'].notnull()]
df_2019 = df_2019[df_2019['LanguageWorkedWith'].notnull()]

df_2016['tech_do'] = df_2016['tech_do'].str.strip() 
df_2017['HaveWorkedLanguage'] = df_2017['HaveWorkedLanguage'].str.strip() 
df_2018['LanguageWorkedWith'] = df_2018['LanguageWorkedWith'].str.strip() 
df_2019['LanguageWorkedWith'] = df_2019['LanguageWorkedWith'].str.strip() 


# In[17]:

df_2016_lang_used = df_2016[['Unnamed: 0','tech_do']]
df_2017_lang_used = df_2017[['Respondent','HaveWorkedLanguage']]
df_2018_lang_used = df_2018[['Respondent','LanguageWorkedWith']]
df_2019_lang_used = df_2019[['Respondent','LanguageWorkedWith']]


# In[18]:

def splitter(values):
    return list(itertools.product( *[str(v).split(';') for v in values]))

def expand(df):
    tuples=list()
    for i,row in df.iterrows():
        tuples.extend(splitter(row))
    return  pd.DataFrame.from_records(tuples,columns=df.columns)


# In[19]:

df_2016_lang_used = expand(df_2016_lang_used)
df_2017_lang_used = expand(df_2017_lang_used)
df_2018_lang_used = expand(df_2018_lang_used)
df_2019_lang_used = expand(df_2019_lang_used)


# In[20]:

df_2016_lang_used['tech_do'] = df_2016_lang_used['tech_do'].str.strip() 
df_2017_lang_used['HaveWorkedLanguage'] = df_2017_lang_used['HaveWorkedLanguage'].str.strip() 
df_2018_lang_used['LanguageWorkedWith'] = df_2018_lang_used['LanguageWorkedWith'].str.strip() 
df_2019_lang_used['LanguageWorkedWith'] = df_2019_lang_used['LanguageWorkedWith'].str.strip() 


# In[21]:

most_used_lang_2016 = pd.DataFrame(df_2016_lang_used['tech_do'].value_counts().reset_index())
most_used_lang_2017 = pd.DataFrame(df_2017_lang_used['HaveWorkedLanguage'].value_counts().reset_index())
most_used_lang_2018 = pd.DataFrame(df_2018_lang_used['LanguageWorkedWith'].value_counts().reset_index())
most_used_lang_2019 = pd.DataFrame(df_2019_lang_used['LanguageWorkedWith'].value_counts().reset_index())


# In[22]:

most_used_lang_2016.rename(columns={'index':'LanguageWorkedWith','tech_do':'count'}, inplace=True)
most_used_lang_2017.rename(columns={'index':'LanguageWorkedWith','HaveWorkedLanguage':'count'}, inplace=True)
most_used_lang_2018.rename(columns={'index':'LanguageWorkedWith','LanguageWorkedWith':'count'}, inplace=True)
most_used_lang_2019.rename(columns={'index':'LanguageWorkedWith','LanguageWorkedWith':'count'}, inplace=True)


# In[23]:

most_used_lang_2016['Year'] = '2016'
most_used_lang_2017['Year'] = '2017'
most_used_lang_2018['Year'] = '2018'
most_used_lang_2019['Year'] = '2019'


# In[24]:

most_used_lang_2016 = most_used_lang_2016.sort_values('count', ascending=False)
most_used_lang_2017 = most_used_lang_2017.sort_values('count', ascending=False)
most_used_lang_2018 = most_used_lang_2018.sort_values('count', ascending=False)
most_used_lang_2019 = most_used_lang_2019.sort_values('count', ascending=False)


# In[25]:

most_used_lang_2016 = most_used_lang_2016[:7]
most_used_lang_2017 = most_used_lang_2017[:7]
most_used_lang_2018 = most_used_lang_2018[:7]
most_used_lang_2019 = most_used_lang_2019[:7]


# In[26]:

most_used_lang_2016['perc'] = (most_used_lang_2016['count']/len(df_2016))*100
most_used_lang_2017['perc'] = (most_used_lang_2017['count']/len(df_2017))*100
most_used_lang_2018['perc'] = (most_used_lang_2018['count']/len(df_2018))*100
most_used_lang_2019['perc'] = (most_used_lang_2019['count']/len(df_2019))*100


# In[27]:

all_years = pd.concat([
most_used_lang_2016,
most_used_lang_2017,
most_used_lang_2018,
most_used_lang_2019], axis=0)


# In[28]:

all_years_pvt = all_years.pivot(index='Year', columns='LanguageWorkedWith', values='perc')
all_years_pvt.plot() 
plt.gcf().set_size_inches(20, 10)
plt.legend(loc=2, prop={'size': 20})

