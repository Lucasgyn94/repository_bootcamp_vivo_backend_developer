from models.ControleRemoto import ControleRemoto

class ControleTV(ControleRemoto):
    def ligar(self):
        print(f"{self.__class__.__name__}: ligando tv!")

    def desligar(self):
        print(f"{self.__class__.__name__}: desligando tv!")
    
    def marca(self):
        print("Lg")