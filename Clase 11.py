# LECTURA Y ESCRITURA DE ARCHIVOS (.txt)

# La estructura 'with' abre el archivo, nos permite trabajar con él y lo CIERRA AUTOMÁTICAMENTE al terminar.

# Parámetros importantes de open():
# - Nombre del archivo (ej. "datos.txt")
# - Modo: 'w' (Write) sobrescribe todo el archivo o lo crea si no existe.
# - encoding="utf-8": Crucial para guardar tildes y caracteres especiales (ñ).


print("--- 1. CREANDO Y ESCRIBIENDO EN EL ARCHIVO ---")
nombre_archivo = "alumnos.txt"


with open(nombre_archivo, "w", encoding="utf-8") as archivo:
    archivo.write("Lista de Alumnos del Curso de Python:\n")
    archivo.write("1. Enrique\n")
    archivo.write("2. Juan\n")
    
print(f"¡El archivo '{nombre_archivo}' fue creado exitosamente!")


#-----------------------------------------------------------------------------------------------------------------------|

# Si abrimos un archivo existente en modo 'w', borraríamos lo que ya tiene.
# Para añadir texto al final sin borrar nada, usamos el modo 'a' (Append).


print("\n--- 2. AÑADIENDO MÁS CONTENIDO ---")

with open(nombre_archivo, "a", encoding="utf-8") as archivo:
    archivo.write("3. Yohan (Agregado después)\n")

print("Se ha añadido a Carlos al final del archivo.")


#-----------------------------------------------------------------------------------------------------------------------|

# El modo 'r' es para leer. Es el modo por defecto de la función open().


print("\n--- 3. LEYENDO EL ARCHIVO COMPLETO ---")

with open(nombre_archivo, "r", encoding="utf-8") as archivo:  # .read() lee absolutamente todo el contenido y lo guarda como un String gigante
    contenido_total = archivo.read()
    print(contenido_total)


#-----------------------------------------------------------------------------------------------------------------------|

# Lectura Linea por linea

print("--- 4. LEYENDO LÍNEA A LÍNEA (IDEAL PARA ARCHIVOS GRANDES) ---")

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        texto_limpio = linea.strip()         # Usamos .strip() para limpiar los saltos de línea invisibles (\n)  que quedan al final de cada oración en el archivo de texto.
        print(f"Procesando -> {texto_limpio}")

 #-----------------------------------------------------------------------------------------------------------------------|

# Leer cantidad especifica de lineas

print("\n\n--- LEER Nº LINEAS ESPECIFICAS ---")

print("\n--- OPCIÓN 1: .readline() manual ---")
with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    primera_linea = archivo.readline()# .readline() (en singular) lee exactamente UNA línea y mueve el "cursor" a la siguiente.
    segunda_linea = archivo.readline()
    
    print("Línea 1:", primera_linea.strip())
    print("Línea 2:", segunda_linea.strip())

 #.....................................................................................................      

print("\n--- OPCIÓN 2: Usar un bucle para las primeras N líneas ---")
lineas_a_leer = 2

with open(nombre_archivo, "r", encoding="utf-8") as archivo:
    for i in range(lineas_a_leer):
        linea = archivo.readline()
        # Si el archivo tiene menos líneas de las que pedimos, 
        # readline() devuelve texto vacío (""), así que podemos frenar para no imprimir en blanco.
        if linea == "":
            break 
        
        print(f"Línea {i + 1}: {linea.strip()}")
