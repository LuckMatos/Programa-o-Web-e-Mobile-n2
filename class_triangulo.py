class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.__lado_a = lado_a
        self.__lado_b = lado_b
        self.__lado_c = lado_c
        
    def calculando_diametro(self):
        return self.__lado_a + self.__lado_b + self.__lado_c
    def maior_lado(self):
        if self.__lado_a > self.__lado_b and self.__lado_a > self.__lado_c:
            return self.__lado_a
        elif self.__lado_b> self.__lado_a and self.__lado_b> self.__lado_c:
            return self.__lado_b
        return self.__lado_c
    def get_lado_dos_triangulo(self):
        return f' lado A: {self.__lado_a}, lado B: {self.__lado_b}, lado C: {self.__lado_c}'
    def set_lados_do_triangulo(self, valor_a, valor_b, valor_c):
        self.__lado_a = valor_a
        self.__lado_b = valor_b
        self.__lado_c = valor_c

        