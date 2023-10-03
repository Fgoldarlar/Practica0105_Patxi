Pan = int(input("Pon el numero de barras de pan de ayer: "))
Precio = 3.49
Descuento = 0.6
Coste = Pan * Precio * (1- Descuento)
print("El precio de una barra de hoy es ", Precio)
print("El descuento de una barra de ayer es ", (Descuento * 100))
print("El coste total es: ", round(Coste, 2))