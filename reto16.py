from sklearn.preprocessing import MinMaxScaler as mm
import pandas as pd
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

#EJERCICIO 1
df = pd.read_csv(url)
df.head()
select = df[df["Age"]>30]
select = select[select["Pclass"]==1]
print("Mayores a 30 anios y aquellos q viajaron en primera clase \n",select[["Name","Age"]])

#EJERCICIO 2
def convertir_meses(edad):
  if 	pd.notnull(edad):
    return edad * 12
df['Age_Months'] = df["Age"].apply(convertir_meses)
print('ANIOS CONVERTIDOS EN MESES \n',df[["Name",'Age','Age_Months']])

#EJERCICIO 3
df.dropna(subset=['Age'], inplace=True)
df.fillna({'Embarked':'S'}, inplace=True)
df.drop_duplicates(subset='Name', inplace=True)
print('DATOS NULOS DE -AGE- ELIMINADOS/ DATOS DE EMBARKED RELLENADOS/ DATOS DUPLICADOS EN -NAME- ELIMINADOS\n',df[['Name','Age','Embarked']])

#EJERCICIO 4
select = df[df['Survived']==1]
select = select.groupby('Pclass')
print('SOBREVIVIENTES POR CLASE',select.size())

#EJERCICIO 5
df['Sex'] = pd.Categorical(df['Sex'])
print('COLUMNA -SEX- CONVERTIDA A CATEGORIA/ NO ES NECESARIO CONVERTIR FARE A FLOAT. YA LO ES\n',df.head())
print(df.dtypes)
#No es necesario convertir Fare en float. Ya es

#EJERCICIO 6
normalizador = mm()
df['Age_Normalized'] = normalizador.fit_transform(df[["Age"]])
print('EDADES NORMALIZADAS\n',df.head())