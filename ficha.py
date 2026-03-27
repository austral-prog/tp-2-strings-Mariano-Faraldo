def ficha():
    
    Nombre_completo = input("introduzca su nombre completo por favor: ")

    Nombre_completo = Nombre_completo.strip().title()

    Mail = input("introduzca un mail: ")
    Mail = Mail.strip().lower()

    print("=" * 24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)

    print(f"Nombre: {Nombre_completo}")
    print(f"Email: {Mail}")

    caracteres_nombre = len(Nombre_completo)
    print(f"Caracteres en nombre: {caracteres_nombre}")

    posicion_espacio = Nombre_completo.find(" ")
    inicial_nombre = Nombre_completo[0]
    inicial_apellido = Nombre_completo[posicion_espacio + 1]
    print(f"Iniciales: {inicial_nombre}{inicial_apellido}")

    nombre_parte = Nombre_completo[:posicion_espacio].lower()
    apellido_parte = Nombre_completo[posicion_espacio + 1:].lower()
    usuario = apellido_parte + "." + nombre_parte
    print(f"Usuario: {usuario}")

    print(f"Email valido: {'@' in Mail}")

    pos_arroba = Mail.find("@")
    
    dominio = Mail[pos_arroba + 1:]
    print(f"Dominio: {dominio}")

    print(f"Nombre para archivo: {Nombre_completo.replace(' ', '_')}")

    print(f"Cantidad de a: {Nombre_completo.lower().count('a')}")

    print(f"Codigo secreto: {Nombre_completo[::-1].upper()}")

    nota1 = input("Introduzca nota 1: ").strip()
    nota2 = input("Introduzca nota 2: ").strip()
    nota3 = input("Introduzca nota 3: ").strip()

    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    suma = int(nota1) + int(nota2) + int(nota3)
    promedio = suma / 3
    promedio_entero = suma // 3  

    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")

    print("=" * 24)


# ficha()