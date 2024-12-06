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
dfSelected=df[['politicke_preference','souhrn_spokojenost_zdr_zarizeni', 'vekova_kategorie', 'vzdelani', 'kraj', 'velikost_bydliste']]

#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#print(dfSelected.head)
clm = cleverminer(df=df,target='souhrn_spokojenost_zdr_zarizeni',proc='CFMiner',
                  quantifiers= {'S_Up': 2, 'Base':30},
                  cond ={
                      'attributes':[
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'vekova_kategorie', 'type': 'seq', 'minlen': 1, 'maxlen': 2},
                          {'name': 'vzdelani', 'type': 'seq', 'minlen': 1, 'maxlen': 3},
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'velikost_bydliste', 'type': 'seq', 'minlen': 1, 'maxlen': 2},
                      ], 'minlen':1, 'maxlen':5, 'type':'con'}
                  )

clm.print_rulelist()
clm.print_summary()
clm.print_rule(2)
clm.draw_rule(2)
