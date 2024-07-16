from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")
except FileNotFoundError as e:
    print("Arquivo não encontrado")
    print(e)
except IsADirectoryError as e:
    print(f"Não foi possível abrir o arquivo: {e}")
except IOError as e:
    print("Erro ao abrir o arquivo: {e}")
except Exception as e:
    print("Algum problema ocorreu ao tentar abrir o arquivo: {e}")
"""
try :
    arquivo = open("meu-arquivo.py")
except FileNotFoundError as ex:
    print("Arquivo não encontrado")
    print(ex)

ROOT_PATH = Path(__file__).parent

try :
    arquivo = open("novo-diretorio")
except IsADirectoryError as e:
    print(f"Não foi possível abrir o arquivo: {e}")
"""