from models.ave.Ave import Ave
from models.mamifero.Mamifero import Mamifero

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_do_bico, cor_do_pelo, numero_de_patas):
        #print(Ornitorrinco.__mro__)
        print(Ornitorrinco.mro())
        super().__init__(cor_do_pelo=cor_do_pelo, cor_do_bico=cor_do_bico, numero_de_patas=numero_de_patas)
