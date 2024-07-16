import sys
sys.path.append('./')
from database import PostgreSQL
from pathlib import Path
import psycopg2
from psycopg2.extras import Row


ROOT_PATH = Path(__file__).parent

conexao = PostgreSQL('clientes', 'postgres', 'carros14')
conexao.connect()
cursor = conexao.cursor()
cursor.row_factory = Row

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?,)", ("teste 3", "teste3@gmail.com"))
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?,)", ("teste 4", "teste4@gmail.com"))
    conexao.commit()
except Exception as ex:
    print(f"OPS! Um erro ocorreu! {ex}")
    conexao.rollback()