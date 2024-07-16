def exemplo_1():
    curso = "Curso de Python";
    nome_curso = curso;
    saldo, limite = 200, 200;

    curso is nome_curso;# true

    curso is not nome_curso; # false

    saldo is limite; #true


saldo = 1000;
limite = 1000;

print(saldo is limite);
print(saldo is not limite);
