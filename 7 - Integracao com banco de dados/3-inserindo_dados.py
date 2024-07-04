import sqlite3

#1 - Conectando no DB

connection = sqlite3.connect('title.db')

# 2 - Criando um cursor


cursor = connection.cursor()

# 3 - Inserindo dados

cursor.execute("""

                INSERT INTO movies (name, year, score)
                VALUES ('Super Mario Bross', '2023', 10)
                """)


cursor.execute("""

                INSERT INTO movies (name, year, score)
                VALUES ('Avatar', '2025', 9.5)
                """)

cursor.execute("""

                INSERT INTO movies (name, year, score)
                VALUES ('Velozes e furiosos', '2021', 9.4)
                """)


connection.commit()

print('Dados inseridos com sucesso!')
connection.close()