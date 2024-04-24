import sqlite3

def crear_tabla_usuarios():
    # Conexión a la base de datos (si no existe, se crea)
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    
    # Crear la tabla del usuario si no existe
    cursor.execute('''CREA TABLA SI NO EXISTEN usuarios (
                        id INTEGRE LLAVE PRIMARIA,
                        nombre TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        contraseña TEXT NOT NULL
                     )''')
    
    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")

    # Conexión a la base de datos
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    
    try:
        # Insertar nuevo usuario en la base de datos
        cursor.execute("INSERT INTO usuarios (nombre, email, contraseña) VALUES (?, ?, ?)",
                       (nombre, email, contraseña))
        print("Usuario registrado con éxito.")
    except sqlite3.IntegrityError:
        print("El email ingresado ya está registrado.")
    
    # Guardar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

# Crear la tabla de usuarios (si no existe)
crear_tabla_usuarios()

# Registrar un nuevo usuario
registrar_usuario()
