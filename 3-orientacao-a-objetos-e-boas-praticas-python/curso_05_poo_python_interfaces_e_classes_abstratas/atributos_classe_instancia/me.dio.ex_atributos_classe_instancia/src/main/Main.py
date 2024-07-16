
import sys
sys.path.append('../')

from models.Estudante import Estudante

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# variaveis de instancia
aluno_1 = Estudante("Lucas", 1)
aluno_2 = Estudante("Maria", 2)
mostrar_valores(aluno_1, aluno_2)
print('\n')
# variaveis de classe
Estudante.escola = 'Python'
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)