def names():

    nombre = input("Escriba su nombre: ")

    apellido = input("Escriba su apellido: ")

    nombre_completo = (nombre + " " + apellido)

    nombre_completo_minusculas = nombre_completo.lower()

    nombre_completo_formato_titulo = nombre_completo.title()

    nombre_completo_mayusculas = nombre_completo.upper()

    nombre_completo_minisculas_tabulador = nombre_completo.lower()

    print(nombre_completo_minusculas)

    print(nombre_completo_formato_titulo)

    print(nombre_completo_mayusculas)

    print("\t" + nombre_completo_minisculas_tabulador)

names()

