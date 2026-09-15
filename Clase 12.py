# ===============================================================================================
# USO DE LIBRERÍAS (MÓDULOS) EN PYTHON
# ===============================================================================================

"""
Nota sobre las Librerías Estándar:
Las librerías utilizadas en este archivo (math, random, time, os) forman parte de la
'Biblioteca Estándar de Python' (Python Standard Library). Esto significa que vienen
integradas e instaladas por defecto con el propio lenguaje Python. Por tanto, no requieren
ser descargadas de internet mediante gestores de paquetes (como pip) para poder ser utilizadas;
están listas para ser importadas en cualquier instalación básica de Python.
"""

# ===============================================================================================
# 1. FORMAS DE IMPORTAR LIBRERÍAS
# ===============================================================================================

# --- MÉTODOS BÁSICOS DE IMPORTACIÓN ---

# A) Importar la librería completa.

import math # Proporciona acceso a funciones matemáticas definidas en el estándar C.

resultado = math.sqrt(25) # Usamos la función 'sqrt' (raíz cuadrada) referenciando su origen 'math'.
print("1. Importación básica de math:", resultado)



# B) Importar con un alias (apodo).

import math as m # Útil para abreviar el nombre de librerías largas y agilizar la escritura del código.

resultado = m.sqrt(25) # Se invoca utilizando el alias 'm'.
print("2. Librería math con alias 'm':", resultado)


# C) Importar una función específica.

from math import sqrt # Importa únicamente el componente necesario en lugar de todo el módulo, ahorrando memoria y permitiendo usar la función directamente sin el prefijo del módulo.

resultado = sqrt(25)
print("3. Función sqrt importada directamente:", resultado)


# ===============================================================================================
# 2. LIBRERÍAS TÍPICAS DE LA BIBLIOTECA ESTÁNDAR
# ===============================================================================================

# -----------------------------------------------------------------------------------------------
# LIBRERÍA RANDOM
# Propósito: Implementa generadores de números pseudoaleatorios para diversas distribuciones.
# Se utiliza comúnmente en simulaciones, juegos, cifrado básico y selección de muestras aleatorias.
# -----------------------------------------------------------------------------------------------
import random

numero_suerte = random.randint(1, 10) # Genera un número entero aleatorio entre 1 y 10 (ambos incluidos).
print("\n[Librería RANDOM]")
print("Número generado aleatoriamente:", numero_suerte)

opciones = ["Piedra", "Papel", "Tijera"]
eleccion_pc = random.choice(opciones) # Selecciona un elemento aleatorio de una secuencia (como esta lista).
print("Selección aleatoria de la lista:", eleccion_pc)


# -----------------------------------------------------------------------------------------------
# LIBRERÍA TIME
# Propósito: Proporciona funciones para manipular fechas, formatos de hora y medir el rendimiento
# del código. Permite interactuar con el reloj del sistema.
# -----------------------------------------------------------------------------------------------
import time

print("\n[Librería TIME]")
print("Ejecutando proceso...")
time.sleep(2)  # Suspende la ejecución del programa durante el número de segundos especificado.
print("El proceso ha finalizado tras una pausa de 2 segundos.")


# -----------------------------------------------------------------------------------------------
# LIBRERÍA OS (Operating System)
# Propósito: Proporciona una interfaz portátil para interactuar con las funcionalidades dependientes
# del sistema operativo (Windows, macOS, Linux). Permite gestionar archivos, directorios y procesos.
# -----------------------------------------------------------------------------------------------
import os

carpeta_actual = os.getcwd() # Devuelve una cadena de texto que representa el directorio de trabajo actual (Current Working Directory).
print("\n[Librería OS]")
print("El directorio de trabajo actual es:", carpeta_actual)
