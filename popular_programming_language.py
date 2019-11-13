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
