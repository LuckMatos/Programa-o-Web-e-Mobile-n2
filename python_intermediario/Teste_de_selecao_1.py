"""Leia 4 valores inteiros A, B, C e D. A seguir, 

se B for maior do que C e se D for maior do que A,

e a soma de C com D for maior que a soma de A e B e se C e D, ambos,

 forem positivos e se a variável A for par escrever a mensagem "Valores aceitos",

 senão escrever "Valores nao aceitos"."""

a = int(input('Informe o numero:\n'))
b = int(input('Informe o numero:\n'))
c = int(input('Informe o numero:\n'))
d = int(input('Informe o numero:\n'))

soma_ab = a + b
soma_cd = c + d


if a %2 == 0:
    if a >= 0 and b >= 0 and c >= 0 and d >=0:
        if soma_cd > soma_ab and c and d :
            print('Valores aceitos')
else:
    print('Valores não aceitos')