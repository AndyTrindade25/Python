#Exercicio para ler as duas primeiras linhas do arquivo

def file_read_from_line(filename, nlines):
    from itertools import islice
    with open(filename, 'r') as file:
        for line in islice(file, nlines):
            print(line)


file_read_from_line("dados/motivation.txt", 2)