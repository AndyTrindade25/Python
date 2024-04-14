# 1 - Funcao para imprimir Hello Word
# def welcome():
#     print('Hello World!')
    
    
# welcome()
# welcome()
# welcome()

# 2 - Funcao para somar dois numeros
# def sum(x):
#     print(5 + x)
    
    
# sum(4)

# 3 - Funcao para cadastrar um jogo
def create_game():
    name = input('Digite o nome do jogo\n')
    yearnLaunch = int(input('Digite o ano de lancamento do jogo\n'))
    gamePrice = float(input('Digite o preco do jogo\n'))
    noteRating = float('Digite a nota de avaliacao do jogo?\n')
    
    print('f{name} - R$ {gamePrice}')
    
create_game()