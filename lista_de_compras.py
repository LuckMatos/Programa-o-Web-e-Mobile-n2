
import os


itens = []

while True:
   
    op = input('[i]nserir [a]pagar [l]listar\n')
    
    if op.lower() == '':
      print('Opção inválida')
        
    if op.lower() != 'i' and op.lower() !=  'a' and op.lower() !='l':
        print('Opção inválida')
        continue
             
    if op.lower() == 'i':
        os.system('CLS')
        item = input('Digite o item :\n')
        if item =='':
            print('Lista vazia')
        itens.append(item)
    elif op.lower() == 'a':
        try:
         indice = int(input('Digite o indice:'))
         itens.pop(indice)
        
        except:
            print('ERRO: Não foi possível apagar esse indice')
    elif op.lower() == 'l':
        os.system('CLS')     
        for i, valor in enumerate(itens):
             print(i, valor)
