import sqlite3

# Función para calcular el promedio
def calcular_promedio():
    print("\nCalcular promedio\n")
    numeros = []
    while True:
        num = input("Ingrese un número (o 'fin' para terminar): ")
        if num.lower() == 'fin':
            break
        try:
            numero = float(num)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")

    if numeros:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números ingresados es: {promedio}")
    else:
        print("No se ingresaron números para calcular el promedio.")

# Función para crear la tabla de electrodomésticos si no existe
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

# Función para verificar si un electrodoméstico ya existe
def electrodomestico_existe(nombre):
    conexion = sqlite3.connect('electrodomesticos.db')
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM electrodomesticos WHERE nombre = ?''', (nombre,))
    electrodomestico = cursor.fetchone()
    conexion.close()
    return electrodomestico is not None

# Función para insertar un electrodoméstico
def insertar_electrodomestico():
    nombre = input("Ingrese el nombre del electrodoméstico: ").strip()
    
    # Validar que el nombre no esté en blanco
    if not nombre:
        print("¡Error! El nombre del electrodoméstico no puede estar en blanco.")
        return
    
    # Verificar si el electrodoméstico ya existe
    if electrodomestico_existe(nombre):
        print("¡Error! Ya existe un electrodoméstico con ese nombre.")
        return
    
    gasto_energetico = input("Ingrese el grado de gasto energético (por ejemplo, A, B, C, D, E, F o G.): ").strip()
    
    # Validar que el grado de gasto energético no esté en blanco
    if not gasto_energetico:
        print("¡Error! El grado de gasto energético no puede estar en blanco.")
        return
    
    conexion = sqlite3.connect('electrodomesticos.db')
    cursor = conexion.cursor()
    cursor.execute('''INSERT INTO electrodomesticos (nombre, gasto_energetico) 
                    VALUES (?, ?)''', (nombre, gasto_energetico))
    conexion.commit()
    conexion.close()

# Función para eliminar un electrodoméstico
def eliminar_electrodomestico():
    id_eliminar = input("Ingrese el ID del electrodoméstico que desea eliminar: ")
    try:
        id_eliminar = int(id_eliminar)
    except ValueError:
        print("¡Error! El ID debe ser un número entero.")
        return

    conexion = sqlite3.connect('electrodomesticos.db')
    cursor = conexion.cursor()
    cursor.execute('''DELETE FROM electrodomesticos WHERE id = ?''', (id_eliminar,))
    if cursor.rowcount == 0:
        print("¡Error! No se encontró ningún electrodoméstico con ese ID.")
    else:
        print("Electrodoméstico eliminado correctamente.")
    conexion.commit()
    conexion.close()

# Función para mostrar todos los electrodomésticos
def mostrar_electrodomesticos():
    conexion = sqlite3.connect('electrodomesticos.db')
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM electrodomesticos''')
    electrodomesticos = cursor.fetchall()
    print("Lista de electrodomésticos:")
    for electrodomestico in electrodomesticos:
        print(f"ID: {electrodomestico[0]}, Nombre: {electrodomestico[1]}, Gasto energético: {electrodomestico[2]}")
    conexion.close()

# Función para el menú secundario
def menu_secundario():
    while True:
        print("\n1. Agregar electrodoméstico")
        print("2. Eliminar electrodoméstico")
        print("3. Mostrar lista de electrodomésticos")
        print("4. Salir")
                
        opcion = input("Seleccione una opción: ")
                
        if opcion == "1":
            insertar_electrodomestico()
        elif opcion == "2":
            eliminar_electrodomestico()
        elif opcion == "3":
            mostrar_electrodomesticos()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Función para el menú principal
def menu_principal():
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
                menu_secundario()
            elif opcion == 3:
                print("\nCerrando el programa\n")
                break
            else:
                print("\nOpción no válida. Por favor, ingrese una opción válida.\n")

        except ValueError:
            print("\nPor favor, ingrese un número válido como opción.\n")

    print("Programa finalizado.")

# Llamada a la función para crear la tabla de electrodomésticos si no existe
crear_tabla()

# Llamada a la función del menú principal
menu_principal()
