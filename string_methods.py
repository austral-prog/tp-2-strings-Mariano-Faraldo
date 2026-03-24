def string_methods():
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""

    nombre_sin_espacios = nombre.strip()
    nombre_sin_espacios_iz = nombre.lstrip()
    nombre_sin_espacios_de = nombre.rstrip()

    print (f"Strip: {nombre_sin_espacios}")
    print (f"Lstrip: {nombre_sin_espacios_iz}")
    print (f"Rstrip: {nombre_sin_espacios_de}")

    frase_mayus = frase.upper()
    frase_minus = frase.lower()
    frase_title = frase.title()

    print(f"Upper: {frase_mayus}" )
    print(f"Lower: {frase_minus}" )
    print(f"Title: {frase_title}" )

    encontrar_frase = frase.find("gran")

    print(f"Find: {encontrar_frase}")

    reemplazo_frase = frase.replace("programacion", "desarrollo")

    print(f"Replace: {reemplazo_frase}")

    Count_a = frase.count("a")

    print(f"Count: {Count_a}")

    print("Contiene Python:","Python" in frase)
    print("Contiene Java:","Java" in frase)

    Slice_frase = frase[0:6]

    print(f"Slice: {Slice_frase}")
    
    paso_frase = Slice_frase[0::2]

    print(f"Paso: {paso_frase}")

    reversa_frase = Slice_frase[::-1]

    print(f"Reverso: {reversa_frase}")

    print(f"Formato: {nombre_sin_espacios} sabe {Slice_frase}")

    print(f"{multilinea}")


string_methods()

