import pandas as pd
import openpyxl

from sklearn.impute import SimpleImputer
from cleverminer import cleverminer

#read the data
df = pd.read_excel ('../data/napo.xlsx')
#in braskets are defined names of columns
df2 = df[['pohlavi', 'vek']]

# Log all columns
print(df.columns)

# Remove missing values in rows
imputer = SimpleImputer(strategy="most_frequent")
df2 = pd.DataFrame(imputer.fit_transform(df2),columns = df2.columns)


# Log first 5 rows
print(df2.head)










'''
df=df[['Driver_Age_Band','Sex','Speed_limit','Severity']]

#handle missing values
imputer = SimpleImputer(strategy="most_frequent")
df = pd.DataFrame(imputer.fit_transform(df),columns = df.columns)

clm = cleverminer(df=df,proc='4ftMiner',
                  quantifiers= {'Base':2000, 'aad':0.4},
                  ante ={
                      'attributes':[
                          {'name': 'Driver_Age_Band', 'type': 'seq', 'minlen': 1, 'maxlen': 3},
                          {'name': 'Speed_limit', 'type': 'seq', 'minlen': 1, 'maxlen': 2},
                          {'name': 'Sex', 'type': 'subset', 'minlen': 1, 'maxlen': 1},
                      ], 'minlen':1, 'maxlen':3, 'type':'con'},
                  succ ={
                      'attributes':[
                          {'name': 'Severity', 'type': 'lcut', 'minlen': 1, 'maxlen': 2}
                      ], 'minlen':1, 'maxlen':1 , 'type':'con'}
                  )

clm.print_summary()
clm.print_rulelist()
clm.print_rule(8)'''