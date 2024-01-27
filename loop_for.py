# nomes = [ "Pedro",'João', 'Anderson']

# for  nome in nomes:
#     print(nome.upper(),end= '')


"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = 'lucas'
cont = 0
letras = ''
tam = len(palavra_secreta.lower())
print(tam)


while True:
    letra = input('Digite uma letra:\n')

    if letra in palavra_secreta:
        # print(letra)

        print(f'Palavra:{letra}')
        letras += letra
        print(letras)
        if letras == palavra_secreta:
            print('Parabéns, você acertou!')
            break

    elif letra not in palavra_secreta:
        print('*')

    cont += 1
    print(f'Tentativa {cont}')
    if cont > tam:
        print('Quantidade máxima de tentativas atingida')
        break
