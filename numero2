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
def crear_tabla_electrodomesticos():
    with sqlite3.connect('electrodomesticos.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS electrodomesticos (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            gasto_energetico TEXT NOT NULL
                        )''')

def insertar_electrodomestico(conexion):
    nombre = input("Ingrese el nombre del electrodoméstico: ").strip()
    gasto_energetico = input("Ingrese el grado de gasto energético (por ejemplo, A, B, C, D, E, F o G.): ").strip()

    if not nombre or not gasto_energetico:
        print("¡Error! El nombre del electrodoméstico y el grado de gasto energético no pueden estar en blanco.")
        return

    with conexion:
        cursor = conexion.cursor()
        cursor.execute('''INSERT INTO electrodomesticos (nombre, gasto_energetico) 
                        VALUES (?, ?)''', (nombre, gasto_energetico))
    print("Electrodoméstico agregado correctamente.")

def eliminar_electrodomestico(conexion):
    id_eliminar = input("Ingrese el ID del electrodoméstico que desea eliminar: ")
    try:
        id_eliminar = int(id_eliminar)
    except ValueError:
        print("¡Error! El ID debe ser un número entero.")
        return

    with conexion:
        cursor = conexion.cursor()
        cursor.execute('''DELETE FROM electrodomesticos WHERE id = ?''', (id_eliminar,))
        if cursor.rowcount == 0:
            print("¡Error! No se encontró ningún electrodoméstico con ese ID.")
        else:
            print("Electrodoméstico eliminado correctamente.")

def mostrar_electrodomesticos(conexion):
    with conexion:
        cursor = conexion.cursor()
        cursor.execute('''SELECT * FROM electrodomesticos''')
        electrodomesticos = cursor.fetchall()
        print("Lista de electrodomésticos:")
        for electrodomestico in electrodomesticos:
            print(f"ID: {electrodomestico[0]}, Nombre: {electrodomestico[1]}, Gasto energético: {electrodomestico[2]}")

# Funciones para la gestión de usuarios
def crear_tabla_usuarios():
    with sqlite3.connect('usuarios.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY,
                            usuario TEXT NOT NULL,
                            contrasena TEXT NOT NULL
                        )''')

def insertar_usuario():
    usuario = input("Ingrese el nombre de usuario: ").strip()
    contrasena = input("Ingrese la contraseña: ").strip()

    if not usuario or not contrasena:
        print("¡Error! El nombre de usuario y la contraseña no pueden estar en blanco.")
        return

    with sqlite3.connect('usuarios.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''INSERT INTO usuarios (usuario, contrasena) 
                        VALUES (?, ?)''', (usuario, contrasena))
    print("Usuario creado correctamente.")

def iniciar_sesion():
    print("\nInicio de sesión\n")
    while True:
        usuario = input("Usuario: ")
        contrasena = input("Contraseña: ")
        
        with sqlite3.connect('usuarios.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('''SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?''', (usuario, contrasena))
            resultado = cursor.fetchone()

        if resultado:
            print("\nInicio de sesión exitoso.\n")
            return True
        else:
            print("\nUsuario o contraseña incorrectos. Inténtelo de nuevo.\n")
            return False

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
    crear_tabla_usuarios()
    crear_tabla_electrodomesticos()
    while True:
        print("\n1. Iniciar sesión")
        print("2. Crear usuario")
        print("3. Salir")
                
        opcion = input("Seleccione una opción: ")
                
        if opcion == "1":
            if iniciar_sesion():
                with sqlite3.connect('electrodomesticos.db') as conexion:
                    while True:
                        try:
                            opcion = int(input("\nMenu\n------\n" +
                                            "\t1. Calcular promedio\n" +
                                            "\t2. Lista de electrodomésticos\n" +
                                            "\t3. Cerrar sesión\n\n" +
                                            "Por favor ingrese una opción: "))

                            if opcion == 1:
                                calcular_promedio()
                            elif opcion == 2:
                                menu_secundario(conexion)
                            elif opcion == 3:
                                print("\nCerrando sesión\n")
                                break
                            else:
                                print("\nOpción no válida. Por favor, ingrese una opción válida.\n")

                        except ValueError:
                            print("\nPor favor, ingrese un número válido como opción.\n")

        elif opcion == "2":
            insertar_usuario()
        elif opcion == "3":
            print("\nSaliendo del programa\n")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

    print("Programa finalizado.")

menu_principal()
