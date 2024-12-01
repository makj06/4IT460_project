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
dfSelected=df[['vekova_kategorie','vzdelani', 'pohlavi', 'kraj', 'velikost_bydliste', 'politicke_preference', 'hodnoceni_ceskeho_zdravotnictvi']]



#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#print(dfSelected.head)


clm = cleverminer(df=df,proc='SD4ftMiner',
                  quantifiers= {'Base1':20,'Base2':20, 'Ratioconf':2},
                  ante ={
                      'attributes':[
                          {'name': 'vekova_kategorie', 'type': 'seq', 'minlen': 1, 'maxlen': 2},
                          {'name': 'vzdelani', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                          {'name': 'velikost_bydliste', 'type': 'seq', 'minlen': 1, 'maxlen': 2},
                          {'name': 'pohlavi', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                      ], 'minlen':1, 'maxlen':4, 'type':'con'},
                  succ ={
                      'attributes':[
                          {'name': 'hodnoceni_ceskeho_zdravotnictvi', 'type': 'lcut', 'minlen': 1, 'maxlen': 2}
                      ], 'minlen':1, 'maxlen':1 , 'type':'con'},
                  frst ={
                      'attributes':[
                          {'name': 'politicke_preference', 'type': 'one', 'value':'Spolu (ODS, KDU-ČSL, TOP 09)'},
                      ], 'minlen':1, 'maxlen':1, 'type':'con'},
                  scnd ={
                      'attributes':[
                          {'name': 'politicke_preference', 'type': 'one', 'value':'ANO'},
                      ], 'minlen':1, 'maxlen':1, 'type':'con'}
                  #               ,opts = {'no_optimizations':True,'max_categories':20}
                  )

clm.print_summary()
clm.print_rulelist()
clm.print_rule(13)
clm.draw_rule(13)