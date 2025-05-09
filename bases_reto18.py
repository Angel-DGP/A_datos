import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np


data = {
    'Producto' : ['A','B','C','D','A','B','C','D','A','B'],
    'Ventas' : [20000,150,250,300,230,190,270,320,210,180],
    'Precio' : [15.5,20.0,22.5,30.0,15.5,20.0,22.5,30.0,15.5,20.0]
}
df = pd.DataFrame(data)
print(df)

media = df['Ventas'].mean()
std = df['Ventas'].std()
print(media)
print(std)

print("\n des \n")
print(df.describe())

correlacion = df[['Ventas','Precio']].corr()
print("\n",correlacion)

q1=df["Ventas"].quantile(0.25)
q3=df["Ventas"].quantile(0.75)

iqr = q3-q1

limite_superior = q3+1.5*iqr
limite_inferior = q1-1.5*iqr

filtro = df[(df["Ventas"]<limite_inferior) | (df['Ventas']>limite_superior)]
print(filtro)

z_scores = stats.zscore(df['Ventas'])
df['Ventas_Z'] = z_scores
#print(df)

filtro2 = df[(z_scores>2 ) | (z_scores <-2)]

print(filtro2)

plt.boxplot(df["Ventas"])
plt.title("BOX SPLOT VENTAS")
plt.show()

df['Ventas_reemplazadas'] = np.where((z_scores<-2) | (z_scores>2), media,df['Ventas'])

print(df)