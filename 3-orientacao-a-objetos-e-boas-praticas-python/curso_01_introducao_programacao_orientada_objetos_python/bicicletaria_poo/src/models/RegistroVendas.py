class RegistroVendas:
    def __init__(self):
        self.vendas = []

    def registrar_venda(self, bicicleta):
        self.vendas.append(bicicleta)

    def listar_vendas(self):
        print("Histórico de Vendas")
        for index, bibicicleta in enumerate(self.vendas, start=1):
            print(f"{index} - {bibicicleta}")
    