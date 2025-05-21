def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    elif edad < 18:
        raise PermissionError("Debes ser mayor de edad para continuar.")
    else:
        print("Acceso concedido.")

try:
    edad = int(input("Introduce tu edad: "))
    verificar_edad(edad)
except (ValueError, PermissionError) as e:
    print("Error:", e)