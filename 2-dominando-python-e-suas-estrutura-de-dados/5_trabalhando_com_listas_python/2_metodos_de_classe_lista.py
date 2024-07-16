lista = [];

#Adicionando elementos
lista.append(1);
lista.append("python");
lista.append([40, 20, 30]);
print(lista);

#limpando elementos
lista.clear();
print(lista);

# Copia lista
lista  = [1, "Python", [40, 30, 20]];
copia_lista = lista.copy();
print(copia_lista);
print(id(lista), id(copia_lista));

# Count
cores = ["vermelho", "azul", "verde", "azul"];
cores.count("vermelho");
cores.count("azul");
cores.count("verde");

# Junção de lista
linguagens = ["python", "js", "c"];
print(linguagens);
linguagens.extend(["java", "csharp"]);
print(linguagens);

# primeira ocorrência
linguagens = ["python", "js", "c", "java", "csharp"];
print(linguagens.index("java"));
print(linguagens.index("python"));

# apagando elementos
print(linguagens.pop()); # apaga csharp
print(linguagens.pop()); # apaga java
print(linguagens.pop()); # apaga c
print(linguagens.pop(0)); # apaga python
print(linguagens);

# remove
linguagens = ["python", "js", "c", "java", "csharp"];
linguagens.remove("c");
print(linguagens);

# espelhamento (deixando lista ao contrario)
linguagens = ["python", "js", "c", "java", "csharp"];
linguagens.reverse();
print(linguagens);

# ordenação de lista

linguagens = ["python", "js", "c", "java", "csharp"];
linguagens.sort();
print(linguagens);

linguagens = ["python", "js", "c", "java", "csharp"];
linguagens.sort(reverse=True);
print(linguagens);

linguagens = ["python", "js", "c", "java", "csharp"];
linguagens.sort(key=lambda x: len(x));

linguagens = ["python", "js", "c", "java", "csharp"];
linguagens.sort(key=lambda x: len(x), reverse=True);
print(linguagens);

# tamanho da lista
linguagens = ["python", "js", "c", "java", "csharp"];
print(len(linguagens));

# ordenar lista sorted
linguagens = ["python", "js", "c", "java", "csharp"];
print(sorted(linguagens));

print(sorted(linguagens, key=lambda x: len(x)));

print(sorted(linguagens, key=lambda x:len(x), reverse=True));