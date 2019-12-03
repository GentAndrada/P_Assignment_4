# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:28:20 2019

@author: 2ecea-4
"""

import pandas as pd
data1 = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
a = pd.DataFrame(data1, columns=['Student','Math'])

data2 = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
b = pd.DataFrame(data2, columns=['Student','Electronics'])

data3 = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
c = pd.DataFrame(data3, columns=['Student','GEAS'])

data4 = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
d = pd.DataFrame(data4, columns=['Student','ESAT'])

e = pd.merge(a,b)
f = pd.merge(e,c)
result = pd.merge(f,d)
print(result,'\n')
long = pd.melt(result, id_vars='Student', var_name='Subject', value_name='Grades')
print(long)

       