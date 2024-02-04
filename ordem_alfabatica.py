# (fácil)Faça um programa que leia 5 nomes e mostre os nomes em ordem alfabética.

nomes = []
for i in range(5):
 nome = input('Digite o seu Nome:\n')
 nomes.append(nome)
 nomes.sort()

 
print(nomes)