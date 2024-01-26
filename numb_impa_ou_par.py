'''Verificação de Número Par ou Ímpar:
Peça ao usuário para inserir um número e, em seguida, use uma estrutura if para determinar se o número é par ou ímpar. Exiba a respost'''

numb = int(input('Digite um numero:'))
if numb % 2 != 0:
    print(f'O {numb} é impar')
else :
    print(f'O {numb} é par')