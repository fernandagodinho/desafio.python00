# As estruturas de dados são fundamentais em qualquer linguagem de programação.
# Este exercício irá focar na criação e manipulação de listas,
# tuplas e dicionários em Python. Você aprenderá a adicionar, 
# remover e modificar elementos nessas estruturas, bem como a acessar 
# seus valores de forma eficiente.

# Criando uma lista
lista = [1, 2, 3, 4, 5]

# Adicionando um elemento ao final da lista
lista.append(6)

# Removendo um elemento da lista
lista.remove(1)

# Modificando um elemento da lista
lista[0] = 7

# Acessando um elemento da lista
print(lista[0])

# Criando uma tupla
tupla = (1, 2, 3, 4, 5)

# Acessando um elemento da tupla
print(tupla[0])

# Tuplas são imutáveis, então você não pode adicionar, remover ou modificar elementos

# Criando um dicionário
dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}

# Adicionando um elemento ao dicionário
dicionario['chave3'] = 'valor3'

# Removendo um elemento do dicionário
del dicionario['chave1']

# Modificando um elemento do dicionário
dicionario['chave2'] = 'novo valor'

# Acessando um elemento do dicionário
print(dicionario['chave2'])
