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
dfSelected=df[['souhrn_spokojenost_zdr_zarizeni','politicke_preference', 'spokojenost_nemocnice', 'spokojenost_prakticky_lekar', 'spokojenost_ambulantni_specialiste', "souhr_hodnoceni_prvku_zdrav"]]

#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#print(dfSelected.head)
clm = cleverminer(df=df,target='politicke_preference',proc='CFMiner',
                  quantifiers= {'S_Up': 2},
                  cond ={
                      'attributes':[
                          #{'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'spokojenost_nemocnice', 'type': 'lcut', 'minlen': 1, 'maxlen': 2},
                          {'name': 'spokojenost_prakticky_lekar', 'type': 'lcut', 'minlen': 1, 'maxlen': 2},
                          {'name': 'spokojenost_ambulantni_specialiste', 'type': 'lcut', 'minlen': 1, 'maxlen': 2},
                      ], 'minlen':1, 'maxlen':2, 'type':'con'}
                  )

clm.print_rulelist()
clm.print_summary()
clm.print_rule(1)
