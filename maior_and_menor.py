'''Cálculo de Maior de Dois Números:
Solicite que o usuário insira dois números e, em seguida, use if e elif para determinar qual dos números é o maior e exiba-o.'''
numero1 = int(input('Informe o primeiro numero:'))
numero2 = int(input('Informe o segundo numero'))

if numero1 > numero2:
    print(f'{numero1} é o maior')
elif numero2 > numero1:
    print(f'{numero2} é o maior ')
else:
    print('Os números são iguais')
