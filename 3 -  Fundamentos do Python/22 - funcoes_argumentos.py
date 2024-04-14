# 1 - Crie uma função que receba dois argumentos: o primerio nome e o segundo nome
# def full_name(fname, lname):
#     print(f"Nome completo: {fname} {lname}")
    
# full_name("Anderson", "Trindade")


# 2 - Crie uma função que some dois números via parâmetros

# def sum(a, b):
#     print(a + b)
    
# sum(5, 5)


# 3 - Argumentos default numa função

# def address(country="Brasil"):
#     print(f'Eu moro no {country}')
    
    
# address("Estados Unidos")

# 4 Avaliação do jogo

def rating_game(qtdRating):
    game_name = input('Digite o nome do jogo')
    sum = 0
    for i in range(qtdRating):
        
        note = int(input(f'Digite a nota do jogo - {i}\n'))
        sum += note
    print(f'Média de avaliação do jogo {game_name} é {sum/qtdRating}')

rating_game(5)