try:
    f = input("Digita una frase: ")

    if f.strip():
        l = input("Digita una letra: ")

        if len(l) != 1:
            raise ValueError("Introduce solo una letra.")
        
        c = f.lower().count(l.lower())

      
        print(f"La letra '{l}' aparece {c} veces en la frase.")
        
    else:
        print("Datos inválidos. No ingresaste una frase.")

except ValueError:
    print(f"Valores inválidos. Digita lo que se te indica")

finally:
    print("Programa finalizado.")