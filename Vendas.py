meta = 150
qtda_vendida =int(input('Informe o valor vendido:\n'))

#Estrututa condicionais

if qtda_vendida<meta:
    print('Não bateu a meta, não tem direito ao bônus')
elif qtda_vendida>=(meta*2):
    bonus = meta*0.07
    print(f'Parabens você vendeu {qtda_vendida}, tem direito ao bônus de {bonus}.')
else:
    qtda_vendida>=meta
    bonus = meta*0.03
    print( f'você vendeu {qtda_vendida}, tem direito a {bonus}')
    
    