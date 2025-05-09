import pandas as pd
datos_ventas = {
    "Fecha": ['2021-05-01', '2021-05-02', '2021-05-03', '2021-05-04', '2021-05-05', '2021-05-06', '2021-05-07','2021-05-08','2021-05-09','2021-05-10'],
    "Categoría del Producto": ['Balones', 'Zapatillas', 'Raquetas', 'Camisetas', 'Balones', 'Zapatillas', 'Raquetas','Camisetas','Balones','Zapatillas'],
    "Producto": [
        'Balón de Fútbol',
        'Zapatillas de Fútbol',
        'Raqueta de Tenis',
        'Camiseta de Entrenamiento',
        'Balón de Baloncesto',
        'Zapatillas de Running',
        'Raqueta de Badminton',
        'Camiseta de Fútbol',
        'Balón de Rugby',
        'Zapatillas de Tenis'
    ],
    "Precio": [30, 120, 150, 25, 40, 110, 90, 35, 50, 95],
    "Cantidad": [5, 2, 3, 10, 4, 1, 6, 2, 3, 7],
    "Método de Pago": [
        'Tarjeta de Crédito',
        'PayPal',
        'Efectivo',
        'Tarjeta de Crédito',
        'PayPal',
        'Efectivo',
        'Tarjeta de Crédito',
        'PayPal',
        'Efectivo',
        'Tarjeta de Crédito'
    ],
    "Ubicación": ['Quito', 'Guayaquil', 'Cuenca', 'Ambato', 'Quito', 'Guayaquil', 'Quito', 'Cuenca', 'Ambato', 'Guayaquil']
}
promociones_descuento = {
    'Categoría del Producto' : ['Balones','Zapatillas','Raquetas','Camisetas'],
    'Descuento (%)' : [10,15,5,20]
}
df = pd.DataFrame(datos_ventas)
df_pd = pd.DataFrame(promociones_descuento)

#1
df['Categoría del Producto'] = pd.Categorical(df['Categoría del Producto'])
df['Método de Pago'] = pd.Categorical(df['Método de Pago'])
print("\nTipo de dato actualizado a categorias\n",df.dtypes)

#2
desviacion = df['Precio'].std()
media = df['Precio'].median()
print(f"\nLA DESVIACIÓN ES DE: {desviacion:.2f}\nLA MEDIANA ES DE: {media:.2f}$\n")
df['Total ventas'] = df['Precio'] * df['Cantidad']
print("\nEl producto con mas ventas es:\n",df.loc[df['Total ventas'].idxmax()])
print("\nEl producto con menos ventas es:\n",df.loc[df['Total ventas'].idxmin()])

#3
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Dias desde ultima compra'] = (pd.to_datetime('2021-06-01') -df['Fecha'] ).dt.days
print("\nColumna de dias de ultima compra agregada\n",df)

#4
df_promociones = pd.merge(df,df_pd, on='Categoría del Producto', how="left")
df_promociones['Precio final'] = df_promociones['Precio'] - (df_promociones['Precio'] * (df_promociones['Descuento (%)']/100)) 
df_promociones['Total ventas'] = df_promociones['Precio final'] * df_promociones['Cantidad'] 
print("\nTabla con valores finales aplicando descuentos",df_promociones)
#PREGUNTA 1:
print("\nEl producto con mayor descuento es:\n",df_promociones.loc[df_promociones['Descuento (%)'].idxmax()])
#Las ventas que poseen mayor descuento aplicados son las de las camisetas, al poseer el descuento mayor de 20%

#5
# PREGUNTA 2
df_promociones.fillna({'Ubicación':'Desconocido'}, inplace=True)
# PREGUNTA 1
df_promociones.drop_duplicates(inplace=True)

#6
# PREGUNTA 4
df_categoria_p = df_promociones.groupby('Categoría del Producto')
sum_dfcp = df_categoria_p['Total ventas'].sum()
print("\nDatos agrupados por categoria para hallar la mayor venta por categoria\n",sum_dfcp)
#La que tuvo mayor ventas fue la categoria zapatillas con 1015

#PREGUNTAS DE REFLEXIONAR:
#1.Ademas de optimizar memoria que sera utilizada, proporciona utilizar varias funciones que permiten un analisis mas practico y eficaz
#2.Para poder obtener una vista general de como se vende tal producto y si terminara siendo rentable a largo plazo o corto plazo
#3.Ayudan a presenciar si hubo algun fallo en la promoción del producto desde el momento que se hizo la primera compra, permitiendo evitar una decadencia en las ventas de este producto
#4.Proporciona que exista un aumento en las ventas, ya que un descuento siempre se consider atractivo al cliente, y otorgarle esta viabilidad proporciona que exista una compra mas rentable, ya que pueden dispararse
#5.Para evitar problemas e incoherencias en los analisis y poseer una vista mas precisa