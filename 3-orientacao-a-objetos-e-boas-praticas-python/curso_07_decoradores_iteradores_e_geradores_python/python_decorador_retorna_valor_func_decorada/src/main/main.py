def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar!")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar!")
        return resultado
    return envelope
    
@meu_decorador
def ola_mundo(nome, outro_argumento):
    print("Olá mundo {nome}!")
    return nome.upper()


resultado = ola_mundo("Lucas", 10000)
print(resultado)
