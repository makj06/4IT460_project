import pandas as pd
import openpyxl
import sys

from matplotlib import pyplot as plt
from sklearn.impute import SimpleImputer
from cleverminer import cleverminer

#Načtení dat
df = pd.read_excel ('../data/napo.xlsx')
#print(df.columns)

#Výběr sloupců používaných při proceduře
dfSelected=df[['politicke_preference','souhrn_spokojenost_zdr_zarizeni', 'vekova_kategorie', 'vzdelani', 'kraj', 'velikost_bydliste']]

#Transformace dat do tabulky
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#Provedení CF Miner procedury
clm = cleverminer(df=df,target='souhrn_spokojenost_zdr_zarizeni',proc='CFMiner',
                  quantifiers= {'S_Up': 2, 'Base':30},
                  cond ={
                      'attributes':[
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1}, #Typ proměnné je subset, protože se jedná o nominální proměnnou
                          {'name': 'vekova_kategorie', 'type': 'seq', 'minlen': 1, 'maxlen': 2}, #Typ proměnné je sequence, protože se jedná o  ordinální proměnnou
                          {'name': 'vzdelani', 'type': 'seq', 'minlen': 1, 'maxlen': 3}, #Typ proměnné je sequence, protože se jedná o  ordinální proměnnou
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 1}, #Typ proměnné je subset, protože se jedná o nominální proměnnou
                          {'name': 'velikost_bydliste', 'type': 'seq', 'minlen': 1, 'maxlen': 2}, #Typ proměnné je sequence, protože se jedná o  ordinální proměnnou
                      ], 'minlen':1, 'maxlen':5, 'type':'con'}
                  )
#Vylogování shrnujících informací
clm.print_summary()
#Vylogování nalezených pravidel
clm.print_rulelist()
#Vylogování pravidla číslo 2.
clm.print_rule(2)
#Zakreslení pravidla 2 do grafu.
clm.draw_rule(2)
