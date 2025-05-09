import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#En este gráfic
url = "https://raw.githubusercontent.com/kevin19925/modulo5/31d3a23df48b1679c899d38ac212ee490d0bcaef/ventas_tienda.csv"

#EJERCICIO 1
df = pd.read_csv(url)
df.fillna({'Ciudad':'Desconocido'}, inplace=True)
df['Categoría'] = pd.Categorical(df['Categoría'])
df['Método_Pago'] = pd.Categorical(df['Método_Pago'])
df['Forma_Contacto'] = pd.Categorical(df['Forma_Contacto'])
df['Estado_Venta'] = pd.Categorical(df['Estado_Venta'])
df['Genero_Cliente'] = pd.Categorical(df['Genero_Cliente'])
df['Cupón_Usado'] = pd.Categorical(df['Cupón_Usado'])
df['Tipo_Cliente'] = pd.Categorical(df['Tipo_Cliente'])
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Fecha_Entrega'] = pd.to_datetime(df['Fecha_Entrega'])
df['Fecha_Registro_Cliente'] = pd.to_datetime(df['Fecha_Registro_Cliente'])

select_cat = df.groupby('Categoría')
select_cat = select_cat['Total_Venta'].sum()
select_cat = select_cat.reset_index()

'''sns.set_style("whitegrid", {'grid.linestyle': ':'})
sns.barplot(x='Categoría', y='Total_Venta', data=select_cat)
plt.title("Ingresos por Categoría de Producto")
plt.tight_layout()
plt.show()'''
#La categoria que tiene mas ventas es 'Libros', y le sigue 'Hogar'

#Metodo de pago mas usado
select_met = df['Método_Pago'].value_counts().reset_index()
select_met.columns = ['Método_Pago', 'Frecuencia']

'''sns.set_style("whitegrid", {'grid.linestyle': ':'})
sns.barplot(x='Método_Pago', y='Frecuencia', data=select_met)
plt.title("Frecuencia por Método de Pago")
plt.tight_layout()
plt.show()'''
#El grafico nos muestra que el metodo de pago mas usado es el 'Efectivo'

'''plt.hist(df['Edad_Cliente'], bins=30, color='skyblue', edgecolor='black')
plt.title("Histograma de la Edad")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()'''
#Se distribuyen con barritas, que nos dan a entender que la frecuencia de la edad mas usual es la de 54 años

#PRECIO VS CANTIDAD VENDIDA
'''plt.scatter(x=df['Precio_Unitario'], y=df['Total_Venta'])
plt.title("Gráfico de Dispersión")
plt.xlabel("Precio")
plt.ylabel("Total de ventas")
plt.show()'''
#Si, existe mucha relacion, en el cual el grafico nos demuestra como los precios mas caros tienen mayores ventas

#CLIENTE NUEVOS Y FRECUENTES
compras_por_tipo = df.groupby('Tipo_Cliente')['Total_Venta'].sum().reset_index()

'''sns.set_style("whitegrid", {'grid.linestyle': ':'})
sns.barplot(x='Tipo_Cliente', y='Total_Venta', data=compras_por_tipo, palette='Set2')

plt.title("Total de Compras por Tipo de Cliente")
plt.xlabel("Tipo de Cliente")
plt.ylabel("Total de Ventas")
plt.tight_layout()
plt.show()'''
#No, los clientes frecuentes compran mas que los nuevos

#CALIFICACION POR PROVINCIA
cal_provincia = df.groupby('Provincia')['Calificación_Cliente'].sum().reset_index()

'''sns.set_style("whitegrid", {'grid.linestyle': ':'})
sns.barplot(x='Provincia', y='Calificación_Cliente', data=cal_provincia, palette='Set2')

plt.title("Total de Calificación_Cliente")
plt.xlabel("Tipo de Provincia")
plt.ylabel("Total de Calificación_Cliente")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()'''

#La provincia con mejor calificacion del cliente es 'Rhode Island'

#TOP 10 EMPLEADOS POR VENTAS
top_10 = df.groupby('Empleado_Vendedor')['Total_Venta'].sum().sort_values(ascending=False).head(10).reset_index()
top_10.dropna()

'''
sns.set_style("whitegrid", {'grid.linestyle': ':'})
sns.barplot(x='Total_Venta', y='Empleado_Vendedor', data=top_10, palette='Set2')

plt.title("Total de ventas por empleado")
plt.xlabel("Empleado")
plt.ylabel("Ventas")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
'''

#El empleado con mayor ventas es Steven Martinez

#ESTADO DE ENTREGA
estado_ent = df['Estado_Entrega'].value_counts().reset_index()
estado_ent.columns = ['Estado_Entrega', 'Cantidad']

'''
sns.set_style("whitegrid", {'grid.linestyle': ':'})
sns.barplot(x='Estado_Entrega', y='Cantidad', data=estado_ent)
plt.title("Estado_Entrega")
plt.tight_layout()
plt.show()
'''
#El estado mas comun es el de 'Entregado'

#VENTAS CON CUPONES
cupones_top = df.groupby('Cupón_Usado')['Total_Venta'].sum().sort_values(ascending=False).reset_index()
print(df.dtypes)
'''
sns.set_style("whitegrid", {'grid.linestyle': ':'})
sns.barplot(x='Cupón_Usado', y='Total_Venta', data=cupones_top, palette='Set2')

plt.title("Tendencia cupones")
plt.xlabel("Cupón_Usado")
plt.ylabel("Total_Venta")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
'''
#Si, el uso de cupones aumenta drasticamente las ventas, llegando a subir al 400000

#DISTRIBUCION DE CALIFICACIONES
sns.boxplot(y=df["Calificación_Cliente"])
plt.title("Calificación_Cliente")
plt.show()

#Lo maximo ha sido 4.0, llegando a no tener valores atipicos, ademas de mostrar como el valor maximo es 5.0