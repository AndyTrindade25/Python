# 1 - Liste valores de 0 a 10 que sejam menor do que 4.
# for i in range(10):
#     if i < 4:
#         print(i)


# listNumbers = [i for i in range(10) if 1 < 4]
# print(listNumbers)

gameList = ["Mario Odyssey", "Dk Country",
            "Luigis Mansion", "Kirby"]

# 2 - Jogos que possuam a Letra A

# newList = [x for x in gameList if "a" in x]
# print(newList)


gamesFinished = [ x for x in gameList if x != 'Kirby']
print(gamesFinished)