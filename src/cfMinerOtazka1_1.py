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
dfSelected=df[['hodnoceni_zdravotnicka_zarizeni','politicke_preference', 'ochota_priplatit_nadstandardni_pojisteni']]

#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#print(dfSelected.head)

#ochota_priplatit_nadstandardni_pojisteni
clm = cleverminer(df=df,target='ochota_priplatit_nadstandardni_pojisteni',proc='CFMiner',
                  quantifiers= {'RelMax': 0.3, 'Base': 100},
                  cond ={
                      'attributes':[
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'ochota_priplatit_nadstandardni_pojisteni', 'type': 'lcut', 'minlen': 1, 'maxlen': 2},
                      ], 'minlen':1, 'maxlen':2, 'type':'con'}
                  )

clm.print_rulelist()
clm.print_summary()
clm.print_rule(1)
