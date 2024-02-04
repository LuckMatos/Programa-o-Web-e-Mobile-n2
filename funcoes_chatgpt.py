# Funções:

# Solicite aos alunos que criem uma função que aceite uma string como argumento e retorne True se a string for um palíndromo (pode ser lida da mesma forma de trás para frente) e False caso contrário.

def verificar_palindromo(string):
    string = string.replace(' ', '').lower()
    
    return string == string[::-1]
a = 'ame a ema'
resultado = verificar_palindromo(string=a)
print(resultado)