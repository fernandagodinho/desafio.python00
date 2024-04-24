# Desenvolva um programa que verifique se uma palavra 
# fornecida pelo usuário é um palíndromo, ou seja, se ela pode ser lida 
# da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda,
# como “radar” ou “asa”.

def verificar_palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        return True
    else:
        return False

palavra = input("Digite uma palavra: ")
if verificar_palindromo(palavra):
    print(palavra, "é um palíndromo.")
else:
    print(palavra, "não é um palíndromo.")
