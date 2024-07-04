import sqlite3

connection = sqlite3.connect('title.db')

cursor = connection.cursor()

# Solicitando dados do usuário

id = int(input('Informe o ID do filme que deseja atualizar\n'))
name = input('Informe o novo nome do filme\n')


# Atualizando os dados

cursor.execute("""
                UPDATE movies SET name = ?
                WHERE id = ?
              """, (name, id))

connection.commit()

print("Dados atualizados com sucesso!")


connection.close()