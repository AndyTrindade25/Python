gameSet = {"Fifa 23", "Red Dead 2", "Star Wars", "The Legend of Zelda",
           "Mario Odyssey", "Resident Evil 4"}

print(gameSet)

# 1 - Buscar o tamanho do set

print(len(gameSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Fifa 23", True, 1, 90.50}
print(exampleSet)

# 3 Adicionar item de outro set
gameSet.update(exampleSet)
print(gameSet)

# 4 Remover um item no set
gameSet.remove(True)
print(gameSet)
# Não possibilita recuperar valores via fatiamento ou slice