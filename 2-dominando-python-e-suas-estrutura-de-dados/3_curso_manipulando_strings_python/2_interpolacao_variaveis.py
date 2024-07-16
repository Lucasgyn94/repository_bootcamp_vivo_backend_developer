def oldStyle():
    # Old Style %
    nome = "Lucas"; 
    idade = 29; 
    profissao = "Programador"; 
    linguagem = "Python";

    print("Olá, me chamo %s. Eu tenho %d anos de idade. Trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem));

def formatStyle():
    nome = "Lucas"; 
    idade = 29; 
    profissao = "Programador"; 
    linguagem = "Python";

    print("Olá, me chamo {}. Eu tenho {} anos de idade. Trabalho como {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem));

def formatStyle2():
    nome = "Lucas"; 
    idade = 29; 
    profissao = "Programador"; 
    linguagem = "Python";

    print("Olá, me chamo {3}. Eu tenho {2} anos de idade. Trabalho como {1} e estou matriculado no curso de {0}." .format(linguagem, profissao, idade, nome));

def formatStyle3():
    nome = "Lucas"; 
    idade = 29; 
    profissao = "Programador"; 
    linguagem = "Python";

    print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade. Trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem));

def formatStyle3():
    pessoa = {
        "nome": "Lucas",
        "idade": 29,
        "profissao": "Programador",
        "linguagem": "Python"
    }

    print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade. Trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))

def fStyle():
    nome= "Lucas";
    idade = 29;
    profissao = "Programador";
    linguagem = "Python";
    
    print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade. Trabalho como {profissao} e estou matriculado no curso de {linguagem}.")


def formataString():
    PI = 3.14159

    print(f"O valor de PI é {PI: .2f}.");
    print(f"O valor de PI é {PI: 10.2f}.");

formataString()  