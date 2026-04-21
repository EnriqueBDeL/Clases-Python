# Esto es un comnetario en Python.


# A diferencia de Java (que requiere crear una clase y un 'public static void main'),
# en Python solo necesitas una línea para mostrar información en pantalla:

print("¡Hola Mundo! Bienvenidos a las clases de Python.")

print("\n Hola desde la otra linea.") # \n imprime un salto de línea



# En Python, no necesitas declarar el tipo de variable (int, String, boolean) antes de usarla.
# Python lo descubre automáticamente (a esto se le llama "tipado dinámico").

nombre = "Enrique"       # Tipo String (cadena de texto). Puedes usar comillas dobles "" o simples ''.
letra = 'A'              # Tipo String (cadena de texto). En Python, un solo carácter es simplemente una cadena de texto (str) que tiene una longitud de 1.
edad = 20                # Tipo Integer (número entero).
altura = 1.75            # Tipo Float (número decimal). Se usa punto, no coma.
le_gusta_programar = True # Tipo Boolean (Verdadero o Falso). Nota que la primera letra va en mayúscula (True/False).



print("\nNombre del alumno:", nombre)
print("Edad:", edad)

print("\n")



# Para unir texto con variables, la forma más moderna y limpia en Python
# es usar las "f-strings" (format strings).
# Solo colocas una letra 'f' antes de las comillas y pones las variables entre llaves {}.


presentacion = f"Hola, me llamo {nombre}, tengo {edad} años y mido {altura} metros."
print("Ejemplo de f-string:")
print(presentacion)



#Otras formas de imprimir:
print("\nOtras formas de imprimir:")
print("1. Me llamo", nombre, "y tengo", edad, "años.")

print("2. Me llamo " + nombre + " y tengo " + str(edad) + " años.")

# Si vienes de C, esto te será muy familiar (printf).
# %s es para String, %d es para enteros (dígitos). Ya casi no se usa.
print("3. Me llamo %s y tengo %d años." % (nombre, edad))


# Pones llaves vacías {} donde quieres que vayan las variables,
# y luego se las pasas en orden dentro de .format()
print("4. Me llamo {} y tengo {} años.".format(nombre, edad))



print("\n")



# Si alguna vez tienes dudas de qué tipo de dato guarda una variable,
# puedes usar la función type()

print("El tipo de dato de la variable 'nombre' es:", type(nombre))
print("El tipo de dato de la variable 'edad' es:", type(edad))
