try:
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except ValueError:
    print("Error: Se ingresó un valor que no es un número entero.")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
