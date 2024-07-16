def my_function():
    print("Hello world!");

def my_function(nome):
    print(f"Hello {nome}!");

def exibir_mensagem(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!");

def calcular_soma(numeros):
    return sum(numeros);


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1;
    sucessor = numero + 1;

    return antecessor, sucessor;

# Argumentos nomeados
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/ {modelo}/ {ano} / {placa}");

# combinação de parâmtros obrigatórios Args e Kwargs
def exibir_poema(data_extenso, *lista, **dicionario):
    texto = "\n".join(lista);
    meta_dados = "\n".join([f"{chave.title()} : {valor}" for chave, valor in dicionario.items() ]);
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem);

#my_function();
#my_function("Lucas");
#exibir_mensagem(nome="Lucas");
#exibir_mensagem();
#print(calcular_soma([1, 2, 3, 4, 5]));
#print(retorna_antecessor_e_sucessor(2));


#salvar_carro("Fiat", "Palio", 1999, "ABC-1234");
#salvar_carro(modelo="Palio", marca="Fiat", ano=1999, placa="ABC-1234");
#salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"});

exibir_poema(
    "Zen of Python", 
    "Beautiful is better than ugly",
    "Explicit is better than explicit",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    autor="Lucas",
    local="Goiânia, GO",
    ano = 1999
)
