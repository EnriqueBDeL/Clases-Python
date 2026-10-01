'''

Pandas es la herramienta definitiva en Python para el análisis y manipulación de datos tabulares (como si fuera un Excel hipervitaminado). 
Se construye directamente sobre NumPy, lo que significa que es igual de rápido, pero añade etiquetas a las filas y columnas para trabajar
con datos estructurados de forma mucho más intuitiva.

'''

# pip install pandas


import pandas as pd

# Pandas trabaja datos y etiquetas. 
# Esto se llama Serie

ventas = pd.Series([150, 200, 300, 100], index=["Lunes", "Martes", "Miércoles", "Jueves"])

print(ventas)

print("\n") 

print(ventas["Martes"])

print("\n")

# Es una tabla de datos de dos dimensiones (filas y columnas). Es una colección de Series que comparten el mismo índic
# Crear un DataFrame desde un diccionario

datos = {
    "Producto": ["Manzanas", "Naranjas", "Plátanos", "Peras"],
    "Precio": [1.50, 2.00, 1.20, 1.80],
    "Stock": [100, 50, 200, 80]
}

df = pd.DataFrame(datos)



print(df.head(2)) # Ver las primeras filas (por defecto 5)
print("\n")

print(df.info()) # Ver información general (tipos de datos, valores nulos, memoria)
print("\n")

print(df.describe()) # Resumen estadístico rápido de las columnas numéricas (media, min, max, etc.)
print("\n")

print(df.columns) # Ver solo los nombres de las columnas
print("\n")



# Filtrar y sleecionar datos

precios = df["Precio"] # Seleccionar una sola columna (devuelve una Series)
print(precios)
print("\n")

sub_df = df[["Producto", "Stock"]] # Seleccionar varias columnas (devuelve un nuevo DataFrame)
print(sub_df)
print("\n")

productos_caros = df[df["Precio"] > 1.50] # Filtrar filas con unacondición 
print(productos_caros)
print("\n")

filtrado = df[(df["Precio"] < 1.60) & (df["Stock"] > 80)] # Filtrar con múltiples condiciones (usar "&"" para AND, "|"" para OR, y paréntesis)
print(filtrado)
print("\n")




# Pandas facilita la creación de nuevos datos a partir de los existentes aplicando operaciones a columnas enteras.

print(df)

df["Valor_Total"] = df["Precio"] * df["Stock"] # Crear una nueva columna calculada

print(df)

df["Precio"] = df["Precio"] * 0.90 # Modificamos la columna "Precio" existente (aplicando un 10% de descuento)

print(df)




# Elimina la columna y guarda el resultado de nuevo en 'df'
df = df.drop("Stock", axis=1)

# Si quieres eliminar VARIAS columnas a la vez, le pasas una lista:
# df = df.drop(["Stock", "Valor_Total"], axis=1)

# Usa esto para eliminar una unica columna
# del df["Stock"] 



print(df)




df = df.drop(0) # Eliminar la fila con el índice 0

print(f"{df}\n")


# Eliminar filas usando una condición (ej. borrar las Peras)
# Básicamente es: "Me quedo con todo lo que NO sea Peras"
df = df[df["Producto"] != "Peras"] 
print(f"{df}\n")


# Después de borrar filas, los números del índice quedan salteados. 
# Así los reiniciamos para que empiecen desde cero otra vez:
df = df.reset_index(drop=True)
print(f"{df}\n")
