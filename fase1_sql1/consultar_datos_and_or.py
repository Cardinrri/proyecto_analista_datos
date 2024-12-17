
import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect('proyecto.db')
cursor = conexion.cursor()

# Consultar datos con múltiples condiciones: precio > 100 AND stock <= 50
cursor.execute('SELECT * FROM productos WHERE precio > 100 AND stock <= 50')
resultados = cursor.fetchall()

# Mostrar los datos filtrados
print("Productos con precio mayor a 100 y stock menor o igual a 50:")
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()
