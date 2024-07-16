class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Au Au Au")

    def dormir(self):
        self.acordado = False
        print("Zzzzzz....")

    def __str__(self):
        return f"nome: {self.nome}, cor: {self.cor}, acordado:"