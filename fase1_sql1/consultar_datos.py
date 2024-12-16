
import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect('proyecto.db')
cursor = conexion.cursor()

# Consultar todos los datos de la tabla 'productos'
cursor.execute('SELECT * FROM productos')
resultados = cursor.fetchall()

# Mostrar los datos
print("Datos en la tabla 'productos':")
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()

