frutas = ["Manzana", "Banana", "Cereza", "Naranja"] # Declaraión de un Array


lista_loca = [1, "Texto", True, 3.14] # En Python, una lista puede contener diferentes tipos de datos mezclados.

print("Mi lista de frutas:", frutas)
print("Mi lista loca:", lista_loca)




# Al igual que en casi todos los lenguajes, empezamos a contar dentro del Array desde el 0.

print("\nLa primera fruta es:", frutas[0])  
print("La tercera fruta es:", frutas[2])    



# Python puede trabajar con indices negativos.

print("\nLa última fruta es:", frutas[-1]) # Si usas -1, accedes al ÚLTIMO elemento de la lista sin importar su tamaño.



# Como las listas son dinámicas, crecen o se encogen según necesitemos.
print("\nLista antes de modificar:", frutas)

frutas[1] = "Pera" # Modifica elemento existente

print("Lista después de modificar:", frutas)



frutas.append("Uva") # Agrega un elemento al final de la lista
print("Lista con nueva fruta:", frutas)



frutas.insert(0, "Mango") # Agrega un elemento en una posición específica (índice, valor) [no modifica]
print("Lista tras insertar Mango al inicio:", frutas)



frutas.remove("Cereza") # Elimina un elemento por su valor
print("Lista tras eliminar la Cereza:", frutas)



print(f"\nActualmente tengo {len(frutas)} frutas en mi lista.") # Nos dice el tamaño o longitud de la lista
