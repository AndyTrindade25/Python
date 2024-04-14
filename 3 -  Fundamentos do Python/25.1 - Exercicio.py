"""

Exercicio 5:
* Conta letras maiúsculos e minúsculas:
-> Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

* Lista números pares e ímpares de uma list:
-> Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.

"""


def contar_maiusculas_minusculas(string):
    maiuscula = 0
    minuscula = 0
    for caractere in string:
        if caractere.isupper():
            maiuscula += 1
        elif caractere.islower():
            minuscula += 1
        
    return maiuscula, minuscula
    
contar_maiusculas_minusculas("JavaScript")

print(f'Quantidade de maiusculas: {maiuscula}')
print(f'Quantidade de minusculas: {minuscula}')