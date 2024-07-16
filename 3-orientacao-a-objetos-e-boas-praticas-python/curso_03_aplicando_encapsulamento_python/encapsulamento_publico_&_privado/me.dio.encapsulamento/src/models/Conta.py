class Conta:
    __CONTA = 1
    __SALDO = 0

    def __init__(self, numero_agencia):
        self.__numero_agencia = numero_agencia
        self.__CONTA += 1
        
    def depositar(self, valor):
        if valor >= 0:
            self.__SALDO += valor
        else:
            print("Valor inválido")
    
    def sacar(self, valor):
        if valor <= self.__SALDO:
            self.__SALDO -= valor
        else:
            print("Saldo insuficiente")
    
    def exibir_saldo(self):
        print(f'Saldo Atual: R${self.__SALDO}')

    def __str__(self):
        return f"Agencia: {self.__numero_agencia}\nConta: {self.__CONTA}\nSaldo: {self.__SALDO}"
    
