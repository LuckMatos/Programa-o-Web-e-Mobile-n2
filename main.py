from class_triangulo import Triangulo

triangulo = Triangulo(3,86,6)

print(triangulo.maior_lado(), triangulo.calculando_diametro())

lados_do_triangulo = triangulo.get_lado_dos_triangulo()

print(lados_do_triangulo)

alterando_lados = triangulo.set_lados_do_triangulo(4,3,3)

novos_lado = triangulo.get_lado_dos_triangulo()

print(novos_lado)



