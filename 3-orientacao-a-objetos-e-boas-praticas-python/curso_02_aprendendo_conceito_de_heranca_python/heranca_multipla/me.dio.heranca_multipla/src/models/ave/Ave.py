from models.animal.Animal import Animal

class Ave(Animal):
    def __init__(self, cor_do_bico, **kw):
        self.cor_do_bico = cor_do_bico
        super().__init__(**kw)

