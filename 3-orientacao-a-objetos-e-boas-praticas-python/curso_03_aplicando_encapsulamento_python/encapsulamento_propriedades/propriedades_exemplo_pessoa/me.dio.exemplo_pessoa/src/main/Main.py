import sys
sys.path.append('../')

from models.Pessoa import Pessoa

p1 = Pessoa("Lucas",1994)
print(f'Pessoa: {p1}')
