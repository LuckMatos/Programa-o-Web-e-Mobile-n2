salas = [['Maria', 'Helena'], ['Luiz','João','Eduarda', (0,10,20,30,40)], ['Renata']
]

print(salas[1] ) # Retorna a lista 
print(salas[1][3] ) #Retorna a lista deseja dentro da lista 
print(salas [1][3][4]) # Retorna o valor desejado da lista desejada. 

for sala in salas:
    print (f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
