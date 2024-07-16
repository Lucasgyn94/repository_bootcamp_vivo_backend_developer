#Limpando dicionario
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3343-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "melaine", "telefone": "3333-7766"}
}

print(f'Dicionário antes da limpeza: \n{contatos}');
contatos.clear();
print(f'Dicionário depois da limpeza: \n{contatos}');

# Fazendo copia do dicionário
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
}

copia = contatos.copy();
copia["needslucas944@gmail.com"] = {"nome": "Lu"};
print(contatos["needslucas944@gmail.com"]);
print(copia["needslucas944@gmail.com"]);

# criando chaves
print(dict.fromkeys(["nome", "telefone"]));
print(dict.fromkeys(["nome", "telefone"], "vazio"));

# acessando dados com get
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
}

# print(contatos["chave"]); # KeyError
print(contatos.get("chave")); # None
print(contatos.get("chave",{})); # {}
print(contatos.get("needslucas944@gmail.com",{}));

# retornando uma lista de tuplas
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
}

print(contatos.items());

contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3343-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "melaine", "telefone": "3333-7766"}
}

print(contatos.keys());

# removendo uma chave com pop
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3343-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "melaine", "telefone": "3333-7766"}
}

contatos.pop("needslucas944@gmail.com");
print(contatos.pop("needslucas944@gmail.com", "Não existe mais"));

# popitem
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3343-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "melaine", "telefone": "3333-7766"}
}

contatos.popitem();
contatos.popitem();
print(contatos);

# setdefault
print('\nSetDefault\n');
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
  }

print(contatos.setdefault("nome", "Giovanna"));
print(contatos);

print('\n \n');

print(contatos.setdefault("idade", 29));
print(contatos);

# atualização de dicionários

print('\n Atualização de dicionários');
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221"},
}

contatos.update({"needslucas944@gmail.com" : {"nome": "Lu"}});
print(contatos)

contatos.update({"giovana@gmail.com": {"nome": "Giovana", "telefone": "3333-2221"}});
print(contatos);

# retornando os valores do dicionário
print('\n Retornando os valores do dicionário\n');
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3343-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "melaine", "telefone": "3333-7766"}
}
print(contatos.values());

# verificar se a chave existi ou não
print('\n Verificação de chave: \n');

contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3343-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "melaine", "telefone": "3333-7766"}
}

print("needslucas944@gmail.com" in contatos);
print("megui@gmail.com" in contatos);
print("idade" in contatos["needslucas944@gmail.com"]);
print("telefone" in contatos["giovanna@gmail.com"]);

# removendo valores com del
print("\n removendo valores com del\n");

contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3343-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "melaine", "telefone": "3333-7766"}
}

del contatos["needslucas944@gmail.com"]["extra"];
del contatos["chappie@gmail.com"]
print(contatos);
