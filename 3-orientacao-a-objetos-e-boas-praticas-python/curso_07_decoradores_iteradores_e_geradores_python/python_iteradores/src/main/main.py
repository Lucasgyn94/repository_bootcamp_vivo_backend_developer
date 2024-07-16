class IteradorArquivos:
    def __init__self(self, nome_arquivo):
        self.arquivo = open(nome_arquivo)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        linha = self.arquivo.readline()
        if linha != '':
            return linha
        else:
            self.arquivo.close()
            raise StopIteration
        

for linha in IteradorArquivos('arquivo_grande.txt'):
    print(linha)