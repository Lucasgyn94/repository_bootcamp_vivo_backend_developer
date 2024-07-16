import sys
sys.path.append('../')

from models.Conta import Conta

conta = Conta("0001")
conta.depositar(100)
conta.sacar(50)
print(conta)
conta.exibir_saldo()