def casting():
   precio = int(input())

   descuento = float(input())

   cantidad = int(input())

   Precio_con_descuento = precio - descuento

   cantidad_compra = Precio_con_descuento * cantidad

   print(f"Precio: {precio}")
   print(f"Descuento: {descuento}")
   print(f"Precio con descuento: {Precio_con_descuento}")
   print(f"Total: {cantidad_compra}")

# casting()

