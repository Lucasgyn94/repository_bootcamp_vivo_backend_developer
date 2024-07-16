MAIOR_IDADE = 18;
IDADE_ESPECIAL = 12;

idade = int(input("Digite a sua idade: "));



if (idade >= MAIOR_IDADE):
    print("Você pode tirar sua CNH!");
if (idade <= MAIOR_IDADE) : 
    print("Você não pode tirar sua CNH!");

if (idade >= MAIOR_IDADE):
    print("Você pode tirar sua CNH!");
else:
    print("Você não pode tirar sua CNH!");

if (idade >= MAIOR_IDADE):
    print("Você pode tirar sua CNH!");
elif idade == IDADE_ESPECIAL:
    print("Você não pode tirar sua CNH!");
else:
    print("Você não pode tirar sua CNH!");