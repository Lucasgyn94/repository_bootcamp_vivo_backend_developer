from models.animal.Animal import Animal

class Mamifero(Animal):
    
    def __init__(self, cor_do_pelo, **kw):
        self.cor_do_pelo = cor_do_pelo
        super().__init__(**kw)
