# ===============================================================================================
# USO DE LIBRERÍAS EXTERNAS Y PIP
# ===============================================================================================


"""
¿Qué son las Librerías Externas?
Son paquetes de código creados por la comunidad de programadores de Python en 
todo el mundo. No vienen instaladas por defecto para que Python no ocupe demasiado 
espacio en tu disco duro. Solo descargas las que necesitas.

¿Qué es PyPI y PIP?
- PyPI (Python Package Index): Es la "tienda" o almacén en internet donde se guardan 
  todas estas librerías.
- PIP (Pip Installs Packages): Es un comando que usas en tu 
  computadora para ir a PyPI, descargar la librería y prepararla para que la uses.
"""

# ===============================================================================================
# 1. ¿CÓMO SE INSTALAN? (PASO PREVIO OBLIGATORIO)
# ===============================================================================================

# ¡ATENCIÓN! El código de instalación NO se escribe aquí en Python.
# Se escribe en la TERMINAL de tu sistema (CMD o PowerShell en Windows, Terminal en Mac/Linux).
#
# Para probar el código de más abajo, primero abre tu terminal y escribe:
#
#   pip install requests
#   pip install pandas
#
# Una vez que la terminal termine de descargar todo, ya puedes ejecutar este archivo Python.


# En mi caso como creador del tutorial, como uso Google Colab, puedo  hacerlo directamente desde la ventana de código.

# Para ejecutar comandos de la terminal (como pip) dentro de una celda de código de Google Colab, solo necesitas anteponer un signo de exclamación (!) al comando.

#
#   !pip install requests
#   !pip install pandas
#


!pip install requests

!pip install pandas


# ===============================================================================================
# 2. EJEMPLOS DE LIBRERÍAS EXTERNAS (Y SUS USOS FORMALES)
# ===============================================================================================

# -----------------------------------------------------------------------------------------------
# LIBRERÍA REQUESTS
# Propósito: Es el estándar de la industria para realizar peticiones HTTP. Sirve para que tu
# programa de Python se conecte a internet, descargue información de páginas web o se 
# comunique con servidores.
# -----------------------------------------------------------------------------------------------

import requests

print("Petición a Github:")
try:
    respuesta = requests.get("https://api.github.com")    # Hacemos una petición para conectarnos a una página web (la API pública de GitHub)

    
    print("Estado de la conexión a internet:", respuesta.status_code)  # Si la conexión es exitosa, el servidor responde con el código 200.

except ImportError:
    print("¡Error! Te olvidaste de instalar la librería. Ve a la terminal y escribe: pip install requests")


# -----------------------------------------------------------------------------------------------
# LIBRERÍA PANDAS
# Propósito: Es la herramienta fundamental para el análisis y manipulación de datos en Python.
# Permite organizar información en tablas (llamadas DataFrames), buscar datos específicos
# y hacer cálculos, de forma muy similar a como funciona Microsoft Excel pero con código.
# -----------------------------------------------------------------------------------------------

import pandas as pd # Es una convención mundial importar pandas siempre con el alias 'pd'

print("\nPANDAS:")

try:
    datos_alumnos = { "Nombre": ["Ana", "Luis", "Carlos"], "Edad": [22, 25, 20], "Nota Final": [8.5, 9.0, 7.5] }

    tabla = pd.DataFrame(datos_alumnos) # Le pedimos a Pandas que convierta esos datos en una tabla profesional (DataFrame)

    print("Tabla de datos generada:")
    print(tabla)

except ImportError:
  
    print("¡Error! Te olvidaste de instalar la librería. Ve a la terminal y escribe: pip install pandas")
