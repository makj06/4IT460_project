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
dfSelected=df[['vekova_kategorie','politické_preference', 'hodnoceni_ceskeho_zdravotnictvi']]

#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

clm = cleverminer(df=df,proc='4ftMiner',
                  quantifiers= {'Base':100, 'conf':0.3},
                  ante ={
                      'attributes':[
                         {'name': 'vekova_kategorie', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                          {'name': 'politické_preference', 'type': 'one', 'value':'ANO'},
                      ], 'minlen':1, 'maxlen':1, 'type':'con'},
                  succ ={
                      'attributes':[
                          {'name': 'hodnoceni_ceskeho_zdravotnictvi', 'type': 'lcut', 'minlen': 1, 'maxlen': 2}
                      ], 'minlen':1, 'maxlen':1 , 'type':'con'}
                  )


clm.print_summary()
clm.print_rulelist()
clm.print_rule(8)
