# Definindo as funções para cada operação matemática
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

# Solicitando ao usuário a operação desejada e os números que serão utilizados
operacao = input("Qual operação deseja realizar? (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando a operação correspondente e mostrando o resultado na tela
if operacao == "+":
    print(num1, "+", num2, "=", adicao(num1, num2))

elif operacao == "-":
    print(num1, "-", num2, "=", subtracao(num1, num2))

elif operacao == "*":
    print(num1, "*", num2, "=", multiplicacao(num1, num2))

elif operacao == "/":
    print(num1, "/", num2, "=", divisao(num1, num2))

else:
    print("Operação inválida.")
