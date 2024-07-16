from models.Veiculo import Veiculo

class Carro(Veiculo):
       def __str__(self) -> str:
        return f"Carro:\nCor:{self.cor}\nPlaca: {self.placa}\nNúmero de rodas: {self.numero_rodas}"
