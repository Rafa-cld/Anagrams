def anagrams(texto1, texto2):
    # Eliminar espacios y convertir a minúsculas
    texto1 = texto1.replace(" ", "").lower()
    texto2 = texto2.replace(" ", "").lower()

    # Verificar que no estén vacíos
    if not texto1 or not texto2:
        return False

    return sorted(texto1) == sorted(texto2) # Verificar si son anagramas
    
# Pedir entradas al usuario
texto1 = input("Ingrese la primer palabra: ")
texto2= input("Ingrese la segunda palabra: ")

# Comprobar e imprimir resultado
if anagrams(texto1, texto2):
    print("Los textos son anagramas.")
else:
    print("Los textos no son anagramas.")

   