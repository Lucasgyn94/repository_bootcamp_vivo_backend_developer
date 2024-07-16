from models.Veiculo import Veiculo

class Motocicleta(Veiculo):
        def __str__(self) -> str:
            return f"Motocicleta:\nCor:{self.cor}\nPlaca: {self.placa}\nNúmero de rodas: {self.numero_rodas}"

