texto = input("Informe um texto: ");
VOGAIS = 'AEIOU';

# exemplo iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(f'{letra}', sep="-");
else:
    print();

# exemplo utilizando a função built-in range.
for numero in range(0, 51, 5):
    print(numero, end=" ");
