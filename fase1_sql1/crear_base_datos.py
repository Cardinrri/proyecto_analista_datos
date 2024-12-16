
import sqlite3

# Paso 1: Crear la conexión a la base de datos (se crea el archivo si no existe)
conexion = sqlite3.connect('proyecto.db')

# Paso 2: Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Paso 3: Crear una tabla llamada 'productos'
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos 'proyecto.db' y tabla 'productos' creadas con éxito.")
