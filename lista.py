
#lista = [ 0, 1, 2,]
#lista2 = ['Jornais ','Cadeira', ' Agosto', 'T7.']
#print(f' foram vendidos {lista[2]} {lista2[0]} em {lista2[2]} na loja {lista2[3]}')

#ista3 = lista + lista2
#lista2.append('Jorge')
#print(lista2)

# Alteração incrementais de variáveis

lista3 = ['mac', 'iphone']
lista3+=['Ipad']
print (lista3)
lista2 =[100, 200, 500]
soma_vendas = 300
soma_vendas+= 500

email = 'Em agosto vendemos {} unidades de produtos, sendo: \n{} unidades de {}  \n{} unidades de  {}'.format(soma_vendas, lista2[0],lista3[0],lista2[1],lista3[1])
email+= '\n{} unidades de {}'.format(lista2[2],lista3[2])
print(email)