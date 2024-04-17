import random

done = False

while not done:
    print("O que você deseja fazer?")
    print("1. Adivinhar o número")
    print("2. Sair")
    
    choice = input(">")
    
    if choice == "1":
        print("===== Advinhe um número de 1 a  10 ======\n")
        number = int(input('Digite o número de 1 a 10\n'))
        result = random.randint(1, 3)
        if number == result:
            print(f'Parabéns!!!!!!!!!!!!!!, vocẽ acertou o número é {result}')
        else:
            print(f"Tente novamente. O número sorteado foi {result}")
    elif choice == "2":
        done = True
        print('Você saiu do jogo')
    else:
        print("Opção inválida")