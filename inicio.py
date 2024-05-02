import sqlite3

# Función para calcular el promedio
def calcular_promedio():
    print("\nCalcular promedio\n")
    datos = []
    for i in range(6):
        while True:
            try:
                dato = float(input(f"Ingrese los datos del mes {i+1}: "))
                datos.append(dato)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

    promedio = sum(datos) / len(datos)
    print("El promedio de los gastos es:", promedio)

# Funciones para la gestión de electrodomésticos
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

def insertar_electrodomestico(conexion):
    nombre = input("Ingrese el nombre del electrodoméstico: ").strip()
    if not nombre:
        print("¡Error! El nombre del electrodoméstico no puede estar en blanco.")
        return
    
    if electrodomestico_existe(conexion, nombre):
        print("¡Error! Ya existe un electrodoméstico con ese nombre.")
        return
    
    gasto_energetico = input("Ingrese el grado de gasto energético (por ejemplo, A, B, C, D, E, F o G.): ").strip()
    if not gasto_energetico:
        print("¡Error! El grado de gasto energético no puede estar en blanco.")
        return
    
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO electrodomesticos (nombre, gasto_energetico) 
                    VALUES (?, ?)''', (nombre, gasto_energetico))
    conexion.commit()
    print("Electrodoméstico agregado correctamente.")

def electrodomestico_existe(conexion, nombre):
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM electrodomesticos WHERE nombre = ?''', (nombre,))
    electrodomestico = cursor.fetchone()
    return electrodomestico is not None

def eliminar_electrodomestico(conexion):
    id_eliminar = input("Ingrese el ID del electrodoméstico que desea eliminar: ")
    try:
        id_eliminar = int(id_eliminar)
    except ValueError:
        print("¡Error! El ID debe ser un número entero.")
        return

    cursor = conexion.cursor()
    cursor.execute('''DELETE FROM electrodomesticos WHERE id = ?''', (id_eliminar,))
    if cursor.rowcount == 0:
        print("¡Error! No se encontró ningún electrodoméstico con ese ID.")
    else:
        print("Electrodoméstico eliminado correctamente.")
    conexion.commit()

def mostrar_electrodomesticos(conexion):
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM electrodomesticos''')
    electrodomesticos = cursor.fetchall()
    print("Lista de electrodomésticos:")
    for electrodomestico in electrodomesticos:
        print(f"ID: {electrodomestico[0]}, Nombre: {electrodomestico[1]}, Gasto energético: {electrodomestico[2]}")

def menu_secundario(conexion):
    while True:
        print("\n1. Agregar electrodoméstico")
        print("2. Eliminar electrodoméstico")
        print("3. Mostrar lista de electrodomésticos")
        print("4. Salir")
                
        opcion = input("Seleccione una opción: ")
                
        if opcion == "1":
            insertar_electrodomestico(conexion)
        elif opcion == "2":
            eliminar_electrodomestico(conexion)
        elif opcion == "3":
            mostrar_electrodomesticos(conexion)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def menu_principal():
    crear_tabla()
    conexion = sqlite3.connect('electrodomesticos.db')
    while True:
        try:
            opcion = int(input("\nMenu\n------\n" +
                            "\t1. Calcular promedio\n" +
                            "\t2. Lista de electrodomésticos\n" +
                            "\t3. Cerrar\n\n" +
                            "Por favor ingrese una opción: "))

            if opcion == 1:
                calcular_promedio()
            elif opcion == 2:
                menu_secundario(conexion)
            elif opcion == 3:
                print("\nCerrando el programa\n")
                conexion.close()
                break
            else:
                print("\nOpción no válida. Por favor, ingrese una opción válida.\n")

        except ValueError:
            print("\nPor favor, ingrese un número válido como opción.\n")

    print("Programa finalizado.")

menu_principal()

# Llamada a la función para crear la tabla de electrodomésticos si no existe
crear_tabla()

# Llamada a la función del menú principal
menu_principal()
