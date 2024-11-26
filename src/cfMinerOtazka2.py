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
                  quantifiers= {'S_Up': 2, 'Base':15},
                  cond ={
                      'attributes':[
                          {'name': 'vekova_kategorie', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'vzdelani', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'velikost_bydliste', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                      ], 'minlen':1, 'maxlen':5, 'type':'con'}
                  )

clm.print_rulelist()
clm.print_summary()
clm.print_rule(1)
clm.draw_rule(1)
