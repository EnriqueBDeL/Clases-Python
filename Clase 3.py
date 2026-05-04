# Sentencia IF, ELIF, ELSE

print("--- SISTEMA DE ACCESO ---")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
#...
    print("Acceso concedido. Eres mayor de edad.") # Fíjate en los espacios antes del 'print'. Esto indica que está DENTRO del if.
    print("¡Disfruta la fiesta!")



print("\n--- CLASIFICACIÓN POR EDADES ---")   # Si quitas los espacios, el código ya no está dentro del if.

# Para revisar múltiples condiciones encadenadas, Python acorta "else if" a "elif".


if edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.") # El else captura cualquier caso que no haya entrado en los de arriba.



# Condicion en una sola linea


estado_civil = "Casado"

#  [Valor Verdadero]    if         [Condición]      else    [Valor Falso]
mensaje = "Felicidades" if estado_civil == "Casado" else "Sigue buscando"

print(f"\nMensaje automático: {mensaje}")



# Condicion con operadores lógicos

tiene_entrada = True
es_vip = False

print("\n--- CONTROL DE PUERTA ---")
if tiene_entrada and not es_vip:
    print("Pase a la zona general.")
elif tiene_entrada and es_vip:
    print("Pase a la sala VIP, le daremos una bebida de cortesía.")
else:
    print("No puede entrar sin boleto.")
