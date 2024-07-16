import datetime

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.__ano_nascimento = ano_nascimento

    @property
    def idade(self):
        __data_atual = datetime.datetime.now()
        __ano_atual = __data_atual.year
        return __ano_atual - self.__ano_nascimento

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'