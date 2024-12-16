
import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect('proyecto.db')
cursor = conexion.cursor()

# Insertar datos en la tabla 'productos'
productos = [
    (1, 'Laptop', 1200.50, 10),
    (2, 'Mouse', 25.75, 100),
    (3, 'Teclado', 45.90, 50),
    (4, 'Monitor', 300.00, 20),
    (5, 'Auriculares', 60.00, 30)
]

try:
    # Ejecutar las inserciones
    cursor.executemany('INSERT INTO productos (id, nombre, precio, stock) VALUES (?, ?, ?, ?)', productos)
    conexion.commit()
    print("Datos insertados correctamente en la tabla 'productos'.")
except sqlite3.IntegrityError as e:
    print(f"Error: {e}")

# Cerrar la conexión
conexion.close()
