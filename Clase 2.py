# Para pedir datos al usuario usamos input(). 
# OJO: input() SIEMPRE devuelve un String (texto), aunque escribas números.
# Si queremos hacer operaciones matemáticas, debemos convertir ese texto (Casting).

nombre_usuario = input("¿Cuál es tu nombre? ")

print("\n")

edad_numero = int(input("¿Cuántos años tienes? "))

print("\nHola", nombre_usuario, ", veo que tienes", edad_numero, "años.\n")



print("-" * 40) # Puedes multiplicar un string para repetirlo en pantalla. En este caso va a imprimir 40 veces el caracter "-".


# Python tiene operadores matemáticos por defecto.

a = 10
b = 3

print("\n--- OPERACIONES MATEMÁTICAS ---")
print(f"Suma: {a} + {b} = {a + b}")
print(f"Resta: {a} - {b} = {a - b}")
print(f"Multiplicación: {a} * {b} = {a * b}")
print(f"División exacta (Float): {a} / {b} = {a / b}")  # En Python la división siempre da decimal (float)
print(f"División entera (Omitir decimales): {a} // {b} = {a // b}") # A si puedes redondear el resultado.
print(f"Módulo (Resto de la división): {a} % {b} = {a % b}")
print(f"Potencia ({a} elevado a {b}): {a} ** {b} = {a ** b}")


print("\n")
print("-" * 40)


print("\n--- OPERADORES LÓGICOS ---")


es_mayor_de_edad = 23 >= 18
tiene_identificacion = True
puede_entrar = es_mayor_de_edad and tiene_identificacion # 'and' es el "Y" logico. Por lo que ambas deben ser Verdaderas. Equivale al simbolo "&&" de Java y C
print("¿Es mayor de edad y tiene ID?", es_mayor_de_edad)



tiene_permiso_especial = False
puede_entrar_vip = puede_entrar or tiene_permiso_especial # 'or' es el "O" logico. Por lo que al menos una debe ser Verdadera. Equivale al simbolo "||" de Java y C
print("¿Puede entrar al área VIP?",puede_entrar_vip)



print(f"Lo contrario a True es:",not True) # invierte el valor. Equivale al simbolo "!" de Java y C