from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "lorem.txt", 'r') as arquivo:
        print(arquivo.read())
except IOError as ex:
    print(f"Erro ao abrir o arquivo {ex}")


try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Aprendendo a manipular arquivos utilizando python.")
except IOError as ex:
    print(f"Erro ao abrir o arquivo {ex}")

"""
try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as ex:
    print(f"Erro ao abrir o arquivo {ex}")
except UnicodeDecodeError as ex:
    print(ex)
"""