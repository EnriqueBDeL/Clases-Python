# Herencia en POO



class Empleado: # Clase Padre (Superclase)
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        print(f"{self.nombre} está realizando sus tareas generales.")

    def mostrar_info(self):
        print(f"Empleado: {self.nombre} | Salario: ${self.salario}")



class Desarrollador(Empleado): # Clase Hija. Para heredar, ponemos la clase padre entre paréntesis.
    
    def __init__(self, nombre, salario, lenguaje_favorito):
        # Usamos super() para llamar al constructor de la clase Padre
        # En Python 3 no hace falta pasar 'self' dentro de super()
        super().__init__(nombre, salario)
        # Añadimos el atributo exclusivo de la clase hija
        self.lenguaje_favorito = lenguaje_favorito

    def trabajar(self):
            print(f"{self.nombre} está escribiendo código en {self.lenguaje_favorito}.")

    def mostrar_info(self):
        super().mostrar_info()         # Podemos llamar al método del padre y luego añadir más cosas
        print(f"Especialidad: Programador {self.lenguaje_favorito}")



class Gerente(Empleado):
    
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está en una reunión de planificación del departamento de {self.departamento}.")


print("--- CREANDO LOS OBJETOS ---")
empleado_comun = Empleado("Ana", 3000)
dev = Desarrollador("Enrique", 4500, "Python")
jefe = Gerente("Carlos", 6000, "Ventas")



print("\n--- APLICANDO POLIMORFISMO ---")
empleado_comun.trabajar()
dev.trabajar()
jefe.trabajar()

print("\n--- INFORMACIÓN COMPLETA (Sobrescritura + super) ---")
dev.mostrar_info()
