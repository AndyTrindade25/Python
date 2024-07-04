import sqlite3

#1 - Criando o BD

connection = sqlite3.connect("title.db")

#2 - Verifica se houve alterações na base dados 
print(connection.total_changes)