try:
    n = int(input("Ingresa un número entero positivo: "))

    if n >= 0:
        while n >= 0:
            print(n, ", ")
            n -= 1
    else:
        print("El número debe ser positivo.")

except:
    print("Error: Debes ingresar un valor válido.")