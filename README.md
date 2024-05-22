Función calcular_promedio ()
Esta función solicita al usuario que ingrese datos de gastos durante 6 meses, los almacena en una lista, y luego calcula y muestra el promedio de estos gastos.
1.	Inicialización:
 

Creamos la función llamada calcular_promedio ().
Imprimimos en la pantalla el título “calcular promedio”.
Se crea una lista vacía para almacenar los datos de gastos con el nombre “gastos”


2.	Bucle para ingresar datos:
 
En vez de crear varias variables para todos los 6 meses de datos se crea un bucle el cual imprima siempre un solo texto y se le vaya sumando un 1 cada vez hasta llegar a un rango de 6, asi ahorramos gastar recursos innecesarios en el sistema.

Diccionario: 
.append: es un método que tiene toda lista de Python el cual permite agregar un elemento al final de la lista

Try: El bloque try te permite probar un bloque de código en busca de errores.

While true: Con el bucle while podemos ejecutar un conjunto de instrucciones siempre que una condición sea verdadera.

For in: En Python, un bucle for se utiliza para iterar/repetir sobre secuencias como listas, cadenas, tuplas, etc.

3.	Cálculo y muestra del promedio:
 

Len: len devuelve el número de valores de un elemento iterable en Python.


Funciones de gestión de electrodomésticos
“crear_tabla_electrodomesticos()”

Crea una tabla llamada “electrodomesticos” en la base de datos si no existe.
 

Se define la función crear_tabla_electrodomesticos que crea una tabla llamada electrodomesticos si no existe. Se conecta a la base de datos electrodomesticos.db, crea un cursor y ejecuta un comando de SQL para crear la tabla con las columnas id, nombre y gasto_energetico.


Función insertar_electrodomestico(conexion)
 

Se define la función insertar_electrodomestico. Solicita al usuario que ingrese el nombre del electrodoméstico y lo almacena en la variable nombre. Si el nombre está vacío, muestra un mensaje de error y termina la función.



 
Solicita al usuario que ingrese el grado de gasto energético, lo convierte a mayúsculas y lo almacena en la variable gasto_energetico. Si el valor ingresado no está en la lista de valores permitidos, muestra un mensaje de error y termina la función.

 
Se crea un cursor y se ejecuta un comando de SQL para insertar un nuevo registro en la tabla electrodomesticos con los valores proporcionados por el usuario. Luego, confirma los cambios y muestra un mensaje de éxito.

Función eliminar_electrodomestico(conexion)

 

Se define la función eliminar_electrodomestico. Solicita al usuario que ingrese el ID del electrodoméstico que desea eliminar y lo convierte a un número entero. Si la conversión falla, muestra un mensaje de error y termina la función.

 
Crea un cursor y ejecuta un comando de SQL para eliminar el registro con el ID proporcionado. Si no se encuentra ningún registro con ese ID, muestra un mensaje de error. Si se elimina correctamente, muestra un mensaje de éxito.

Función mostrar_electrodomesticos(conexion)
 
Define la función mostrar_electrodomesticos. Crea un cursor y ejecuta un comando SQL para seleccionar todos los registros de la tabla electrodomesticos. Luego, recorre los resultados y muestra cada electrodoméstico.

Función crear_tabla_usuarios()
 
Define la función crear_tabla_usuarios que crea una tabla llamada usuarios si no existe. Se conecta a la base de datos usuarios.db, crea un cursor y ejecuta un comando SQL para crear la tabla con las columnas id, usuario y contraseña.

Función insertar_usuario()
 
Define la función insertar_usuario. Solicita al usuario que ingrese un nombre de usuario y una contraseña, y los almacena en las variables usuario y contraseña, respectivamente. Si alguno de los valores está vacío, muestra un mensaje de error y termina la función.
 
Crea un cursor y ejecuta un comando SQL para insertar un nuevo registro en la tabla usuarios con los valores proporcionados por el usuario. Luego, muestra un mensaje de éxito.
Función iniciar_sesion()
 
Define la función iniciar_sesion y muestra un mensaje indicando el inicio del proceso de inicio de sesión.

 
Inicia un bucle que solicita al usuario que ingrese un nombre de usuario y una contraseña. Se conecta a la base de datos usuarios.db, crea un cursor y ejecuta un comando SQL para buscar un registro que coincida con el nombre de usuario y la contraseña proporcionados.

 
Si se encuentra un registro que coincida, muestra un mensaje de éxito y retorna True. Si no se encuentra, muestra un mensaje de error y retorna False.

Función menu_secundario(conexion)
 
Define la función menu_secundario. Inicia un bucle que presenta opciones para gestionar electrodomésticos: agregar, eliminar, mostrar lista o salir.

 
Solicita al usuario que seleccione una opción del menú. (creo que es obvio, pero aja)



 
Dependiendo de la opción seleccionada, llama a la función correspondiente para agregar, eliminar o mostrar electrodomésticos. Si la opción es "4", rompe el bucle y sale del menú secundario. Si la opción no es válida, muestra un mensaje de error.

Función menu_principal()
 
Define la función menu_principal. Crea las tablas de usuarios y electrodomesticos si no existen.

 
Inicia un bucle que presenta las opciones principales del programa: iniciar sesión, crear usuario o salir.

 
Solicita al usuario que seleccione una opción del menú principal.

 
Si el usuario selecciona "1" (iniciar sesión) y la autenticación es exitosa, se conecta a la base de datos electrodomesticos.db y presenta un menú secundario con opciones para calcular el promedio, listar electrodomésticos o cerrar sesión.

 
Dependiendo de la opción seleccionada en el menú secundario, llama a la función correspondiente para calcular el promedio, mostrar el menú de electrodomésticos o cerrar sesión. Si la opción no es válida, muestra un mensaje de error.

 
Si el usuario ingresa una opción no numérica, captura la excepción ValueError y muestra un mensaje de error.

 
Si el usuario selecciona "2" (crear usuario), llama a la función insertar_usuario. Si selecciona "3" (salir), muestra un mensaje de salida y rompe el bucle principal. Si la opción no es válida, muestra un mensaje de error.

 
Muestra un mensaje de despedida cuando el programa termina.

 
Llama a la función menu_principal para iniciar el programa.
