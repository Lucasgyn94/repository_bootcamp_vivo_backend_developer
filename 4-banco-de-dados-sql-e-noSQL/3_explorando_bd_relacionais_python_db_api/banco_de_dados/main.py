import sys
sys.path.append('./')
from gerenciando_transacoes.database import PostgreSQL
from pathlib import Path
import psycopg2
from psycopg2.extras import Row


ROOT_PATH = Path(__file__).parent

conexao = PostgreSQL('clientes', 'postgres', 'carros14')
conexao.connect()
cursor = conexao.cursor()
cursor.row_factory = Row

def criar_tabela_clientes(conexao, cursor):
    try:
        cursor.execute("SELECT to_regclass('public.clientes')")
        tabela_existe = cursor.fetchone()[0] is not None

        if not tabela_existe:
            cursor.execute('''
                CREATE TABLE clientes (
                    id SERIAL PRIMARY KEY, 
                    nome VARCHAR(100), 
                    email VARCHAR(150)
                );
            ''')
            conexao.commit()
            print("Tabela 'clientes' criada com sucesso!")
        else:
            print("A tabela 'clientes' já existe.")
    except psycopg2.Error as e:
        print(f"Erro ao criar a tabela: {e}")

def inserir_cliente(conexao, cursor, nome, email):
    data = [(nome, email)]  # Lista contendo uma tupla
    cursor.execute("INSERT INTO clientes(nome, email) VALUES (%s, %s);", data[0])  # Passando a tupla individualmente
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = [(nome, email, id)]  # Lista contendo uma tupla
    cursor.execute("UPDATE clientes SET nome=%s, email=%s WHERE id=%s;", data[0])  # Passando a tupla individualmente
    conexao.commit()

def excluir_registro(conexao, cursor, id):
    data = [(id,)]  # Lista contendo uma tupla
    cursor.execute("DELETE FROM clientes WHERE id=%s;", data[0])  # Passando a tupla individualmente
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes(nome, email) VALUES (%s, %s)", dados)
    conexao.commit()

def recuperar_cliente_dict(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=%s;", (id,))
    return cursor.fetchone()  # Já retorna um dicionário

def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=%s;", (id,))
    resultado = cursor.fetchone()
    return resultado

def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome ASC;")
    return cursor.fetchall()



cliente = recuperar_cliente_dict(cursor, 2)
print(cliente)  # Imprime o dicionário diretamente
print(cliente["id"])
"""

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(cliente)

cliente = recuperar_cliente(cursor, 2)
print(cliente)
"""





#atualizar_registro(conexao, cursor, "Lucas Ferreira da Silva", "needslucas94@hotmail.com", 1)
#excluir_registro(conexao, cursor, 1)
#inserir_muitos(conexao, cursor, dados)
"""
dados = [
    ("Jose Alves", "jose@gmail.com"),
    ("Ana Maria", "maria@gmail.com"),
    ("Helena Rodrigues", "helena@gmail.com"),
]

"""
