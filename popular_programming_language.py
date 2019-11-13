import pandas as pd
import zipfile
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

df_2011 = pd.read_csv("./input/2011 Stack Overflow Survey Results.csv")
df_2011['Year'] = '2011'
df_2012 = pd.read_csv("./input/2012 Stack Overflow Survey Results.csv")
df_2012['Year'] = '2012'
df_2013 = pd.read_csv("./input/2013 Stack Overflow Survey Responses.csv")
df_2013['Year'] = '2013'
df_2014 = pd.read_csv("./input/2014 Stack Overflow Survey Responses.csv")
df_2014['Year'] = '2014'
df_2015 = pd.read_csv("./input/2015 Stack Overflow Developer Survey Responses.csv")
df_2015['Year'] = '2015'
df_2016 = pd.read_csv("./input/2016 Stack Overflow Survey Responses.csv")
df_2016['Year'] = '2016'
df_2017 = pd.read_csv("./input/2017 Survey Result.csv")
df_2017['Year'] = '2017'
df_2018 = pd.read_csv("./input/2018 Survey Result.csv")
df_2018['Year'] = '2018'
df_2019 = pd.read_csv("./input/2019 Survey Result.csv")
df_2019['Year'] = '2019'

df_2016 = df_2016[['Year','age_range','country','gender','job_satisfaction','salary_range','programming_ability','tech_do','tech_want']]
df_2017 = df_2017[['Respondent','Year','WantWorkLanguage','HaveWorkedLanguage','Gender','DeveloperType','Country','CompanySize','Salary','CareerSatisfaction','JobSatisfaction']]
df_2018 = df_2018[['Respondent','LanguageDesireNextYear','LanguageWorkedWith','Age','CareerSatisfaction','CompanySize','DevType','Gender','JobSatisfaction','Salary','ConvertedSalary','Year','Country','SelfTaughtTypes']]
df_2019 = df_2019[['Respondent','Age','CompTotal','CareerSat','Country','DevType','Gender','LanguageDesireNextYear','LanguageWorkedWith','Year']]

possible_vals = ['Python','Java','JavaScript','TypeScript','Rust','Go','PHP','C#','C','Ruby','SQL',
                 'Kotlin','WebAssembly','Swift','Clojure','Elixir','Dart','HTML/CSS','F#','Bash/Shell/PowerShell',
                 'Scala','C++','R','Erlang','Assembly','VBA','Objective-C']

df_2016_values  = df_2016['tech_do'].value_counts().reset_index()
df_2017_values  = df_2017['HaveWorkedLanguage'].value_counts().reset_index()
df_2018_values  = df_2018['LanguageWorkedWith'].value_counts().reset_index()
df_2019_values  = df_2019['LanguageWorkedWith'].value_counts().reset_index()

df_2016_values.rename(columns={'index':'language','tech_do': 'count'}, inplace=True)
df_2017_values.rename(columns={ 'index':'language','HaveWorkedLanguage': 'count'},inplace=True)
df_2018_values.rename(columns={ 'index':'language','LanguageWorkedWith': 'count'},inplace=True)
df_2019_values.rename(columns={ 'index':'language','LanguageWorkedWith': 'count'},inplace=True)

def total_count(df, col1, col2, look_for):
    '''
    INPUT:
    df - the pandas dataframe you want to search
    col1 - the column name you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of df[col]
    
    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it shows up 
    '''
    new_df = defaultdict(int)
    for val in look_for:
        for idx in range(df.shape[0]):
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])   
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df
  
most_popular_lang_2016 = total_count(df_2016_values, 'language', 'count', possible_vals)
most_popular_lang_2017 = total_count(df_2017_values, 'language', 'count', possible_vals)
most_popular_lang_2018 = total_count(df_2018_values, 'language', 'count', possible_vals)
most_popular_lang_2019 = total_count(df_2019_values, 'language', 'count', possible_vals)

most_popular_lang_2016 = most_popular_lang_2016.sort_values('count',ascending=True)
most_popular_lang_2017 = most_popular_lang_2017.sort_values('count',ascending=True)
most_popular_lang_2018 = most_popular_lang_2018.sort_values('count',ascending=True)
most_popular_lang_2019 = most_popular_lang_2019.sort_values('count',ascending=True)

def plot_barh(df,x_col,y_col):
    x_pos = [i for i, _ in enumerate(df[x_col])]
    plt.figure(figsize=(8,8))
    plt.barh(x_pos,df[y_col])
    plt.yticks(x_pos, df[x_col])
    plt.show()
    
    
plot_barh(most_popular_lang_2016,'language','count')
plot_barh(most_popular_lang_2017,'language','count')
plot_barh(most_popular_lang_2018,'language','count')
plot_barh(most_popular_lang_2019,'language','count')
