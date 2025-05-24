"""""
programa que solicite una cadena de caracteres e imprima como
resultado si la cadena es palíndroma o no
"""
try:
    a=input('Escribe una cadena: ')
    b=list(a)
    c=list(b)
    c.reverse()
    if c==b:
        print('Es un Palíndromo')
    else:
        print('No es un Palíndromo')

finally:
        print("Analisis de cadena finalizado")