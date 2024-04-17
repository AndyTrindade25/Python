import statistics

# 1 - Aplicar a média
print(f"{statistics.mean([5, 10, 6, 7, 10, 9, 10])}")

# 2 - Aplicar a mediana
print(statistics.median([1, 2, 3, 4, 5, 6]))

print(statistics.median([1, 2, 4, 5, 9, 8]))

# 4 - Aplicar a moda
print(statistics.mode([2, 5, 6, 7, 7, 7,5, 4, 3, 2, 1]))


# 4 - Desvio padrão


"""
Quanto mais próximo de 0 for o desvio padrão,
significa que os dados do conjunto estão menos dispersos.

"""
print(statistics.stdev([1, 1.5, 2, 5, 7]))