import pandas as pd
#diccionario
datos = {'nombre':['jose','kevin','anuel'],
         'edad':[10,20,30],
         'ciudad': ['quito','cuenca','machala']
         }
dt = pd.DataFrame(datos)
print(dt)
print("Nombres")
print(dt['nombre'])

#series
edades = pd.Series([22,23,24])
print(edades)

#fechas
fechas = pd.to_datetime(["2025-04-02","2025-04-03","2025-04-04"])
dt['fechas'] = fechas
print("Nuevo date")
print(dt['fechas'])

dt["año"] = dt["fechas"].dt.year
print(dt['año'])

dt['mayor_a_20'] = dt["edad"]>20
print(dt['mayor_a_20'])

mayor_q_20=dt[dt["edad"]>20]
print(mayor_q_20)