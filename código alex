# ROEH
import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('electrodomesticos.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear tabla de electrodomésticos si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS electrodomesticos
                  (id INTEGER PRIMARY KEY, nombre TEXT, categoria TEXT)''')

# Lista de electrodomésticos con sus categorías
electrodomesticos = {
    "Televisores": "Televisores",
    "Monitores": "Monitores",
    "Radios": "Radios",
    "Reproductores de música": "Reproductores de música",
    "Cámaras de foto y video": "Cámaras de foto y video",
    "Auriculares": "Auriculares",
    "Mandos a distancia": "Mandos a distancia",
    "Equipos de música y altavoces": "Equipos de música y altavoces",
    "Reproductor de video": "Reproductor de video",
    "Hornos": "Hornos",
    "Refrigeración": "Refrigeración",
    "Congeladores": "Congeladores",
    "Campanas extractoras": "Campanas extractoras",
    "Microondas": "Microondas",
    "Aires acondicionados": "Aires acondicionados",
    "Lavadoras": "Lavadoras",
    "Secadoras": "Secadoras",
    "Lavavajillas": "Lavavajillas",
    "Consola de videojuegos": "Consola de videojuegos",
    "Ordenadores portátiles y de mesa": "Ordenadores portátiles y de mesa",
    "Teléfonos inteligentes": "Teléfonos inteligentes",
    "Tabletas": "Tabletas",
    "Impresoras": "Impresoras",
    "Faxes": "Faxes",
    "Teclados": "Teclados",
    "Freidoras": "Freidoras",
    "Cafeteras": "Cafeteras",
    "Licuadora": "Licuadora"
}

# Insertar datos en la tabla
for nombre, categoria in electrodomesticos.items():
    cursor.execute("INSERT INTO electrodomesticos (nombre, categoria) VALUES (?, ?)", (nombre, categoria))

# Guardar los cambios
conn.commit()

# Consultar los datos de la tabla
cursor.execute("SELECT * FROM electrodomesticos")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()
