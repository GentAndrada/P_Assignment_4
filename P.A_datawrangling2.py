# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 17:04:23 2019

@author: Samsung
"""

import pandas as pd
data={'Box':['Box1','Box1','Box1','Box2','Box2','Box2'],'Dimension':['Length','Width','Height','Length','Width','Height'],
      'Value':[6,4,2,5,3,4]}
messy = pd.DataFrame(data, columns = ['Box','Dimension','Value'])
tidy = messy.pivot_table(index='Box',columns='Dimension', values='Value').reset_index()
tidy['Volume'] = tidy.Length*tidy.Height*tidy.Width
print(tidy)
