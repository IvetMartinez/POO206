try:
    n = int(input("Ingresa un número entero mayor a 10"))
    if n>10:
        print("Ingresaste un número entero y mayor a 10")
        print("Números impares desde  hasta ", n)
        for i in range(2, n + 1):
            if i % 2 != 0:
                 print(i, ", ")
    else:
        print("No ingresaste un valor  mayor a 10. Ingresa un valor válido ") 
        
except ValueError:
    print("Error: Se ingresó un valor que no es un número entero.")

 