meta_f = 100
meta_e = 200

venda_f = int(input('Informe quanto o colaborador vendeu : '))
venda_e = int(input('Informe quanto a empresa vendeu : '))

if venda_f>meta_f and venda_e>meta_e:
    bonus = 0.03* venda_f
    print('O colaborador tem vendeu {}, validou o bonus de {}'.format(venda_f,bonus))
elif venda_f<meta_f and venda_e>meta_e:
    print('O colaborador não bateu meta, a empresa bateu meta!')

else:
    print('O colaborador bateu meta, mas não validou o bonus. A empresa não meta')