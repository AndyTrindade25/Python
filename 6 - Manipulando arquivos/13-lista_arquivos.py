import glob, os, zipfile


# 1 - Diretório de trabalho atual
os.getcwd()

print(os.getcwd())
# 2 - Listar todos os arquivos .txt

for file in glob.glob("dados/*.txt"):
    print(file)


for file in glob.glob("dados/*.csv"):
    print(file)