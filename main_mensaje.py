import csv
from datos.direccion import Direccion
from datos.fecha import Fecha
from datos.empleados import Empleado
from datos.sistema import Sistema
from datos.menu import Menu

txtempleados = "txt/Empleados.txt"
txtpassword = "txt/Password.txt"

sistema = Sistema()
empleados = sistema.empleados

sistema.cargarEmpleados(txtempleados)
sistema.cargarPassword(txtpassword)

while True:
    # Pedir al usuario que ingrese su cedula y contraseña
    cedula_ingresada = int(input("Ingrese su número de identificación (cedula): "))
    
    if cedula_ingresada == 0000:
        break

    contraseña_ingresada = str(input("Ingrese su contraseña: "))

    # Verificar el acceso y obtener el rol del usuario
    rol_usuario = sistema.verificarAcceso(cedula_ingresada, contraseña_ingresada)

    if rol_usuario is not None:
        print(f"Bienvenido, usted es un {rol_usuario}.")
        menu = Menu()

        menu.menu_admin(rol_usuario, sistema, txtempleados, txtpassword) 

    else:
        print("Acceso denegado. Verifique sus datos e ingrese nuevamente.")






