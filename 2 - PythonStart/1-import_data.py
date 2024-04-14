import pandas as pd

#1 - Importando dados
data = pd.read_excel('./VendaCarros.xlsx')

#2 - Registre os primeiros 5 registros
#print(data.head())


#3 - Registre os 5 ultimos registros
#print(data.tail())

#4 - Trazendo apenas determinada coluna
print(data["Fabricante"].value_counts())