# (fácil) [Solução] Escreva um programa que leia 15 numeros. Apenas após ler todos os números do teclados, o programa deve apresentar os números lidos em ordem crescente.
lista_num = []
num2= 0

for i in range(0,15):
 num = int(input('Digite um numero:'))
 lista_num.append(num)
    
numeros_ordenados = sorted(lista_num)

print(numeros_ordenados)

# Antes de tentar criar um algoritmo, verifica se há algum método capaz de fazer a tarefa com mais eficiência. 
