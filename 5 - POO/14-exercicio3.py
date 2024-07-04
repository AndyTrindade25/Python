from exercicio3 import Trip

trip0 = Trip("São Paulo")
trip1 = Trip("Rio de Janeiro")
trip2 = Trip("Belo Horizonte")
trip3 = Trip("Curitiba")
trip4 = Trip("Porto Alegre")

print("Eae vianjante, temos algumas ofertas para você.")
travaler = input("Digite o seu nome para começar\n ")
print(f"Olá, {travaler}! Temos 5 destinos para você, escolha um deles."
      '''

        [0] - São Paulo
        [1] - Rio de Janeiro
        [2] - Belo Horizonte
        [3] - Curitiba
        [4] - Porto Alegre

      '''
    )

choice = int(input("Selecione um destino\n"))
list_of_trips = [trip0, trip1, trip2, trip3, trip4]

for option in list_of_trips:
    if choice >= 5:
        print("Opção inválida")
        break
    else:
        print(f"Você escolheu {list_of_trips[choice].destiny}!")
        print("Boa viagem!!")
        break