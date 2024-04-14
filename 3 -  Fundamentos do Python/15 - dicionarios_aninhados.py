import pprint

gamesDict = {
    "Resident Evil 4": {
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre": ["ação", "aventura"]
    },
    "Mario Odyssey": {
        "yearLaunch": 2017,
        "classification": 10.0,
        "genre": ["aventura", "3d"]
    },
    "Donkey Kong Country": {
        "yearLaunch": 1995,
        "classification": 9.5,
        "genre": ["aventura", "plataforma"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
#pp.pprint(gamesDict)

# 1 - Buscar informações dentro de um dicionário aninhado
#print(gamesDict["Mario Odyssey"]["genre"])

# 2 - Adicionar novo item
#gamesDict["Mario Odyssey"]["players"] = 1
#pp.pprint(gamesDict["Mario Odyssey"])

# 3 - Excluir um dicionário
del gamesDict["Resident Evil 4"]
pp.pprint(gamesDict)
