# Escrever 10, 9, 8,
#import winsound

number = 10
while number != 0:
    print(number)
    number -= 1
    
print(0)
#winsound.Beep(2500, 500)

# Tabuada 

numberTabuada = int(input('Escreva abaixo o número para mostrar a tabuada\n'))

vezesTabuada = int(input("Até quantas vezes deseja multiplicar"))

resultadoTabuada = 0
for i in range(vezesTabuada+1):
    resultadoTabuada = numberTabuada * i
    print(f"{numberTabuada} x {i} = {resultadoTabuada}")