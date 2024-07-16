class Animal:
    def __init__(self, numero_de_patas):
        self.numero_de_patas = numero_de_patas

    def mensagem_animal(self):
        print(f'Eu sou um {self.__class__.__name__}')


    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"