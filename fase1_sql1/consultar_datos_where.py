
import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect('proyecto.db')
cursor = conexion.cursor()

# Consultar datos filtrados: productos con precio > 100
cursor.execute('SELECT * FROM productos WHERE precio > 100')
resultados = cursor.fetchall()

# Mostrar los datos
print("Productos con precio mayor a 100:")
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()
