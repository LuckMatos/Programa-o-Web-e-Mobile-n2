# (fácil) [Solução] Escreva um programa que dado uma sequência de n números lidos, imprimi-los na ordem inversa à da leitura.

list_lista = []

for i in range(4):
    num = int(input('Digite um numero'))
    list_lista.append(num)
    
    
list_lista.reverse()
lista_invertida = list_lista[::-1]

print(list_lista, lista_invertida)