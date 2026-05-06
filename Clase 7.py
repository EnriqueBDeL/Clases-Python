# ---------------------------------------------------------
# 1. LAS TUPLAS (Listas que no pueden cambiar)
# ---------------------------------------------------------
# Las tuplas son casi idénticas a las listas, pero con una gran diferencia:
# son INMUTABLES. Una vez creadas, no puedes agregar, eliminar ni cambiar sus elementos.
# Se crean usando paréntesis ( ) en lugar de corchetes [ ].


 # Las tuplas on más rápidas que las listas y protegen datos sensibles de modificaciones accidentales.

print("--- TUPLAS ---") # Ideal para datos fijos.
coordenadas_madrid = (40.4168, -3.7038) 
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

print(f"Latitud de Madrid: {coordenadas_madrid[0]}")
print(f"El mejor día es el: {dias_semana[4]}")




# ---------------------------------------------------------
# 2. LOS DICCIONARIOS (Clave - Valor)
# ---------------------------------------------------------
# El equivalente directo al HashMap<String, Object> de Java.
# En lugar de acceder a los datos por su posición (0, 1, 2...),
# accedemos a ellos a través de un nombre o "clave". Se usan llaves { }.


print("\n--- DICCIONARIOS ---")
alumno = {
    "nombre": "Enrique",
    "edad": 25,
    "lenguaje_favorito": "Python",
    "calificaciones": [9, 8, 10]  # ¡Podemos meter listas dentro de diccionarios!
}

print(f"Nombre del alumno: {alumno['nombre']}") # Para leer un valor, usamos corchetes con el nombre de la clave
print(f"Primera nota: {alumno['calificaciones'][0]}")


print("\n")


alumno["edad"] = 26 # Modificar es tan fácil como reasignar

alumno["graduado"] = True # Si la clave no existe, Python la crea automáticamente.

print("--- DICCIONARIO ACTUALIZADO ---")
print(alumno)

print("\n")



# RECORRER UN DICCIONARIO CON UN FOR
# Los diccionarios tienen 3 métodos clave para iterar: 
# .keys() para las claves, .values() para los valores, y .items() para ambos.

print("--- ITERANDO EL DICCIONARIO ---")

for clave, valor in alumno.items(): # .items() nos permite desempaquetar la clave y el valor al mismo tiempo en el 'for'

    print(f"{clave}: {valor}")    

