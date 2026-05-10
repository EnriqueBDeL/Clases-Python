# Programación Orientada a Objetos



class Coche: # Declaracion de una clase
    
    # El método __init__ es el CONSTRUCTOR. 
    # 'self' SIEMPRE debe ser el primer parámetro en los métodos de una clase.
    # 'self' hace referencia al objeto mismo (es exactamente igual al 'this' de Java).
    def __init__(self, marca, modelo, color):
        # Aquí definimos los atributos del objeto
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False # Podemos dar valores por defecto



    def arrancar(self): # Definicion metodo. Recuerda pasar siempre 'self' para que el método pueda acceder a los atributos.
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado. ¡Brum, brum!")
        else:
            print("El coche ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"El {self.marca} ha sido apagado.")
        else:
            print("El coche ya está apagado.")
            
    def pintar(self, nuevo_color):
        self.color = nuevo_color
        print(f"Ahora el coche es de color {self.color}.")



# En Python NO usamos la palabra 'new'. Simplemente llamamos a la clase
# como si fuera una función y le pasamos los parámetros del __init__.

print("--- CREANDO OBJETOS ---")

# Instanciamos dos coches diferentes
mi_coche = Coche("Toyota", "Corolla", "Rojo")
coche_amigo = Coche("Ford", "Mustang", "Negro")


print(f"Mi coche es un {mi_coche.marca} de color {mi_coche.color}.")



print("\n--- USANDO LOS MÉTODOS ---")
mi_coche.arrancar()
mi_coche.arrancar() # Intentamos arrancar de nuevo para probar la lógica
mi_coche.pintar("Azul")
mi_coche.apagar()



print("\n--- ESTADO INDEPENDIENTE ---")
coche_amigo.arrancar() # Demostramos que son objetos totalmente independientes
print(f"¿El coche de mi amigo está encendido? {coche_amigo.encendido}")
print(f"¿Mi coche está encendido? {mi_coche.encendido}")
