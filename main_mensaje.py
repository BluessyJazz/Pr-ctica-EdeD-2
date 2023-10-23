import csv
from datos.direccion import Direccion
from datos.fecha import Fecha
from datos.empleado import Empleado
from datos.sistema_empleados import Sistema_Empleados
from datos.menu import Menu
from datos.sistema_mensajes import Sistema_Mensajes

txtempleados = "txt/Empleados.txt"
txtpassword = "txt/Password.txt"

sistema = Sistema_Empleados()
empleados = sistema.empleados

sistema.cargarEmpleados(txtempleados)
sistema.cargarPassword(txtpassword)

while True:
    # Pedir al usuario que ingrese su cedula y contraseña
    id_usuario = int(input("\nIngrese su número de identificación (cedula): "))
    
    if id_usuario == 0000:
        print("\nGOOD BYE!\n")
        break

    contraseña_ingresada = str(input("Ingrese su contraseña: "))

    # Verificar el acceso y obtener el rol del usuario
    rol_usuario = sistema.verificarAcceso(id_usuario, contraseña_ingresada)

    if rol_usuario == "administrador":
        print(f"\nBienvenido, usted es un {rol_usuario}.")

        #Opción de menú de admin y menú de mensajes
        
        menu = Menu()

        menu.menu_admin(rol_usuario, sistema, txtempleados, txtpassword)

    elif rol_usuario == "empleado":
        print(f"\nBienvenido, usted es un {rol_usuario}.")

        sistema_mensajes = Sistema_Mensajes()

        archivo_mensaje = f"txt/{id_usuario}_BA.txt"

        print(sistema_mensajes.cargarMensajes(archivo_mensaje, id_usuario))

    else:
        print("\nAcceso denegado. Verifique sus datos e intente nuevamente.")