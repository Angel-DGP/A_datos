import numpy as np

datos = np.array([
    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    [15, 25, 35, 45, 55, 65, 75, 85, 95, 105],
    [20, 30, 40, 50, 60, 70, 80, 90, 100, 110],
    [25, 35, 45, 55, 65, 75, 85, 95, 105, 115],
    [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
    [35, 45, 55, 65, 75, 85, 95, 105, 115, 125],
    [40, 50, 60, 70, 80, 90, 100, 110, 120, 130],
    [45, 55, 65, 75, 85, 95, 105, 115, 125, 135],
    [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    [55, 65, 75, 85, 95, 105, 115, 125, 135, 145]
])
#PARTE 2 - 1
media_todos_10dias = np.mean(datos,axis=0)
for i in range(len(datos)):
    print(f"La media del producto {i+1} en los 10 dias es:{media_todos_10dias[i]}")
print("")
#PARTE 2 - 2
mediana_todos_10dias = np.median(datos,axis=0)
for i in range(len(datos)):
    print(f"La mediana del producto {i+1} en los 10 dias es:{mediana_todos_10dias[i]}")
print("")
#PARTE 2 - 3
desvia_todos_10dias = np.std(datos, axis=0)
for i in range(len(datos)):
    print(f"La desviación del producto {i+1} en los 10 dias es:{desvia_todos_10dias[i]}")
print("")
#PARTE 3 - 1
suma_total = np.sum(datos)
print(f"La venta total de los productos fue de: {suma_total}")
print("")
#PARTE 3 - 2 
minimos = np.min(datos, axis=0)
maximos = np.max(datos, axis=0)

for i in range(len(minimos)):
    print(f"Del producto {i+1} su mínimo fue de: {minimos[i]}, su máximo fue de: {maximos[i]}")
print("")
#PARTE 3 - 3 
suma_todos_10dias = np.sum(datos,axis= 0)
for i in range(len(suma_todos_10dias)): 
    print(f"La suma del producto {i+1} en los 10 dias es: {suma_todos_10dias[i]}")
print("")
#PARTE 4 - 1
datos_normalizados=(datos-np.min(datos))/(np.max(datos) - np.min(datos))
for i in range(len(datos)):
    print(f"DIA {i+1} {datos_normalizados[i]}")
#PARTE 4 - 2
datos_mas_10 = np.multiply(datos,1.1)
print("\nDATOS CON UN AUMENTO DEL 10%")
for i in range(len(datos)):
    print(f"DIA {i+1}",datos_mas_10[i])
    