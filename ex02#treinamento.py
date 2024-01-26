meta_f = 300 #int(input('Informe a meta do funcionario: \n'))
meta_e = 400 # int(input('Informe a meta da empresa:\n'))
nota = int(input('Informe a nota do funcionario:\n'))
venda_e = int(input('Informe as vendas da empresa:\n'))
venda_f = int(input(' Informe as vendas do funcionario:\n'))

# Estrutura condicional IF com OR e AND
if nota <= 0   and venda_f<=0 and venda_e<=0:
    print('Valores invalidos ')
elif nota == 9 or nota == 10  and  venda_f>meta_f and venda_e >meta_e:
    bonus = venda_f*0.3
    print(f' O funcionario alcançou a nota e bateu a meta, validou o bonus de {bonus}, Empresa bateu a meta!')  
elif nota == 9 or nota == 10 and venda_f>meta_f or venda_e<meta_e:
    print('funcionario alcançou a nota e bateu a meta, mas empresa fechou no negativo, funcionario não tem direito ao bonus') 
elif nota == 9 or nota == 10 and venda_f< meta_f and venda_e>meta_e :
     bonus = venda_f*0.3
     print( f'O funcionário não atingiu a nota, mas bateu a meta junto com a empresa, não tem direito ao bonus {bonus}')
else:
    print( 'Funcionario não tem direito')
