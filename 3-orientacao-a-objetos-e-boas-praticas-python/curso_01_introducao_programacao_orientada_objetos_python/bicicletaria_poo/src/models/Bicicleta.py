class Bicicleta:
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 1
    
    def buzinar(self):
        print('Bi Bi')

    def parar(self):
        print('Freando')
    
    def correr(self):
        print('correndo')

    def trocar_marcha(self, numero_marcha):
        print('Trocando Marcha')
        # pass

        def trocar_coroa_marcha():
            if numero_marcha > self.marcha:
                self.marcha += 1;
                print(f'Trocado para {numero_marcha} marcha...')
            else:
                print('Marcha não pode ser trocada...')

    
    # def __str__(self):
    #     return f"cor: {self.cor}, modelo: {self.modelo}, ano: {self.ano}, valor: {self.valor}"
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"
