'''

NumPy (Numerical Python) es la biblioteca principal para la computación científica en Python. 
Su gran ventaja frente a las listas tradicionales de Python es la velocidad y su capacidad para 
realizar operaciones matemáticas complejas en miles o millones de datos utilizando muy pocas líneas de código.

'''

#pip install numpy

import numpy as np



# A diferencia de las listas normales de Python, todos los elementos de un array de NumPy deben ser del mismo tipo (generalmente números), lo que permite que se procesen a una velocidad mucho mayor.


# Array de 1 dimensión (vector)
vector = np.array([1, 2, 3, 4, 5])

# Array de 2 dimensiones (matriz)
matriz = np.array([[1, 2, 3], 
                   [4, 5, 6]])


# Funciones muy útiles para crear arrays pre-llenados

ceros = np.zeros(5)             # [0., 0., 0., 0., 0.]


unos = np.ones((2, 3))          # Matriz de 2 filas y 3 columnas llena de unos


pares = np.arange(0, 10, 2) # [0, 2, 4, 6, 8] (inicio, fin excluido, saltos)




# Cuando trabajas con un conjunto de datos, necesitas saber qué forma tiene. NumPy te ofrece atributos directos para inspeccionar cualquier array:

print(matriz.ndim)   # 2 (Número de dimensiones)

print(matriz.shape)  # (2, 3) (Tupla que indica 2 filas, 3 columnas)

print(matriz.size)   # 6 (Cantidad total de elementos en el array)

print(matriz.dtype)  # int64 (Tipo de dato, ej. enteros de 64 bits)




# Con Numpy no necesitas hacer bucles for para operar sobre los datos. Las operaciones matemáticas se aplican directamente elemento por elemento (esto se llama vectorización).



precios = np.array([100, 200, 300])

precios_con_iva = precios * 1.21  # Multiplicar todos los elementos por 1.21 (ej. calcular impuestos)

print(precios_con_iva)



costos = np.array([50, 50, 50])

ganancia = precios - costos # Calculo entre arrays

print(ganancia)




# Puedes acceder a partes específicas de un array utilizando los corchetes [], separando las dimensiones por comas.


numeros = np.array([10, 20, 30, 40, 50])

print(numeros[0])     # 10 (El primer elemento)

print(numeros[1:4])   # [20, 30, 40] (Desde el índice 1 hasta el 3)


# En una matriz de 2D (filas, columnas)
matriz_3x3 = np.array([[1, 2, 3], 
                       [4, 5, 6], 
                       [7, 8, 9]])

print(matriz_3x3[0, 1])   # 2 (Fila 0, Columna 1)

print(matriz_3x3[:, 2])   # [3, 6, 9] (El ":" significa todas las filas, solo la columna 2)
