import pandas as pd
#---------------------EJERCICIO 1---------------------#
print("\nEJERCICIO 1\n")
#diccionario
datos = {'nombre':['Juan','Ana','Carlos','Maria','Luis'],
         'edad':[18,22,20,19,21],
         'ciudad': ['Quito','Guayaquil','Loja','Cuenca','Ambato'],
         'promedio' : [9.5,8.0,7.5,9.0,8.5]
         }
dt = pd.DataFrame(datos)

#promedio
print("PROMEDIOS\n",dt['promedio'])

#aprobado
dt['aprobado'] = dt["promedio"]>=8
print("APROBADOS\n",dt['aprobado'])

aprobados=dt[dt["promedio"]>=8]
print("DATAFRAME + APROBADOS\n",aprobados['nombre'])

#---------------------EJERCICIO 2---------------------#
print("\nEJERCICIO 2\n")
eventos = {
    'Evento' : ['Concierto','Conferencia','Seminario','Feria','Taller'],
    'Fecha' : ['2025-05-01','2025-06-15','2025-07-10','2025-08-25','2025-09-05'],
    'Lugar' : ['Quito','Guayaquil','Loja','Cuenca','Ambato']
}
dt = pd.DataFrame(eventos)
#Convertir
dt['Fecha'] = pd.to_datetime(dt['Fecha'])
#Extraer de año y mes
dt["año"] = dt["Fecha"].dt.year
dt["mes"] = dt["Fecha"].dt.month

#Filtrado de eventos 2025
ocurridos_2025=dt[dt["año"]==2025]
print("\nEVENTOS QUE OCURRIRAN EN 2025:\n",ocurridos_2025[['Evento','Lugar']])
#Filtrado de eventos septiembre
en_sep = dt[dt['mes']==9]
print("\nEVENTO QUE OCURRIRA EN SEPTIEMVRE:\n",en_sep)
#Dias hasta el evento
dt['Dias hasta el evento'] = dt['Fecha'] - pd.to_datetime('2025-4-22')
print("\nDIAS HASTA EL EVENTO\n",dt)

#---------------------EJERCICIO 3---------------------#
print("\nEJERCICIO 3\n")
venta_productos = {
    'Producto' : ['Laptop','Celular','Tablet','Auriculares','Teclado'],
    'Precio' : [500,300,150,50,75],
    'Cantidad Vendida' : [10,15,7,25,30],
    'Fecha de venta': ['2025-04-01','2025-04-03','2025-04-05','2025-04-06','2025-04-10']
}
dt = pd.DataFrame(venta_productos)
dt['Fecha de venta'] = pd.to_datetime(dt['Fecha de venta'])
print("\nCon fecha de venta\n",dt)

#Columna de ingreso total
dt['Ingreso Total'] = dt['Precio'] * dt['Cantidad Vendida']
#Mayor a 1000
print("\nCon ingreso total\n",dt[dt['Ingreso Total']>1000])

#Mes de venta
dt['Mes de venta'] = dt['Fecha de venta'].dt.month

#Ocurridos en abril
en_abril = dt[dt['Mes de venta']==4]
print("\nOcurridos en abril\n",en_abril['Cantidad Vendida'])

#---------------------EJERCICIO 4---------------------#
print("\nEJERCICIO 4\n")

temperaturas = pd.Series([18.5,20.3,22.0,21.8,19.7,20.1,21.4], index=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'])
print("\nTemperaturas\n",temperaturas)

#Lunes, miercoles, viernes
print("\nOcurridos en dias especificos\n",temperaturas[['Lunes','Miercoles','Viernes']])

#Temperatura media
print("\nLa temperatura media de la semana es: \n",temperaturas.median())

#Nueva Serie Fahrenheit
t_fahrenheit = pd.Series(temperaturas * 9/5+ 32)
print("\nEn fahrenheit\n",t_fahrenheit)

#Temperatura max o min
print(f"\nLa temperatura mas alta es {t_fahrenheit.max()} y la mas baja {t_fahrenheit.min()} de la semana")

#---------------------EJERCICIO 5---------------------#
print("\nEJERCICIO 5\n")

asistencia = {
    'Estudiante' : ['Ana','Luis','Carlos','Maria','Pedro'],
    'Dias asistidos' : [20,18,22,15,19],
    'Mes' : ['Abril','Abril','Abril','Abril','Abril']
    }
dt = pd.DataFrame(asistencia)
print("\nAsistencia\n",dt)

#Total de dias
dt['Total dias en el mes'] = 30
print("\nCon total de dias\n",dt)

#Asistencia (%)
dt['Asistencia (%)'] = ((dt['Dias asistidos'] / dt['Total dias en el mes']) * 100).round(2)
print("\nCon asistencia en porcentajes\n",dt)

#Filtrado mayor a 80% asistencia
mayor_a_80 = dt[dt['Asistencia (%)']>80]
print("\nMayores a 80% de asistencia\n",mayor_a_80)

#Ordenado
ordenado = dt.sort_values(by="Asistencia (%)", ascending=False)
print("\nOrdenados de mayora menor\n",ordenado)

#---------------------EJERCICIO 6---------------------#
print("\nEJERCICIO 6\n")

ingresos_egresos = {
    'Fecha' : ['2025-03-01','2025-03-05','2025-03-10','2025-03-15','2025-03-20'],
    'Ingreso' : [1500,1200,2000,1800,1600],
    'Egreso' : [500,700,600,800,400]
}
dt = pd.DataFrame(ingresos_egresos)
#Convertir fecha
dt['Fecha'] = pd.to_datetime(dt['Fecha'])
print("\nFecha convertida\n",dt)

#Saldo
dt['Saldo'] = dt["Ingreso"] - dt["Egreso"]
print("\nCon saldo\n",dt)

#Filtrar
positivo = dt[dt['Saldo']>=0]
print("\nValores positivos de saldo\n",positivo[['Fecha','Saldo']])