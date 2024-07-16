arquivo = open('./lorem.txt', 'r')

def leitura_read(arquivo):
    print('\nleitura READ\n')
    print(arquivo.read())
    arquivo.close()

def leitura_readline(arquivo):
    print("\nleitura READLINE\n")
    print(arquivo.readline())
    arquivo.close()

def leitura_readlines(arquivo):
    print('\nLeitura READLINES\n')
    print(arquivo.readlines())
    arquivo.close()



while len(linha := arquivo.readlines()):
    print(linha)

#leitura_read(arquivo)
#leitura_readlines(arquivo)
#leitura_todas_linhas(arquivo)
#leitura_primeira_linha(arquivo)