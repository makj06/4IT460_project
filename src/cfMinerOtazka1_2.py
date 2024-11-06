import pandas as pd
import openpyxl
import sys

from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer
from cleverminer import cleverminer

#read the data
df = pd.read_excel ('../data/napo.xlsx')
#print(df.columns)

#select only required rows
dfSelected=df[['vekova_kategorie','vzdelani', 'pohlavi', 'kraj', 'velikost_bydliste', 'politicke_preference', 'prime_platby_cekani_specialista']]

#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#print(dfSelected.head)
clm = cleverminer(df=df,target='prime_platby_cekani_specialista',proc='CFMiner',
                  quantifiers= {'RelMax': 0.3, 'Base': 100},
                  cond ={
                      'attributes':[
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'vekova_kategorie', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'velikost_bydliste', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'vzdelani', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'pohlavi', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                      ], 'minlen':1, 'maxlen':2, 'type':'con'}
                  )

clm.print_rulelist()
clm.print_summary()
clm.print_rule(1)
