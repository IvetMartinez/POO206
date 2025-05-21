try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except (ValueError, ZeroDivisionError):
    print("¡Ocurrió un error! Asegúrate de ingresar un número válido y distinto de cero.")
0