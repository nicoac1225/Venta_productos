import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Abro el archivo csv y lo convierto en un DataFrame
df = pd.read_csv('ventas_productos.csv', sep=";")
print (df)

#Defino función para calcular Precio total
def calcular_precio_total(cantidad, precio):
    return cantidad*precio

#Aplico función al DataFrame
df['Precio_Total'] = df.apply(lambda row: calcular_precio_total(row['Cantidad'], row['Precio']), axis=1)
print("\n DataFrame con el Precio Total")
print (df)

#Creo grafico de barras a partir del DataFrame y lo guardo como imagen
plt.bar(df['Producto'], df['Precio_Total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title ('Precio Total por Producto')
plt.savefig('Grafico_Precios.png')
plt.show()