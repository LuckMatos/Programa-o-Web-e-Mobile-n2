# Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

# Entrada
# Seis valores, negativos e/ou positivos.

# Saída
# Imprima uma mensagem dizendo quantos valores positivos foram lidos.

i = 0
acumuladora = 0

while i < 7:
    numero = int(input('Informe o numero:\n'))
    
    if numero>0:
        acumuladora += 1
    
    i+=1
print(f'{acumuladora} valores positivos')