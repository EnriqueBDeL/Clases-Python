
print("--- CONTROL DESPEGUE (WHILE) ---")

contador = 5

while contador > 0:
    print(f"Despegue en... {contador}")
    contador -= 1 

    # En Python NO existe el "contador--" o "contador++."
    # Usamos "contador -= 1" o "contador += 1"

print("¡Despegue!\n")






print("--- RECORRER UNA LISTA (FOR) ---")

lenguajes = ["Python", "Java", "C++", "JavaScript"]


for lenguaje in lenguajes: # Se ejecuta el interior tantas veces el numero que ocupa el Array.
    print(f"Me gusta programar en {lenguaje}")




print("\n--- REPETIR N VECES CON RANGE ---")

for i in range(5): # Genera números del 0 al 4 (siempre es uno menos que el límite) En este caso siempre saldrá 5
    print(f"Esta es la repetición número {i}")


print("\n--- RANGOS PERSONALIZADOS ---")
# range(inicio, fin, salto)
for numero_par in range(2, 11, 2): # Empieza en 2, termina antes del 11, salta de 2 en 2
    print(f"Número par: {numero_par}")





print("\n--- USO DE BREAK Y CONTINUE ---")
for num in range(1, 7):
    if num == 3:
        print("Saltamos el número 3")
        continue # continue: Salta el resto del código en esta iteración y pasa a la siguiente.
        print("Esto no se ejecuta si saltamos")
    if num == 5:
        print("Llegamos al 5, cortamos el ciclo")
        break # break: Rompe y termina el ciclo completo.
        print("No se procesará ni este mensaje ni el 6")
    print(f"Procesando el número {num}")


