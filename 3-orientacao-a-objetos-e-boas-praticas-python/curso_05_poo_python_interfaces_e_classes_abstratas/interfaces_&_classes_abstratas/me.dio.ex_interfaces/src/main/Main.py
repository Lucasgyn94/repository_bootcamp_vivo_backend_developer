import sys
sys.path.append('../')

from models.ControleTV import ControleTV
from models.ControleArCondicionado import ControleArCondicionado


controle_tv = ControleTV()
controle_tv.ligar()
controle_tv.desligar()
controle_tv.marca()

controle_ar = ControleArCondicionado()
controle_ar.ligar()
controle_ar.marca()
