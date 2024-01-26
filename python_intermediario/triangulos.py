# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


# Perimetro = XX.X
a = float(input('Digite o valor desejado:\n'))
b  = float(input('Digite o valor desejado:\n'))
c  = float(input('Digite o valor desejado:\n'))
perimetro = 0
if a + b > c and b + c > a and a + c > b: 
    perimetro = a + b + c 
    print( f'Perimetro = {perimetro}' )
else:
    area = (a + b)*c/2
    print(f'Area = {area}')
