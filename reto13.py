import numpy as np

matriz_de_venta = np.array([
 ["Producto 1",30,50,10,20], ["Producto 2",20,70,5,30],["Producto 3",50,20,15,10],["Producto 4",15,100,20,40],["Producto 5",10,150,25,60],
 ["Producto 6",25,200,10,80],["Producto 7",40,30,0,15],["Producto 8",35,120,5,50],["Producto 9",45,60,20,25],["Producto 10",50,90,30,35],
 ["Producto 11",60,110,15,45],["Producto 12",30,80,10,30],["Producto 13",25,50,5,20],["Producto 14",40,150,0,60],["Producto 15",55,60,10,25],
 ["Producto 16",35,70,10,35],["Producto 17",45,100,20,45],["Producto 18",50,120,15,50],["Producto 19",60,80,10,40],["Producto 20",30,150,25,55]
])
#EJERCICIO 1
nombres = np.array(matriz_de_venta[:, 0])
cantidad = np.array(matriz_de_venta[:, 1].astype(float))
precio   = np.array(matriz_de_venta[:, 2].astype(float))
descuento = np.array(matriz_de_venta[:, 3].astype(float))
costo    = np.array(matriz_de_venta[:, 4].astype(float))

#EJERCICIO 2
total = np.subtract(np.multiply(cantidad, precio),np.multiply(np.divide(descuento,100),np.multiply(cantidad, precio)))

for i in range(len(nombres)):
    print(f"{nombres[i]} ${total[i]}")
#EJERCICIO 3
print(f"\nEL INGRESO TOTAL ES: {total.sum()}\n")
#EJERCICIO 4
costo_produccion = np.multiply(cantidad,costo)
for i in range(len(nombres)):
    print(f"{nombres[i]} su costo de producción es: {np.multiply(cantidad,costo)[i]}")
#EJERCICIO 5
print("")
ganancia_bruta = np.subtract(total,costo_produccion)
for i in range(len(nombres)):
    print(f"LA GANANCIA BRUTA POR {nombres[i]} ES: {ganancia_bruta[i]}")
#EJERCICIO 6
print(f"\nLA GANACIA BRUTA TOTAL DE TODOS LOS PRODUCTOS ES: {ganancia_bruta.sum()}")
#EJERCICIO 7
print(f"\nEL INGRESO PROMEDIO POR PRODUCTO ES APROX: {np.mean(total):.2f}")
#EJERCICIO 8
print(f"\nEL PRECIO UNITARIO PROMEDIO ES APROX: {np.mean(precio)}")
#EJERCICIO 9
index = np.where(total == np.max(total))[0][0]
print(f"\nEL {nombres[index]} ES EL MAYOR INGRESO(+DES) CON: {np.max(total)}")
#EJERCICIO 10
index = np.where(ganancia_bruta== np.max(ganancia_bruta))[0][0]
print(f"\nEL {nombres[index]} ES EL MAYOR INGRESO DE GANANCIA BRUTA CON: {np.max(ganancia_bruta)}")
#EJERCICIO 11
print(f"\nLA SUMA DE PRODUCTOS VENDIDOS EN TOTAL ES (CANTIDAD VENDIDA): {cantidad.sum()}")
#EJERCICIO 12
descuento_aplicado = np.multiply(np.divide(descuento,100),np.multiply(cantidad, precio))
print(f"\nEL PROMEDIO DE DESCUENTOS APLICADOS ESTA EN: {np.mean(descuento_aplicado)}")
#EJERCICIO 13
print(f"\nEL TOTAL DE COSTO DE PRODUCCION DE TODOS LOS PRODUCTOS ES: {costo_produccion.sum()}")
#EJERCICIO 14
ingreso_total = total.sum()
costo_total = costo_produccion.sum()
porcentaje = (ingreso_total / costo_total) * 100
print(f"\nEL INGRESO TOTAL ES {porcentaje:.2f}% DEL COSTO TOTAL DE PRODUCCION.")
#EJERCICIO 15
print(f"\nLA RENTABILIDAD DE LA TIENDA ESTA EN UN {np.multiply(np.divide(ganancia_bruta.sum(),total.sum()),100):.1f}%")