# -*- coding: utf-8 -*-
"""
*args - Utilizamos ele quando nao temos certeza de quantos argumentos queremos ter numa funcao.
- Os argumentos asao passados como  uma tupla

**kwargs - além dos valores podemos passar tambem as respectivas chaves para cada argumento.
- Os argumentos sao passados como um dicionario

"""

# # 1 - Soma de numeros
# def sum(*num):
#     sum_total = 0
#     for i in num:
#         sum_total += i
#     print(f"Soma é: {sum_total}")

# sum(7, 5, 3)  # Exemplo com múltiplos números


# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f'{key} - {value}')

presentation(name="Python", category="backend", level="Iniciante")
print('#')
presentation(name="Dashboards com Dash", category="Data Science", level="Intermediário")
print('#')
presentation(name="Visão Computacional com Python", category="IA", level="Avançado")

