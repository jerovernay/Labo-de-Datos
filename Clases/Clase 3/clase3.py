import pandas as pd

#1ra Parte

nombre_archivo = 'clase3-datos.csv'

df = pd.read_csv(nombre_archivo)

reducir = ['provincia','longitud' ,'latitud']
df_reducido = df[reducir]

provincias = ['Córdoba', 'Buenos Aires', 'San Juan']
df2 = df_reducido[df_reducido['provincia'].isin(provincias)]

df_Córdoba = df_reducido[df_reducido['provincia'] == 'Córdoba'].copy()
df_BuenosAires = df_reducido[df_reducido['provincia'] == 'Buenos Aires'].copy()
 

#print(df_Córdoba.sample(10))
#print(df_BuenosAires.sample(10))


def triangular(dataframe):
    suma:float = 0
    
    for value in dataframe['latitud']:
        suma += value
        
    return suma/len(dataframe['latitud'])
    

#print(f"Promedio de Latitud de Cordoba : {triangular(df_Córdoba)}")
#print(f"Promedio de Latitud de Buenos Aires : {triangular(df_BuenosAires)}")

# Forma FACIL (funciona)
# def triangular(dataframe):
#     return dataframe['latitud'].mean()

import matplotlib.pyplot as plt

# fig, ax = plt.figure()

# ax.bar()

transportes = 'respuestas.csv'

df = pd.read_csv(transportes, encoding = 'latin1')
df.rename(columns = {'¿Cuál es el transporte que utilizó hoy para llegar a Ciudad Universitaria?' : 'transporte'}, inplace = True)

res = df['transporte'].value_counts()

plt.bar(df['transporte'].unique(), res)

plt.show()

