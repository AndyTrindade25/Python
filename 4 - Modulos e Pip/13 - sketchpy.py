import os
from pathlib import Path
from sketchpy import library as lib

# Constrói o caminho para o arquivo data.txt no diretório home do usuário
data_file_path = Path(os.getenv('anderson')) / 'data.txt'

# Usa a biblioteca sketchpy
object = lib.rdj()
object.draw()
