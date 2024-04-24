# Crie um programa Python que simule uma calculadora simples. 
# O programa deve permitir que o usuário escolha entre diferentes operações matemáticas,
# como adição, subtração, multiplicação e divisão,
# e solicitar os números de entrada para executar 
# a operação selecionada.

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
   return x * y

def divisao(x, y):
    return x / y

print("Selecione a operação:")
print("1.Adição")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")

escolha = input("Digite sua escolha(1/2/3/4):")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if escolha == '1':
    print(num1,"+",num2,"=", adicao(num1,num2))

elif escolha == '2':
    print(num1,"-",num2,"=", subtracao(num1,num2))

elif escolha == '3':
    print(num1,"*",num2,"=", multiplicacao(num1,num2))

elif escolha == '4':
    print(num1,"/",num2,"=", divisao(num1,num2))
else:
    print("Entrada inválida")
