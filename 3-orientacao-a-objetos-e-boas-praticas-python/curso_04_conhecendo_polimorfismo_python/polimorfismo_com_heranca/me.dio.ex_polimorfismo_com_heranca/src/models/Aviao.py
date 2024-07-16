from models.Passaro import Passaro

# EXEMPLO RUIM DO USO DE HERANÇA
class Aviao(Passaro):
    def voar(self):
        print("Avião decolando!")