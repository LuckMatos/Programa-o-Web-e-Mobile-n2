# (difícil) [Solução] A distância euclidiana ( wikipedia) pode ser utilizada para determinar a distância entre dois pontos 2D em um plano 2D. Cada ponto possui suas próprias coordenadas x e y no plano 2D. Escreva um programa que leia as coordenadas do ponto1 (x1, y1) e as coordenadas ponto2 (x2, y2). Após a leitura dos valores, calcule a distância entre os dois utilizando a distância euclidiana, conforme a equação a seguir: , onde d é a distância entre os dois pontos. Apresente, após o cálculo, a distância entre os dois pontos lidos.
from math import sqrt
x1 = float(input('Digite a cordenada de x1\n'))
x2 = float(input('Digite a cordenada de x2\n'))

y1 =float(input('Digite o valor de Y1:\n'))
y2 =float(input('Digite o valor de Y2:\n'))

d = sqrt((x1 - x2)*2 + (y1 - y2)*2)
print(d)