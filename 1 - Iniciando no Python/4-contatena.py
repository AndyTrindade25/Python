# Utilizando o Input
'''
Comentário multi linha
'''

name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
gamePrice = float(input('Digite o preço do jogo\n'))
planIncluded = input('Está incluso o serviço mensal?\n')

print("#### Dados do Jogo ####")
print('########################')
print('Nome do jogo', name)
print(f'Ano do jogo: {yearLaunch}')
print(f'Preço do jogo: {gamePrice}')
print(f'Está incluído no plano? {planIncluded}')