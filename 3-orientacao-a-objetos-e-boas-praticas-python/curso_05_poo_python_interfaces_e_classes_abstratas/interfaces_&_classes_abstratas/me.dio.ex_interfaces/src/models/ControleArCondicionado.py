from models.ControleRemoto import ControleRemoto

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print(f"{self.__class__.__name__}: ligando ar condicionado!")

    def desligar(self):
        print(f"{self.__class__.__name__}: desligando ar condicionado!")

    def marca(self):
        print("Samsung")