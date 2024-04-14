gameName = input('Digite o nome do jogo\n')
qtdRdating = 0
totalRating = 0
rating = 0
average = 0

while(rating!= -1):
    rating = float(input('Informe a nota do jogo\n'))
    if (rating!= -1):
        totalRating += rating
        qtdRdating += 1
        average = totalRating / qtdRdating
print(f"Média das avaliações do jogo {gameName} é {average:.2f}")