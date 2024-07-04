import sqlite3

connection = sqlite3.connect('title.db')

cursor = connection.cursor()

# Lendo dados na tabela
# data = cursor.execute('SELECT * FROM movies')

# print(data.fetchall())
# connection.close()


# Iterando os dados

for row in cursor.execute('SELECT * FROM movies'):
    print(row)


# Ordenando os dados pelo score

for row in cursor.execute('SELECT * FROM movies ORDER BY score DESC'):
    print(f'{row}')


connection.close()