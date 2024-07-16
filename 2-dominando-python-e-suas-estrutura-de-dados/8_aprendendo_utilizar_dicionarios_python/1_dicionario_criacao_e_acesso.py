# Criando dicionário
pessoa = {
    "nome": "Lucas",
    "idade": 29,
    "profissao": "Programador",
    "linguagem": "Python"
}

# criando com dict
pessoa = dict(nome="Lucas", idade=29, profissao="Programador", linguagem="Python")

# adicionando nova chave
pessoa["telefone"] = "3333-1234";

# Acessando os dados
print(pessoa["nome"]);
print(pessoa["idade"]);
print(pessoa["profissao"]);
print(pessoa["linguagem"]);
print(pessoa["telefone"]);

## modificando os dados
pessoa["idade"] = 30;
print(pessoa["idade"]);
pessoa["telefone"] = "9988-1787";
print(pessoa["telefone"]);

print(pessoa);

# Dicionários aninhados
contatos = {
    "needslucas944@gmail.com": {"nome": "Lucas", "telefone": "3333-2221", "extra": {"a" : 1}},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3343-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "melaine", "telefone": "3333-7766"}
}

print(contatos);

# Acessando telefone
print(contatos["giovanna@gmail.com"]["telefone"]);

# acessando o extra
print(contatos["needslucas944@gmail.com"]["extra"]["a"]);

# Iterando sobre dicionários
print('\nIterando sobre dicionários: \n')
for chave in contatos:
    print(chave, contatos[chave]);

print('\nIterando sobre dicionários com chave e valor: \n')
for chave, valor in contatos.items():
    print(chave, valor);
