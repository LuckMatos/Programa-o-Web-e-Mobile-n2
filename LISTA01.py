lista = ['Banana', 'Abacaxi', 'Morango']
lista.insert(2, 'Lucas')
print(lista)

if lista[2] in lista:
    lista.insert(3, 'Matos')
    lista.append('Lopes')
    lista.pop(4)
    print(lista)
    
for i in range(len(lista)):
    print(lista[i])