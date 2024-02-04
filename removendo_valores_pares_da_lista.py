# (moderado) [Solução] Escreva um programa que leia 20 números. Depois da leitura, remova todos os valores pares que existem na lista e mostre a lista resultante.
lista_numeros = []
lista_numeros_pares = []
cont = 0 

for i in range(20):
    num = int(input('Digite um numero:\n'))
    lista_numeros.append(num)
    if lista_numeros[i]% 2 == 0:
        lista_numeros_pares.append(lista_numeros[i])
        cont+=1

print(f'A lista {lista_numeros} é composta por {cont, len(lista_numeros_pares)} números pares, sendo eles: {lista_numeros_pares}')