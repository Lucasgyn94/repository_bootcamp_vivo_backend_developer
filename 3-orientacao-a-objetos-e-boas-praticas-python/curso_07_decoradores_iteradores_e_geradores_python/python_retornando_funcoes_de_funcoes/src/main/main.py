# RETORNANDO FUNCOES DE FUNCOES
def calculadora(operacao):
    def somar(a, b):
        return a + b
    
    def subtrair(a, b):
        return a - b
    
    def multiplicar(a, b):
        return a * b
    
    def dividir(a, b):
        return a / b
    
    if operacao == "+":
        return somar
    elif operacao == "-":
        return subtrair
    elif operacao == "*":
        return multiplicar
    elif operacao == "/":
        return dividir
    else:
        return "Digite uma operação válida + - * /"
    
calculadora("+")(2, 5)

op = calculadora("+")
print(op(2, 5))

op = calculadora("-")
print(op(10, 5))

op = calculadora("*")
print(op(5, 5))

op = calculadora("/")
print(op(10, 2))