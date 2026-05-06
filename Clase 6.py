# Para declarar una función, en Python usamos la palabra reservada 'def' seguida del nombre de la función y paréntesis (). 

def saludar():
    print("¡Hola! Esta es mi primera función en Python.")


print("--- LLAMANDO A LA FUNCIÓN ---")
saludar()
saludar() 



# Los parámetros son variables que la función necesita para trabajar. No tienes que declarar qué tipo de dato son (ni String, ni int).

def saludar_persona(nombre, edad):
    print(f"Hola {nombre}, he visto que tienes {edad} años.")

print("\n--- FUNCIONES CON PARÁMETROS ---")
saludar_persona("Enrique", 25)
saludar_persona("Ana", 30)



print("\n")



def sumar(a, b):
    resultado = a + b
    return resultado #devuelve un valor


print("--- DEVOLVIENDO VALORES ---")
mi_suma = sumar(10, 15) # Guardamos el resultado en una variable
print(f"El resultado de la suma es: {mi_suma}")


print(f"\nSumando 10 + 15: {sumar(10, 15)}") # Podemos usar la función directamente dentro de un print


print("\n")



def crear_perfil(nombre, pais="España"): # pais es un parametro con un valor por defecto
    print(f"Usuario: {nombre} | Región: {pais}")



print("--- PARÁMETROS POR DEFECTO ---")
crear_perfil("Carlos") # Si no le paso el país, usará "España" por defecto


crear_perfil("María", "México")# Si le paso el país, sobrescribe el valor por defecto
