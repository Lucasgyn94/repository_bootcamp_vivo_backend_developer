import sys
sys.path.append('../')

from models.mamifero.Cachorro import Cachorro
from models.ave.Ornitorrinco import Ornitorrinco

cachorro = Cachorro(numero_de_patas=2, cor_do_pelo="Vermelho")
print(cachorro)

ornitorrinco = Ornitorrinco(numero_de_patas=2, cor_do_pelo="Vermelho", cor_do_bico="Laranja")
print(ornitorrinco)
ornitorrinco.mensagem_animal()

ornitorrinco_2 = Ornitorrinco(numero_de_patas=2, cor_do_pelo="Laranja", cor_do_bico="Azul")
print(ornitorrinco_2)
ornitorrinco_2.mensagem_animal()
