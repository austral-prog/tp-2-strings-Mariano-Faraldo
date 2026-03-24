def change():
    print("Ingresar gasto:")
    gasto = float(input())
    print(gasto)
    print("Dinero recibido")
    dinero_recibido = int(input())
    print(dinero_recibido)
    print()
    print("Vuelto")
    print()
    pesos_vuelto = dinero_recibido - gasto
    print("Pesos:")
    print(int(pesos_vuelto))
    centavos_vuelto = round((pesos_vuelto - int(pesos_vuelto)) * 100)
    print("Centavos:")
    print(centavos_vuelto)

change()