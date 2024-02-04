# 1. Crie a função verificar_idade() que:
# 1. Solicitar ao usuário que insira sua idade.
# 2. Tentar converter a entrada do usuário para
# um número inteiro.
# 3. Verificar se a idade está dentro do intervalo
# de 0 a 120 anos.
# 4. Lidar com a exceção ValueError se o
# usuário inserir algo que não seja um número
# inteiro.
# 5. Imprimir uma mensagem indicando se a idade
# é válida ou não

def verificar_idade():
    try:
        
        idade = int(input('Informe sua idade:\n'))
    except ValueError:
        idade = -1 
        print('ERRO: Insira um número inteiro válido')
    finally:
        print('Programa finalizado')
    if idade >0 and idade< 120:
        print(f' Idade válida: {idade} anos')
    else:
        print('ERRO: A idade deve estar no intervalo entre 0 a 120 anos')
        

verificar_idade()