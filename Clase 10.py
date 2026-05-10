# Excepciones


print("--- DIVISIÓN SEGURA (Con error)---")

try: # Intentamos ejecutar un código que podría fallar
    resultado = 10 / 0
    print(resultado)
except ZeroDivisionError: # Capturamos el error específico (División por cero)
    print("¡Error! No puedes dividir un número entre cero.")



print("\n--- DIVISIÓN SEGURA (Sin error) ---")

try: # Intentamos ejecutar un código que podría fallar
    resultado = 4 / 2
    print(resultado)
except ZeroDivisionError: # Capturamos el error específico (División por cero)
    print("¡Error! No puedes dividir un número entre cero.")





print("\n--- VALIDACIÓN DE ENTRADA ---")

try:
    numero_str = input("Ingresa un número entero para calcular su doble: ")
    numero = int(numero_str) # Esto fallará si el usuario escribe letras
    doble = numero * 2
    
except ValueError:     # Este bloque se ejecuta si el usuario ingresó texto en lugar de un número
    print("¡Error! Debes ingresar un número entero válido, no letras.")
    
except Exception as e:     # Exception captura CUALQUIER otro error no previsto (como Exception en Java).
                           # Guardamos el error en la variable 'e' para poder imprimirlo.
    print(f"Ocurrió un error inesperado: {e}")
    
else:
    # ¡Exclusivo de Python!
    # El bloque 'else' SOLO se ejecuta si el 'try' tuvo éxito (si no hubo errores).
    print(f"¡Cálculo exitoso! El doble de {numero} es {doble}.")
    
finally:
    # Al igual que en Java, 'finally' SIEMPRE se ejecuta, haya fallado o no.
    # Se suele usar para cerrar archivos o conexiones a bases de datos.
    print("-> Fin de la operación (Este mensaje siempre se muestra).")


print("\nEl programa continúa funcionando normalmente sin cerrarse de golpe.")
