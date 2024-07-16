import sys
sys.path.append('../')

from models.Pardal import Pardal
from models.Avestruz import Avestruz
from models.Aviao import Aviao

def plano_de_voo(passaro):
    passaro.voar()

pardal = Pardal()
plano_de_voo(pardal)

avestruz = Avestruz()
plano_de_voo(avestruz)

aviao = Aviao()
plano_de_voo(aviao)