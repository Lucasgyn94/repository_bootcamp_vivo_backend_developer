import sys
sys.path.append('../')

from models.Motocicleta import Motocicleta
from models.Carro import Carro
from models.Caminhao import Caminhao

moto = Motocicleta("Preta", "ABC-123", 2)
print(moto)
moto.ligar_motor()
print('\n')

carro = Carro("Azul", "ABC-2240", 4)
print(carro)
carro.ligar_motor()
print('\n')

caminhao = Caminhao("Vermelho", "ABC-8890", 8, True)
print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()
