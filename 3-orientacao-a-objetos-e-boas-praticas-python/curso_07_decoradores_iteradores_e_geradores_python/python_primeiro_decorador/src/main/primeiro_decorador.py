def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar!")
        funcao()
        print("Faz algo depois de executar!")
    return envelope

def ola_mundo():
    print("Olá mundo!")


# Passando função para variável
ola_mundo = meu_decorador(ola_mundo)
ola_mundo()


def mensagem(nome):
    print("Executando mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("Executando mensagem")
    return f"Olá, tudo bem com você {nome}?"


def executar(funcao, nome):
    return funcao(nome)

print(executar(mensagem, "Lucas"))
print(executar(mensagem_longa, "Lucas"))