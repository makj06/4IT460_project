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
dfSelected=df[['vekova_kategorie', 'vzdelani', 'kraj','velikost_bydliste', 'politicke_preference','ochota_dojizdet_za_kvalitnejsi_peci', 'prerozdeleni_financi_zdravotnictvi_skolstvi', 'Q12_prerozdeleni_financi_zdravotnictvi_obrana', 'prerozdeleni_financi_zdravotnictvi_jine_rezorty', 'prerozdeleni_financi_beze_zmeny_uspory_uvnitr_zdravotnictvi']]
#transform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#print(dfSelected.head)

#skupina volicu smyslejici
clm = cleverminer(df=df,target='politicke_preference',proc='CFMiner',
                  quantifiers= {'RelMax_leq': 1, 'Base': 100},
                  cond ={
                      'attributes':[
                         {'name': 'vekova_kategorie', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                         {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                         {'name': 'velikost_bydliste', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'prerozdeleni_financi_zdravotnictvi_socialni_davky_duchody', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                      ], 'minlen':1, 'maxlen':4, 'type':'con'}
                  )

clm.print_rulelist()
clm.print_summary()
clm.print_rule(6)
clm.draw_rule(6)