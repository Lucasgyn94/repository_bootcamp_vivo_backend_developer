saldo = 500;


def sacar(valor) :
    global saldo;
    if (saldo >= valor) :
        saldo = saldo - valor;
        print(f'Você sacou R$ {valor} reais com sucesso!');
    else :
        print('Você não possui saldo suficiente!');

def depositar(valor): 
    global saldo;
    saldo = saldo + valor;
    print(f'Você depositou R$ {valor} reais com sucesso!');

sacar(600);
