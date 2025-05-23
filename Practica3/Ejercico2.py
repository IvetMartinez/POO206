""""
Programa que pida al usuario un año indicando si es bisiesto o no 
Divisible por 4: Si el año es divisible por 4, generalmente es bisiesto. 
Divisible por 100: Si es divisible por 100, NO es bisiesto a menos que también sea divisible por 400. 
Divisible por 400: Si es divisible por 400, SI es bisiesto. 
En resumen, un año es bisiesto si es divisible por 4 pero no por 100, o si es divisible por 400. 
"""
a=0
a=int(input("Introduce un año:"))

if a % 4 != 0: 
	print("Año no bisiesto")
elif a % 4 == 0 and a % 100 != 0:
	print("Año bisiesto")
elif a % 4 == 0 and a % 100 == 0 and a % 400 != 0: 
	print("Año no bisiesto")
elif a % 4 == 0 and a % 100 == 0 and a % 400 == 0: 
	print("Año bisiesto")
