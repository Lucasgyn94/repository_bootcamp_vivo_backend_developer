import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / "novo-diretorio")

# Criando arquivo
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# Renomeando arquivo
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Remover arquivo
os.remove(ROOT_PATH / "alterado.txt")

# Movendo arquivo
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
