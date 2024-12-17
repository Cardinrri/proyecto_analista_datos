
import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect('proyecto.db')
cursor = conexion.cursor()

# Consultar y ordenar datos: productos ordenados por precio ascendente
cursor.execute('SELECT * FROM productos ORDER BY precio ASC')
resultados = cursor.fetchall()

# Mostrar los datos ordenados
print("Productos ordenados por precio (ascendente):")
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()
