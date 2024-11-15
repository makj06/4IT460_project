import pandas as pd
import openpyxl
import sys

from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer
from cleverminer import cleverminer

#Otázka: Závisí volba politické strany na zkušenosti s přímými platbami za nedstandardní záležitosti?

#read the data
df = pd.read_excel ('../../data/napo.xlsx')
#print(df.columns)

#select only required rows
dfSelected=df[['politicke_preference', 'prerozdeleni_financi_zdravotnictvi_socialni_davky_duchody']]

#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

clm = cleverminer(df=df,proc='4ftMiner',
                  quantifiers= {'Base':20, 'conf':0.5},
                  ante ={
                      'attributes':[
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1}
                      ], 'minlen':1, 'maxlen':1, 'type':'con'},
                  succ ={
                      'attributes':[
                          {'name': 'platba_bez_zkusenosti', 'type': 'one', 'value': 'ne'}
                      ], 'minlen':1, 'maxlen':1 , 'type':'con'}
                  )


clm.print_summary()
clm.print_rulelist()
clm.print_rule(1)
