from conexao_post import conn


cursor = conn.cursor()

sql = "DELETE FROM game WHERE id = %s"

cursor.execute(sql, (6,))

conn.commit()

print('Dado removido com sucesso!')

conn.close()