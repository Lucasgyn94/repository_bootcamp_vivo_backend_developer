import datetime

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_de_data_nascimento(cls, ano_nascimento, mes_nascimento, dia_nascimento, nome):
        data_atual = datetime.datetime.now()
        ano_atual = data_atual.year

        idade = ano_atual - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18 or "É  de menor"
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"