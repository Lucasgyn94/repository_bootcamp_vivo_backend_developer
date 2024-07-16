# Criação de listas
frutas = [];

frutas = ["Laranja", "Maça", "Uva"];

letras = list("Python");
print(letras);

numeros = list(range(10));
print(numeros);

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True];

# Acesso a lista
frutas = ["Maça","Laranja", "Uva", "Pera"];
print(frutas[0]); # maça
print(frutas[2]); # Uva

print(frutas[-1]) #pera
print(frutas[-3]) # laranja

# Lista aninhadas
# Matriz 
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0]; #  [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # c

# Fatiametnto

lista = ["p", "y", "t", "h", "o", "n"];

lista[2:] # ["t", "h", "o", "n"]
lista[: 2] # ["p", "y"]
lista[1: 3] # ["y", "t"];
lista[0: 3: 2] # ["p", "t"];
lista[: : ] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]

#ITERAÇÃO LISTAS
carros = ["gol", "celta", "palio"];

for carro in carros:
    print(carro);

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}");

# Compreensão de listas
numeros = [1, 30, 21, 2, 9, 65, 34];
pares = [];

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero);

# filtro versão 2
numeros = [1, 30, 21, 2, 9, 65, 34];
pares = [numero for numero in numeros if numero % 2 == 0];

# modificando valores
numeros = [1, 30, 21, 2, 9, 65, 34];
quadrado = [];
for numero in numeros:
    quadrado.append(numero ** 2);

# modificando versão 2
numeros = [1, 30, 21, 2, 9, 65, 34];
quadrado = [];

quadrado = [numero ** 2 for numero in numeros];