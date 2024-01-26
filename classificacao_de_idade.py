'''Classificação de Idade:

Peça ao usuário para inserir sua idade e, em seguida, use instruções if e elif para classificar a idade em uma das seguintes categorias:

"Criança" se a idade for menor que 13 anos.
"Adolescente" se a idade estiver entre 13 e 19 anos, inclusive.
"Adulto" se a idade for igual ou maior que 20 anos.'''

idade = int(input('Informe a sua idade:\n'))
if idade <= 13 : 
     print('Criança')
elif idade > 13 and idade <19:
    print ('Adolescente')
else:
    print ('Adulto')