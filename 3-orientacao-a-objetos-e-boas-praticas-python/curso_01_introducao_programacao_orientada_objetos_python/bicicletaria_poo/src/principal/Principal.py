import sys
sys.path.append('../')

from models.Bicicleta import Bicicleta
from models.RegistroVendas import RegistroVendas

b1 = Bicicleta("amarela", "caloi", 2024, 3000)
b2 = Bicicleta("Preto Fosco", "GTSM1", 2024, 3200)
b1.trocar_marcha(2)
b2.correr()

registro = RegistroVendas()
registro.registrar_venda(b1)
registro.registrar_venda(b2)
print(f'Registro de Vendas: {registro.listar_vendas()}')
