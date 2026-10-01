'''

Matplotlib es la librería de visualización más usada en Python.
Permite crear gráficos de todo tipo: líneas, barras, dispersión, histogramas, mapas decalor, etc

'''

# pip install matplotlib

import matplotlib.pyplot as plt # En Matplotlib, casi siempre usamos un submódulo llamado pyplot. El estándar mundial es importarlo con el alias plt
import numpy as np # Lo usaremos para generar datos de ejemplo


# Matplotlib divide un gráfico en dos partes:
#
# - La Figura (Figure): Es el lienzo en blanco, el marco de la ventana.
#
# - Los Ejes (Axes): Es el gráfico en sí mismo (la cuadrícula, las líneas, los puntos).



# Grafico de Líneas

# 1. Datos
meses = ["Ene", "Feb", "Mar", "Abr"]
ventas = [150, 200, 180, 250]

plt.plot(meses, ventas) # 2. Crear el gráfico de línea

plt.show() # 3. Mostrar el gráfico en pantalla (siempre va al final)



# Personalizar grafico

x = np.array([1, 2, 3, 4, 5])
y = x ** 2 # El cuadrado de x: [1, 4, 9, 16, 25]

# Dibujar la línea. 
# color: color de línea | marker: estilo del punto ('o' es círculo) | label: nombre para la leyenda
plt.plot(x, y, color="red", marker="o", linestyle="--", label="Crecimiento")

# Etiquetas
plt.title("Mi Primer Gráfico Pro")
plt.xlabel("Eje X (Tiempo)")
plt.ylabel("Eje Y (Cantidad)")

# Activar la leyenda y la cuadrícula
plt.legend() 
plt.grid(True)

# Guardar el gráfico como imagen
# plt.savefig("mi_grafico.png", dpi=300) 

plt.show()






# Grafico de Barras

categorias = ["Manzanas", "Naranjas", "Peras"]
cantidades = [100, 50, 80]

plt.bar(categorias, cantidades, color=["red", "orange", "green"])
plt.title("Stock de Frutas")
plt.show()


# Grafico de Dispersión

edad = [25, 30, 35, 40, 45]
salario = [30000, 40000, 45000, 60000, 55000]


plt.scatter(edad, salario, color="blue")
plt.title("Edad vs Salario")
plt.show()


# Grafico de Histograma

edades_clientes = np.random.randint(18, 65, size=200) # 200 edades aleatorias

plt.hist(edades_clientes, bins=10, edgecolor="black") # bins = número de "cajas"
plt.title("Distribución de Edades")
plt.show()





# Grafico de Calor


# Imaginemos que es la cantidad de clientes en una tienda (Matriz de 5 días x 3 turnos)
clientes = np.array([
    [10, 50, 30],  # Lunes
    [20, 60, 40],  # Martes
    [30, 80, 50],  # Miércoles
    [40, 90, 70],  # Jueves
    [80, 120, 90]  # Viernes
])

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
turnos = ["Mañana", "Tarde", "Noche"]


fig, ax = plt.subplots() # Crear la figura y el gráfico


mapa = ax.imshow(clientes, cmap="YlOrRd") # imshow mapea los números a colores. cmap es la paleta de colores ("hot", "viridis", "Blues"...)


fig.colorbar(mapa, label="Número de clientes") # Añadir la barra de color lateral (leyenda térmica)

# Configurar las etiquetas de los ejes
ax.set_xticks(np.arange(len(turnos)), labels=turnos)
ax.set_yticks(np.arange(len(dias)), labels=dias)

# (Opcional) Escribir el número exacto dentro de cada cuadrito
for i in range(len(dias)):
    for j in range(len(turnos)):
        ax.text(j, i, clientes[i, j], ha="center", va="center", color="black")

plt.title("Afluencia de clientes por día y turno")
plt.show()
