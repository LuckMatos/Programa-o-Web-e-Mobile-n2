'''Listas e Loops:

Peça aos alunos para criar uma lista de números. Em seguida, peça para o programa verificar e imprimir apenas os números pares da lista usando loops.'''

nomes = []

for i in range(6):
    nome = input('Infome  o seu nome:\n')
    nomes.append(nome)

print('Nomes inseridos: ',end= '')
for n in nomes:
        print( n,end=',')
        
