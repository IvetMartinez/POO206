try:
    print("Intentando abrir un archivo...")
    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
    print(contenido)

except FileNotFoundError:
    print("Error: El archivo no existe.")

finally:
    print("Este mensaje se muestra siempre, sin importar si hubo un error.")
