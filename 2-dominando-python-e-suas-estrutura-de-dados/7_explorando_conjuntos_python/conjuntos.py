print(set([1, 2, 3, 1, 3, 4]));
print(set("abacaxi"));
print(set(("palio", "gol", "celta", "palio")));

linguagens = {"python", "java", "python"};
print(linguagens);

## Acessando os dados
numeros = {1, 2, 3, 2};
numeros = list(numeros);
print(numeros[1]);

## Iteração

carros = {"gol", "celta", "palio"};

for carro in carros:
    print(carro);

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}");

## Metodos da classe set
conjunto_a = {1, 2};
conjunto_b = {3, 4};
uniao = conjunto_a.union(conjunto_b);
print(f'União: {uniao} ');

conjunto_a = {1, 2, 3};
conjunto_b = {2, 3, 4};

interseccao = conjunto_a.intersection(conjunto_b);
print(f'Intersecção: {interseccao}');

conjunto_a = {1, 2, 3};
conjunto_b = {2, 3, 4};

diferenca_a = conjunto_a.difference(conjunto_b);
diferenca_b = conjunto_b.difference(conjunto_a);

print(f'Diferença conjunto a de b: {diferenca_a}');
print(f'Diferença conjunto b de a: {diferenca_b}');

conjunto_a = {1, 2, 3};
conjunto_b = {2, 3, 4};

diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b);
print(f'Diferença simetric a de b: {diferenca_simetrica}');

conjunto_a = {1, 2, 3};
conjunto_b = {4, 1, 2, 5, 6, 3};

issubset_a = conjunto_a.issubset(conjunto_b);
issubset_b = conjunto_b.issubset(conjunto_a);

print(f'Conjunto a é subconjunto de b: {issubset_a}');
print(f'Conjunto b é subconjunto de a: {issubset_b}');

conjunto_a = {1, 2, 3};
conjunto_b = {4, 1, 2, 5, 6, 3};

issuperset_a = conjunto_a.issuperset(conjunto_b);
issuperset_b = conjunto_b.issuperset(conjunto_a);

print(f'Conjunto a é superconjunto de b: {issuperset_a}');
print(f'Conjunto b é superconjunto de a: {issuperset_b}');

conjunto_a = {1, 2, 3, 4, 5};
conjunto_b = {6, 7, 8, 9};
conjunto_c = {1, 0};

isdisjoint_a = conjunto_a.isdisjoint(conjunto_b);
isdisjoint_c = conjunto_a.isdisjoint(conjunto_c);

print(f'Conjunto a é disjunto de b: {isdisjoint_a}');
print(f'Conjunto a é disjunto de c: {isdisjoint_c}');

# adicionando elementos

sorteio = {1, 23};

sorteio.add(25);
sorteio.add(42);
sorteio.add(25);
print(f'sorteio: {sorteio}');

# limpadndo elemetos

sorteio = {1, 23};
print(f'sorteio: {sorteio}');
sorteio.clear();
print(f'sorteio: {sorteio}');

## copiando elementos

sorteio = {1, 23};
print(f'sorteio: {sorteio}');
sorteio_copia = sorteio.copy();
print(f'sorteio: {sorteio}');
print(f'sorteio_copia: {sorteio_copia}');

# Discartando valores
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0};
print(f'numeros: {numeros}');
numeros.discard(1);
numeros.discard(45);
print(numeros);

# Removendo elementos

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0};
print(f'numeros: {numeros}');
numeros.pop();
numeros.pop();
print(numeros);

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0};
print(f'Removendo primeiro elemento');
numeros.remove(0)
print(f'Removendo o número 5');
numeros.remove(5);
print(f'numeros: {numeros}');

## Tamanho do conjunto

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0};
print(f'Tamanho do conjunto: {len(numeros)}');

## verifica se dentro do conjunto

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0};
print(1 in numeros);
print(10 in numeros);

## Iterando em conjuntos