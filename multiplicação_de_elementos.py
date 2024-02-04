# (moderado) [Solução] Escreva um programa que leia duas listas de 10 posições de números inteiros e faça a multiplicação dos elementos de mesmo índice destas listas, colocando o resultado em uma terceira lista. Mostre a lista resultante.

lista1 = [1,3,4,5,23,99,23,1,34,22,3,4]
lista = [1,2,3,4,8,4,5,2,3,65,5,4,2,3,4]
lista3 = []
for i in range(len(lista1)):
    lista3.append( lista[i] * lista1[i])
    
print(lista3)
