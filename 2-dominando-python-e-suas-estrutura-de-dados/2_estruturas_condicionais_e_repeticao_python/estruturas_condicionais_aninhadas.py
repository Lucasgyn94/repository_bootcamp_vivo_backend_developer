contar_normal = True;
conta_universitaria = False;

saldo = 2000;
saque = 500;
cheque_especial = 450;

if contar_normal:
    if saldo >= saque:
        print(f'Você sacou R$ {saque} reais com sucesso!');
    elif saque <= (saldo + cheque_especial):
        print(f'Você sacou R$ {saque} reais com sucesso com uso do cheque especial!');
    else:
        print('Você não possui saldo suficiente!');

elif conta_universitaria:
    if saldo >= saque:
        print(f'Você sacou R$ {saque} reais com sucesso!');
    else:
        print('Você não possui saldo suficiente!');