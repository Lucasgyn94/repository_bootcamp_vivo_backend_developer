import psycopg2

class PostgreSQL:

    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conexao = None
    

    def connect(self):
        try:
            self.conexao = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Conexão efetuada com sucesso!")
        except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")

    def disconnect(self):
        if self.conexao :
            self.conexao.close()
            print("Conexão fechada com sucesso!")

    def cursor(self):
        if self.conexao:
            return self.conexao.cursor()
        else:
            raise Exception("Conexão não estabelecida, se conecte primeiramente")
        
    def commit(self):
        return self.conexao.commit()