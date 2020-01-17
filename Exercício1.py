# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números

lista1 = [1,2,3,4,5,6,7,8,9,10]
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])
print(lista1[4])
print(lista1[5])
print(lista1[6])
print(lista1[7])
print(lista1[8])
print(lista1[9])

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

lista2 = [1, 2.5, 'Wilkinson', 0, '123']
print(lista2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

string1 = 'Wilkinson'
string2 = 'Varela'
string3 = string1 + string2

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla1 = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla1.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dic = {}
print(dic)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dic2 = {1 : 'Wilkinson', 2:'Varela', 3:'Oliveira'}
print(dic2)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dic2.update({4:'Lima'})
print(dic2)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
# Imprima o dicionário na tela.

dic3 =  {'lista':[1, 2], 2: 'inteiro', 3: 5.5}
print(dic3)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

lista3 = ["Texto", (1, 2), {'chave1': 1, 'chave2': 2}, 5.5]
print(lista3)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.

frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[:18])