
#Crie um programa ao o usuário cadastre produtos, e para finalizar o programa o usuário digite enter.

f = open('lucas.txt',"w")
produtos  = str(input ('Digite o nome do produto que deseja cadastrar: \n'))
produto = []
while produtos !="":
    produto.append(produtos)
    produtos = str(input ('Digite o nome do produto que deseja cadastrar: \n'))
    print(produto)
    for i in produtos :
    
     f.write(i.replace( " ", ","))
    

print('Escrita concluída!! ')