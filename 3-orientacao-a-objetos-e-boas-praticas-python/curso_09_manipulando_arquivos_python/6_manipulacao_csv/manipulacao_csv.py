import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent


def escrita_arquivo_csv():
    try:
        with open(ROOT_PATH / "usuarios.csv", "w", newline='', encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["id","nome"])
            escritor.writerow(["1","Lucas"])
            escritor.writerow(["2","Maria"])
            escritor.writerow(["3","João"])
        
    except IOError as ex:
        print(f"Erro ao criar o arquivo. {ex}")

def leiura_arquivo_csv():
    try:
        with open(ROOT_PATH / "usuarios.csv", "r", newline='', encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)

    except IOError as ex:
        print(f"Erro ao criar o arquivo. {ex}")


def leitura_arquivo_csv_dict():
    try:
        with open(ROOT_PATH / "usuarios.csv", "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['id'], row['nome'])
    except IOError as ex:
        print(f"Erro ao criar o arquivo. {ex}")

leitura_arquivo_csv_dict()