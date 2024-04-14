import pandas as pd

#1 - Importando dados
data = pd.read_excel('./data/VendaCarros.xlsx')

df = data[["Fabricante", "ValorVenda", "Ano"]]
#print(df)

#3 - Criando tabela pivô

pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)


pivot_table.to_excel("data/pivot_table.xlsx", "Relatorio")