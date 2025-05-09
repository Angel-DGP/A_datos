import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
datos = {
    "Producto": ["E", "F", "G", "D", "E", "F", "G", "H", "I", "J"],
    "Fecha": [
        "2021-06-01", "2021-06-01", "2021-06-02", "2021-06-03", "2021-06-03",
        "2021-06-04", "2021-06-05", "2021-06-05", "2021-06-06", "2021-06-06"
    ],
    "Categoría": [
        "Electrónica", "Ropa", "Alimentación", "Electrónica", "Ropa",
        "Alimentación", "Electrónica", "Ropa", "Alimentación", "Electrónica"
    ],
    "Precio": [120, 50, 20, 150, 90, 10, 200, 80, 15, 130],
    "Unidades Vendidas": [15, 30, 50, 5, 12, 60, 8, 25, 40, 10],
    "Costo de Producción": [80, 30, 10, 100, 50, 5, 120, 40, 7, 70],
    "Método de Pago": [
        "Tarjeta de Crédito", "PayPal", "Efectivo", "Tarjeta de Crédito", "PayPal",
        "Efectivo", "Tarjeta de Crédito", "PayPal", "Efectivo", "Tarjeta de Crédito"
    ],
    "Ciudad": [
        "Quito", "Cuenca", "Guayaquil", "Loja", "Ambato",
        "Quito", "Guayaquil", "Cuenca", "Quito", "Loja"
    ]
}
df = pd.DataFrame(datos)

#2 - MANIPULACION DE DATOS
#PREGUNTA 1     
print("\nEl tipo de dato de cada columna\n",df.dtypes)

#PREGUNTA 2
df['Fecha'] = pd.to_datetime(df['Fecha'])
#Es importante ya que nos permite poder realizar operaciones con estas sin tantas dificultades y mas eficazes

#PREGUNTA 3
df['Categoría'] = pd.Categorical(df['Categoría'])
df['Método de Pago'] = pd.Categorical(df['Método de Pago'])
#Permite no poseer un gasto inecesario de memoria, ademas de permitir trabajar con estos datos mas eficazmente

#PREGUNTA ANALISIS PARTE 2
#1. Permite poder hacer operaciones matemáticas mas eficaz, ademas de permitir poder extraer un dato de la fecha (dia,mes, año) y podremos realizar filtrados por rangos de fecha
#2. Permite poder guardar los datos en enteros para ahorrar la materia, y esto acelera la funcion "groupby" 

#3 -Estadisticas descriptivas
#EJERCICIO 1
media = df['Unidades Vendidas'].median()
std = df['Unidades Vendidas'].std()
print(f"\nmedia:\n{media}\nstd:\n{std}")

#PREGUNTA 4
#1. La media nos indica un valor aproximado de todos los datos, permitiendo sacar conclusiones de datos gigantes, de un valor como su nombre lo indica, media que nos muestra el valor de la mitad de todos los datos
#2. La desviación nos indica lo alejado que estan los valores de un aproximado, es decir hay valores muy gigantes y tambien valores muy pequeños, nos indica lo alejado significa que los valores no estan cerca del promedio todos

#PREGUNTA ANALISIS PARTE 3
#1. Nos ayuda a detectar valores atipicos, y aportan dando valores completos, pudiendo hayar los valores extremos o sospechosamente fuera de lugar
#2. La media nos dice el promedio de unidades vendidas, pero no nos muestra si los datos están concentrados o dispersos, se necesitan los dos

#4 -CALCULO DE CORRELACIÓN
correlacion = df[['Unidades Vendidas','Precio']].corr()
print("\nCORRELACION DE UNIDADES VENDIDAS Y PRECIO\n",correlacion)

#PREGUNTA 6
#1. La correlacion nos dice que su relacion es extremedamente fuerte
#1. La correlacion es negativa
#2. Significa que mientras el precio sube de un producto, la venta disminuye

#PREGUNTA ANALISIS PARTE 4
#1. Esto afectaria de tal manera que habria rentabilidad para subir precios sin riesgo a perder ventas
#2. Tendria un efecto negativo, ya que proporciona que las ventas disminuyen cuando los precios suben

