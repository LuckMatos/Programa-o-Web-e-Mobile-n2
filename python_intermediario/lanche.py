print('Bem-vindo ao Lanche Python\n CARDÁPIO\n 1 - Cachorro Quente R$ 4.00\n 2 - X-Salada R$ 4.50\n 3 - X-Bacon R$ 5.00\n 4 - Torrada Simples R$ 2.00 \n 5 - Refrigerante R$ 1.50\n ' )

cod = input('Informe código do item:\n')
quantidade = int(input('Informe a quantidade desejada:\n'))
cachorro_quente = 4.00
x_salada = 4.50        
x_bacon = 5.00
torrada =  2.00 
refrigerante = 1.50

if quantidade < 0 or quantidade == "":
    print('Informe a quantidade desejada.')
    
if cod == '1' and float( quantidade )> 0:
    valor_pagar = quantidade * cachorro_quente 
    print(f'Total: R${valor_pagar:.3}')
elif cod == '2' and quantidade > 0:
    valor_pagar = quantidade * x_salada
    print(f'Total: R${valor_pagar:.3}')
elif cod == '3' and quantidade > 0:
    valor_pagar = quantidade * x_bacon
    print(f'Total: R${valor_pagar:.3}')
elif cod == '4' and quantidade > 0:
    valor_pagar = quantidade * torrada
    print(f'Total: R${valor_pagar:.3}')
elif cod == '5' and quantidade > 0:
    valor_pagar = quantidade * refrigerante
    print(f'Total: R${valor_pagar:.3}')
else:
    print('Produto inválido')