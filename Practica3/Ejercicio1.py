""""
Programa que pida al usuario un número entero y 
muestre por pantalla si es par o impar 
"""
try:
   a=0
   a=int(input("Introduce un número entero:"))

   if a % 2 == 0 :
    print("%d es par.")
   else:
    print("%d es impar.")

except ValueError:
    print("Error: Se ingresó un valor que no es un número entero.")
