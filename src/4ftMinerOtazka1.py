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
dfSelected=df[['vekova_kategorie','politicke_preference', 'vzdelani','hodnoceni_ceskeho_zdravotnictvi', 'kraj','velikost_bydliste', 'ekonomicke_postaveni', 'cisty_mesicni_prijem']]

#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

clm = cleverminer(df=df,proc='4ftMiner',
                  quantifiers= {'Base':15, 'conf':0.7},
                  ante ={
                      'attributes':[
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'vekova_kategorie', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'velikost_bydliste', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'vzdelani', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'cisty_mesicni_prijem', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'ekonomicke_postaveni', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                      ], 'minlen':2, 'maxlen':7, 'type':'con'},
                  succ ={
                      'attributes':[
                          {'name': 'ochota_dojizdet_za_kvalitnejsi_peci', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
                      ], 'minlen':1, 'maxlen':1 , 'type':'con'}
                  )


clm.print_summary()
clm.print_rulelist()
clm.print_rule(1)
clm.draw_rule(1)