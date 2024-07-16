import sys
sys.path.append('../')

from models.Cachorro import Cachorro

cao_1 = Cachorro("Tampinha", "Amarelo", False)
print(cao_1)

cao_2 = Cachorro("Aladim", "Branco e preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)
