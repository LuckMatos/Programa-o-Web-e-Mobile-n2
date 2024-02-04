# (moderado) [Solução] Escreva um programa que leia n números. Depois da leitura mostre a média dos números lidos, o maior número lido, e o menor.
from statistics import mean
lista_num =[]

for i in range(2):
    num = int(input('Digite o número:\n'))
    lista_num.append(num)
    
    
print(mean(lista_num))
print(min(lista_num), max(lista_num))