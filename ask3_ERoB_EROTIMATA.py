from wsgiref import headers
import pandas as pd
import numpy as np
from tabulate import tabulate ## apla gia na ta tiponi pio oraia ## just to print it nicer...
import matplotlib.pyplot as plt
from ask3_ERoB_CREATE_DATAFRAME_CSV import list_prices ## import list_grades so we can use it in the diagram
from ask3_ERoB_CREATE_DATAFRAME_CSV import list_rams ## import to list_rams gia na to xristimopioso gia to diagramma ## 

df = pd.read_csv('DATA_CSV.csv', na_values='NaN', keep_default_na=False) ## open the csv file

##headers = ['ID', 'Title', 'Price', 'Kodikos Plaisio', 'RAM']
##print(tabulate(df, headers, tablefmt="github"))


COUNT_NULL_VALUES = np.count_nonzero(df.isnull().values) ## here we get the number of the nulls /// it is 0  
print("NUMBER OF NULL VALUES --> ", COUNT_NULL_VALUES)
print("PERCENTAGE OF NULL VALUES --> ", str(COUNT_NULL_VALUES) + '%') 

## TO EROTIMA 3 DEN MPORO NA TO KANO DEN EXO NULL TIMES...

## CONVERT TA LIST ME TIS TIMES (POU EINAI SAN STING) STIS IDIES LIST ALLA ME INTEGERS ANTI GIA STRINGS... --> MALLON DEN XRIAZETAI, AFORA TIN 33 LINE
for i in range(0, len(list_prices)):
    list_prices[i] = int(list_prices[i])
    if i == 11:
        break
del list_prices[-1] ## apla gia na diarazi to telaiutaio item stin lista pou gia kapoion logo einai apla ena keno mas to xala giati prepi na ne idio megethos kai oi dio listes oste na ta baloume sto diagramma

for i in range(0, len(list_rams)):
    list_rams[i] = int(list_rams[i])
    if i == 11:
        break

##plt.scatter(list_prices, list_rams, c="blue") ## ERORIMA 4 --> APLA EDO DIABAZI APO TIS LISTES ME TA RAMS KAI TA PRICES KAI FTIAXNI TO DIAGRAMMA
##plt.show()

df.plot(kind = 'scatter', x = 'Price', y = 'RAM') ## here it reads the  csv file and creates the diagram
plt.show()
