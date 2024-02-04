# (fácil) [Solução] Escreva um programa que leia 15 numeros. Apenas após ler todos os números do teclados, o programa deve apresentar os números lidos.
lista_de_numeros= []

for i in range(15):

 num = int(input('Digite um número:\n'))
 lista_de_numeros.append(num)
 
for n in lista_de_numeros:
     print(n, end='')