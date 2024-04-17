import hashlib


# 1 - Verificar os algoritmos disponíveis
#rint(hashlib.algorithms_available)

# 2 - Algoritmos disponiveis de acordo com o SO
#print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o Sha256
algorithm = hashlib.sha256()
message = "A melhor forma de prever o futuro é criá-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())