#5 -DETECCIÓNde OUTLIERS Y CÁLCULO DE CUARTILES
#1. [
q1=df["Unidades Vendidas"].quantile(0.25)
q3=df["Unidades Vendidas"].quantile(0.75)

iqr = q3-q1
#]
#PREGUNTA 7
#Los cuartiles son valores que dividen un conjunto de datos ordenado en cuatro partes iguales. Cada parte contiene el 25% de los datos.
#Son las medias de cierto datos de un diccionario, es decir del 25% del diccionario la media de este es 'x', con el 50% es la media de esto la cual seria el ultimo valor del 25% esto seria parecido con el 75% en este seria la media de esos datos 
#Con el IQR podemos sacar los limites inferiores y superiores, en los cuales cuando un valor pasa de estos, se le considera un outlier

#2. [
limite_superior = q3+1.5*iqr
limite_inferior = q1-1.5*iqr
print("\nEl limite inferior es:\n",limite_inferior)
print("\nEl limite superior es\n",limite_superior)
#]

#PREGUNTA 8
#El limite inferior es '-30.0' y el superior es '78.0'
#No existe ningun producto con un valor fuera de estos limites

#3.[
z_scores = stats.zscore(df['Unidades Vendidas'])
print(z_scores)
#]

#PREGUNTA 9
#Un zScore es una desviación del valor estandar, es decir, son los valores convertidos en valores comunes diciendo que el 0 es la media y arriba de este es que esta por encima de la media, lo contrario si es debajo del 0
#Cuando un zScore esta por arriba del 2, si es 2 puede ser un outlier moderado, si esta arriba de este es un outlier definitivamente

#PREGUNTA ANALISIS PARTE 5
#1. Pueden afectar gravemente si no son detectados a tiempo, lo ideal seria sobrestimar la demanda y terminar con el exceso de stock eso en un pico anormal de ventas
#en estrategias de venta un outlier puede hacer creer que se vendio un producto a un precio elevado, cuando en realidad fue un caso aislado
#2. Porque no se ve afectado por los valores extremos, estos al detectar valores anomalos permiten evitar ser engañados por datos sin relevancia

#6 -DETECCIÓN DE OUTLIERS Y REMPLAZO DE VALORES
#1. [
filtrado = df[(z_scores>2 ) | (z_scores <-2)]
print("\nFiltrado de zScores\n",filtrado)
#]
#PREGUNTA 10
#1. Ningun producto posee un outlier
#2. Significa que existe un outlier y se lo debe tratar

#2. [
df['V Reemplazadas'] = np.where((z_scores<-2) | (z_scores>2), media,df['Unidades Vendidas'])
print("\nTabla con la columna de ventas reemplazadas:\n",df)
#]
#PREGUNTA 11
#1. El conjunto de datos no cambia en nada relevante, solo se agrega la columna de ventas reemplazadas pero mantiene los mismo valores de unidades vendidas
#2. No posee ningun impacto, ya que no existen outliers en el conjunto de datos

#PREGUNTA ANALISIS PARTE 6
#1. Desde mi punto de vista, si, esto permite sacar estadisticas mas acertadas, permitiendo no cometer errores o conclusiones de datos erroneos o no veridicos
#2. Podriamos simplemente borrandolos, o dandoles el valor promedio

#7 -VISUALIZACIÓN DE DATOS
#1 [

plt.boxplot(df["Unidades Vendidas"])
plt.title("BOX SPLOT VENTAS")
plt.show()
#]

#PREGUNTA 12
#1. Nos muestra que un promedio es por el valor del 21, ademas de que los limites se encuentran en 0 al 60, siendo que los datos empiezan por el 12 hasta lo que parece ser el 38
#ademas, el grafico incluye unos topes con forma de 'T' que llegan desde los datos mas extremos, siendo que empiezan desde el 38 al 60 y respectivamente abajo es 10 al 1
#2. Los outliers los identificamos cuando se muestran ciruclos 'o' dispersos por el plano

#PREGUNTA ANALISIS PARTE 7
#1. Es muy útil a la hora de hallar irregularidades
#2. Que las ventas llegan al 38 lo que parece ser, por arriba del 10, ademas de incluir una linea roja que parece indicar el promedio que esta ubicado en el 18 parece ser


