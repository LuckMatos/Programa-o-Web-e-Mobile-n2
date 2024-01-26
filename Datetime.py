# Estrutura condicional IF 

meta_de_vendas = 50000
qtdeVenda = 400


if qtdeVenda>=meta_de_vendas:
    print(f'Batemos a meta, vendemos {qtdeVenda}')
else: 
    print('Infelizmente você não bateu a meta')
    qtdeVenda = int( input('informe a quantidade vendida novamente:'))

while qtdeVenda <meta_de_vendas:
    
     print('Infelizmente você não bateu a meta')
     qtdeVenda = int( input('informe a quantidade vendida novamente:'))
print('Você bateu a meta!')