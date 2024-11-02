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
dfSelected=df[['vekova_kategorie','vzdelani', 'pohlavi', 'kraj', 'velikost_bydliste', 'politické_preference', 'hodnoceni_ceskeho_zdravotnictvi']]

#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#print(dfSelected.head)


clm = cleverminer(df=df,proc='SD4ftMiner',
                  quantifiers= {'Base1':40,'Base2':40, 'Ratioconf':1.5},
                  ante ={
                      'attributes':[
                          {'name': 'vekova_kategorie', 'type': 'subset', 'minlen': 1, 'maxlen': 3},
                          {'name': 'vzdelani', 'type': 'subset', 'minlen': 1, 'maxlen': 3},
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                          {'name': 'velikost_bydliste', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                          {'name': 'politické_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                      ], 'minlen':1, 'maxlen':4, 'type':'con'},
                  succ ={
                      'attributes':[
                          {'name': 'hodnoceni_ceskeho_zdravotnictvi', 'type': 'rcut', 'minlen': 1, 'maxlen': 2}
                      ], 'minlen':1, 'maxlen':1 , 'type':'con'},
                  frst ={
                      'attributes':[
                          {'name': 'pohlavi', 'type': 'one', 'value':'Muž'}
                      ], 'minlen':1, 'maxlen':1, 'type':'con'},
                  scnd ={
                      'attributes':[
                          {'name': 'pohlavi', 'type': 'one', 'value':'Žena'}
                      ], 'minlen':1, 'maxlen':1, 'type':'con'}
                  #               ,opts = {'no_optimizations':True,'max_categories':20}
                  )

clm.print_summary()
clm.print_rulelist()
clm.print_rule(1)