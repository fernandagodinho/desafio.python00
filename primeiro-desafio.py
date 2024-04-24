# Crie um programa que gere senhas aleatórias com um determinado número de caracteres. 
# O programa deve permitir que o usuário especifique o número de 
# caracteres da senha e quais caracteres devem ser incluídos na mesma.

import string
import random

def gerar_senha(tamanho, caracteres):
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

print("Gerador de Senha Aleatória")
tamanho = int(input("Digite o tamanho da senha: "))
caracteres = input("Digite os caracteres que podem ser incluídos na senha: ")

senha = gerar_senha(tamanho, caracteres)
print("Sua senha é: ", senha)
