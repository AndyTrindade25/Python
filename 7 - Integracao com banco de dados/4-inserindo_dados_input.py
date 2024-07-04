import sqlite3

connection = sqlite3.connect('title.db')

cursor = connection.cursor()

# 3 - Solicitando dados do usuário

name = input('Nome do filme\n')
year = int(input('Ano do filme\n'))
score = float(input('Nota do filme\n'))

# 4 - Inserindo dados do usuário

cursor.execute("""

                INSERT INTO movies (name, year, score)
                VALUES (?, ? , ?)

                """, (name, year, score))

# 5 - Gravando dados no BD

connection.commit()
print('Dados inseridos com sucesso!')

# 6 - Fechando a conexão

connection.close()