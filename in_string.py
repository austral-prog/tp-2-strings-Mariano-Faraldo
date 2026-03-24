def check_vowels():
    Ingresar_nombre = input("Introducte tu nombre: ")

    nombre_minuscula = Ingresar_nombre.lower()

    Hay_a = "a" in nombre_minuscula
    Hay_e = "e" in nombre_minuscula
    Hay_i = "i" in nombre_minuscula
    Hay_o = "o" in nombre_minuscula
    Hay_u = "u" in nombre_minuscula

    print(f"Contiene a: {Hay_a}")
    print(f"Contiene e: {Hay_e}")
    print(f"Contiene i: {Hay_i}")
    print(f"Contiene o: {Hay_o}")
    print(f"Contiene u: {Hay_u}")

check_vowels()
