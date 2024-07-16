# funcoes com parametros especiais
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(f"Carro inserido com sucesso!\n{marca}/ {modelo}/ {ano} / {placa} / {motor} / {combustivel}");

#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor=1.0, combustivel="Gasolina"); # valido
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor=1.0, combustivel="Gasolina"); # invalido
#criar_carro("Gol", 1998, "ABC-1234", "Wolkswagen", 1.0, "Gasolina");


# Somente por posição Keyword Only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(f"Carro inserido com sucesso!\n{marca}/ {modelo}/ {ano} / {placa} / {motor} / {combustivel}");

#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor=1.0, combustivel="Gasolina"); # valido
#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor = "1.0", combustivel="Gasolina") # invalido

# FORMA HIBRIDA POR POSIÇÃO E PARAMETROS NOMEADOS
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(f"Carro inserido com sucesso!\n{marca}/ {modelo}/ {ano} / {placa} / {motor} / {combustivel}");

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor=1.0, combustivel="Gasolina"); # valido
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor=1.0, combustivel="Gasolina"); # invalido

# OBJETOS DE PRIMEIRA CLASSE
def somar(a, b):
    return a + b;

def subtrair(a, b):
    return a - b;


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b);
    if (funcao == somar):
        print(f"{a} + {b} = {resultado}");
    elif (funcao == subtrair):
        print(f"{a} - {b} = {resultado}");

def test(a, b):
    return a * 2 + b * 3;

#exibir_resultado(10, 20, somar);
#exibir_resultado(20, 10, subtrair);
#print(test(2, 2));

#operacao = somar;
#print(operacao(10, 20));

# ESCOPO LOCAL E ESCOPO GLOBAL
salario = 2000;

def salario_bonus(bonus):
    global salario;
    salario += bonus;
    return salario, bonus;

print(salario_bonus(500));