'''Solicite aos alunos que criem um programa que peça a idade do usuário e, com base nessa idade, informe se a pessoa é menor de idade, maior de idade ou idosa.'''


idade = int(input('Digite sua idade'))

if idade < 18:
    print (f'Você tem apenas {idade}, ainda alcançou a maior idade.')
elif idade >= 18 and idade <= 50:
    print('Bem-vindo ao mundo dos adultos! ')
else :
    print('Tá velhão')