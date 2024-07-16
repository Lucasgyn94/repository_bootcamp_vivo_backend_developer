# Criação de tuplas
frutas = ("laranja", "pera", "uva",);
print(frutas);

letras = tuple("python");
print(letras);

numeros = tuple([1, 2, 3, 4]);
print(numeros)

pais = ("Brasil",);
print(pais);

# Acesso Direto
frutas = ("maça", "laranja", "uva", "pera",);
print(frutas[0]); # maça
print(frutas[2]); # uva

#Indíces negativos
frutas = ("maça", "laranja", "uva", "pera",);
print(frutas[-1]);
print(frutas[-3]);

# Tuplas aninhadas
tupla = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)
print(tupla[0]);
print(tupla[0][0]);
print(tupla[0][-1]);
print(tupla[-1][-1]);

# Fatiamento
tupla = ("p", "y", "t", "h", "o", "n");
print(tupla[2:]);
print(tupla[: 2]);
print(tupla[1: 3]);
print(tupla[0: 3: 2]);
print(tupla[: : ]);
print(tupla[::-1]);

# Iteração tuplas
carros = ("gol", "celta", "palio");

for carro in carros:
    print(carro);

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}");