import sqlite3

connection = sqlite3.connect('title.db')

cursor = connection.cursor()

# Solicitando dados do usuário
id = int(input('Informe o ID do filme que deseja remover\n'))

cursor.execute('DELETE FROM movies WHERE id = ?', (id,))

connection.commit()
print('Filme removido com sucesso!')

connection.close()