print('*'*20 +' CALCULADORA '+ '*'*20)

while True:
    try:
        num = int(input('Digite o primeiro número:\n'))
        num1 = int(input('Digite o segundo  número:\n'))
    except ValueError:
    
        print('ERRO: Digite apenas numero')
        continue
    opcao = input('[A]dição\n[S]ubtração\n[M]ultiplicação\n[D]ivisão\n[E]ncerrar\n').upper()

    if opcao != 'A' and opcao !='S' and opcao != 'M' and opcao !='D'and opcao !='E':
        print('OpçAo invalida')
    
    if opcao == 'A':
        print (f'{num} + {num1} = {num + num1}')
    elif opcao == 'S':
          print (f'{num} - {num1} = {num - num1}')
    elif opcao == 'M':
        
          print (f'{num} * {num1} = {num  * num1}')
    elif opcao == 'D':
        
          print (f'{num} /  {num1} = {num  / num1}')
    elif opcao == 'E':
        print('Programa encerrado')
        break