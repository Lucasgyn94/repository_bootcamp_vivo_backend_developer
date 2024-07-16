

# Maisculas e minusculas em python
curso1 = 'pYtHon';
print(f'Curso 1: {curso1}')
print(curso1.upper());
print(curso1.lower());
print(curso1.title());

# Eliminando espaços em branco
texto = "   Olá Mundo!  ";
print(texto + '.');
print(texto.strip() + '.');
print(texto.lstrip() + '.');
print(texto.rstrip() + '.');

# Junções e centralização
curso3 = "Python";
print(curso3.center(10, "#"));
# "###Python###"
print("-".join(curso3));
