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
dfSelected=df[['vekova_kategorie','vzdelani', 'pohlavi', 'kraj', 'velikost_bydliste', 'politicke_preference', 'hodnoceni_ceskeho_zdravotnictvi']]

#Transformace dat do tabulky
imputer = SimpleImputer(strategy="most_frequent")
dfSelected = pd.DataFrame(imputer.fit_transform(dfSelected),columns = dfSelected.columns)

#Provedení SD4FT Miner procedury
clm = cleverminer(df=df,proc='SD4ftMiner',
                  quantifiers= {'Base1':10,'Base2':10, 'Ratioconf':1.5},
                  ante ={
                      'attributes':[
                          {'name': 'vekova_kategorie', 'type': 'seq', 'minlen': 1, 'maxlen': 2}, #Typ proměnné je sequence, protože se jedná o  ordinální proměnnou.
                          {'name': 'vzdelani', 'type': 'seq', 'minlen': 1, 'maxlen': 2}, #Typ proměnné je sequence, protože se jedná o  ordinální proměnnou.
                          {'name': 'kraj', 'type': 'subset', 'minlen': 1, 'maxlen': 2}, #Typ proměnné je subset, protože se jedná o nominální proměnnou.
                          {'name': 'velikost_bydliste', 'type': 'seq', 'minlen': 1, 'maxlen': 2}, #Typ proměnné je sequence, protože se jedná o  ordinální proměnnou.
                          {'name': 'politicke_preference', 'type': 'subset', 'minlen': 1, 'maxlen': 1}, #Typ proměnné je subset, protože se jedná o nominální proměnnou.
                      ], 'minlen':1, 'maxlen':4, 'type':'con'},
                  succ ={
                      'attributes':[
                          {'name': 'hodnoceni_ceskeho_zdravotnictvi', 'type': 'rcut', 'minlen': 1, 'maxlen': 2} #Typ proměnné je RCut, protože chceme získat z hodnocení pouze negatvní hodnoty. (hodnocení 4,5).
                      ], 'minlen':1, 'maxlen':1 , 'type':'con'},
                  frst ={
                      'attributes':[
                          {'name': 'pohlavi', 'type': 'one', 'value':'Muž'} #Typ proměnné je one, používá se protože potřebujeme pouze konkrétní hodnotu.
                      ], 'minlen':1, 'maxlen':1, 'type':'con'},
                  scnd ={
                      'attributes':[
                          {'name': 'pohlavi', 'type': 'one', 'value':'Žena'} #Typ proměnné je one, používá se protože potřebujeme pouze konkrétní hodnotu.
                      ], 'minlen':1, 'maxlen':1, 'type':'con'}
                  #               ,opts = {'no_optimizations':True,'max_categories':20}
                  )
#Vylogování shrnujících informací
clm.print_summary()
#Vylogování nalezených pravidel
clm.print_rulelist()
#Vylogování pravidla číslo 15.
clm.print_rule(15)
#Zakreslení pravidla 15 do grafu.
clm.draw_rule(15)