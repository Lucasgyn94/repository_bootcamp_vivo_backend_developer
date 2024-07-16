import sys
sys.path.append('../')

from models.Cachorro import Cachorro

cao_1 = Cachorro("Tampinha", "Amarelo", False)
print(cao_1)
cao_1.falar()

del cao_1