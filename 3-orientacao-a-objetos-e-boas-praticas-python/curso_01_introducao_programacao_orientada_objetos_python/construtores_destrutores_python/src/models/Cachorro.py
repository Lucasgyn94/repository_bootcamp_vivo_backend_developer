class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print(f'Inicializando a classe {self.__class__.__name__}')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print("au au au")

    def __str__(self):
        return f"Nome: {self.nome}, Cor: {self.cor}, Acordado: {self.acordado}"

    def __del__(self):
        print(f"Destruindo a instancia: {self.__class__.__name__}")