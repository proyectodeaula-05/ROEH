import sqlite3


def crear_tabla():
    conexion = sqlite3.connect('electrodomesticos.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS electrodomesticos (
                        id INTEGER PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        gasto_energetico TEXT NOT NULL
                    )''')
    conexion.commit()
    conexion.close()

def electrodomestico_existe(nombre):
    conexion = sqlite3.connect('electrodomesticos.db')
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM electrodomesticos WHERE nombre = ?''', (nombre,))
    electrodomestico = cursor.fetchone()
    conexion.close()
    return electrodomestico is not None


def insertar_electrodomestico():
    nombre = input("Ingrese el nombre del electrodoméstico: ")
    
    
    if electrodomestico_existe(nombre):
        print("¡Error! Ya existe un electrodoméstico con ese nombre.")
        return
    
    gasto_energetico = input("Ingrese el grado de gasto energético (por ejemplo, A, B, C, D, F o G): ")
    
    conexion = sqlite3.connect('electrodomesticos.db')
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO electrodomesticos (nombre, gasto_energetico) 
                    VALUES (?, ?)''', (nombre, gasto_energetico))
    conexion.commit()
    conexion.close()


def mostrar_electrodomesticos():
    conexion = sqlite3.connect('electrodomesticos.db')
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM electrodomesticos''')
    electrodomesticos = cursor.fetchall()
    print("Lista de electrodomésticos:")
    for electrodomestico in electrodomesticos:
        print(f"ID: {electrodomestico[0]}, Nombre: {electrodomestico[1]}, Gasto energético: {electrodomestico[2]}")
    conexion.close()


crear_tabla()
