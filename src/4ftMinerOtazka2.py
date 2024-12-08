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
dfSelected=df[['vekova_kategorie','politicke_preference', 'vzdelani', 'kraj','velikost_bydliste', 'ekonomicke_postaveni', 'cisty_mesicni_prijem', 'platba_bez_zkusenosti']]

#Transformace dat do tabulky
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#Provedení FT Miner procedury
clm = cleverminer(df=df,proc='4ftMiner',
                  quantifiers= {'Base':30, 'conf':0.8},
                  ante={
                      'attributes': [
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1}, #Typ proměnné je subset, protože se jedná o nominální proměnnou
                          {'name': 'vekova_kategorie', 'type': 'seq', 'minlen': 1, 'maxlen': 2}, #Typ proměnné je sequence, protože se jedná o  ordinální proměnnou
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 1}, #Typ proměnné je subset, protože se jedná o nominální proměnnou
                          {'name': 'velikost_bydliste', 'type': 'seq', 'minlen': 1, 'maxlen': 2}, #Typ proměnné je sequence, protože se jedná o  ordinální proměnnou
                          {'name': 'vzdelani', 'type': 'seq', 'minlen': 1, 'maxlen': 3}, #Typ proměnné je sequence, protože se jedná o  ordinální proměnnou
                          {'name': 'ekonomicke_postaveni', 'type': 'subset', 'minlen': 1, 'maxlen': 1}, #Typ proměnné je subset, protože se jedná o nominální proměnnou
                      ], 'minlen':2, 'maxlen':6, 'type':'con'},
                  succ={
                      'attributes': [
                          {'name': 'platba_bez_zkusenosti', 'type': 'subset', 'minlen': 1, 'maxlen': 1} #Typ proměnné je subset, protože se jedná o nominální proměnnou
                      ],
                      'minlen': 1, 'maxlen': 1, 'type': 'con'
                  }
                  )

#Vylogování shrnujících informací
clm.print_summary()
#Vylogování nalezených pravidel
clm.print_rulelist()
#Vylogování pravidla číslo 10, které je v tomto případě nejlepší vyhledané.
clm.print_rule(10)
#Zakreslení pravidla 10 do grafu.
clm.draw_rule(10)
