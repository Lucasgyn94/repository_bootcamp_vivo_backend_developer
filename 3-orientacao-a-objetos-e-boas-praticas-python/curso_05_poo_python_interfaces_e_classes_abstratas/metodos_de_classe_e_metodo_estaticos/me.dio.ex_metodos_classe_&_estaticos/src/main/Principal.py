import sys
sys.path.append('../')

from models.Pessoa import Pessoa

p = Pessoa.criar_de_data_nascimento(1994, 8, 5, "Lucas")
print(p.nome, p.idade)

print(Pessoa.e_maior_de_idade(p.idade))
print(Pessoa.e_maior_de_idade(17))
