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
dfSelected=df[['vekova_kategorie','politicke_preference', 'hodnoceni_ceskeho_zdravotnictvi', 'kdy_resit_zmeny']]

#trandform to table
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

clm = cleverminer(df=df,proc='4ftMiner',
                  quantifiers= {'Base':10, 'conf':0.1},
                  ante={
                      'attributes': [
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'vzdelani', 'type': 'subset', 'minlen': 1, 'maxlen': 2},
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                          {'name': 'velikost_bydliste', 'type': 'subset', 'minlen': 1, 'maxlen': 2}
                      ],
                      'minlen': 1,
                      'maxlen': 3,
                      'type': 'con'
                  },
                  succ={
                      'attributes': [
                          {'name': 'kdy_resit_zmeny', 'type': 'one', 'value': 'Co nejdříve, ihned'}
                      ],
                      'minlen': 1,
                      'maxlen': 1,
                      'type': 'con'
                  }
                  )

clm.print_summary()
clm.print_rulelist()
clm.print_rule(1)
