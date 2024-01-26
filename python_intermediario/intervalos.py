
num = int(input('Digite um número:\n'))

if num >= 0 and num  <= 25:
    print('Intervalo [0,25]')
elif num >= 21.01 and num  <= 50.1:
    print('Intervalo [25,50]')
elif num >= 50.1 and num  <=75.01:
    print('Intervalo [50,75]')
elif num >=75.01 and num <= 100.00:
   print('Intervalo [75,100]')
else:
    print('Fora do intervalo')
    