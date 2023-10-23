from .sistema_empleados import Sistema_Empleados
from .empleado import Empleado

class Menu(Sistema_Empleados):
    def __init__(self):
        self
    
def menu_admin(sistema, txtemp, txtpass):
    while True:
        print("\nMENU ADMIN:")
        print("1. Registrar nuevo usuario")
        print("2. Eliminar usuario")
        print("3. Cambiar contraseña de usuario")
        print("4. Ver usuarios")
        print("5. Guardar")
        print("6. Guardar y cerrar sesión")
        print("7. Cerrar sesión SIN GUARDAR")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            sistema.agregarEmpleado(Empleado)

        elif opcion == "2":
            id = int(input("Escriba el número de ID del empleado que desea eliminar: "))
            print(sistema.eliminarEmpleado(id))
                
        elif opcion == "3":
            sistema.cambiarPassword()
        
        elif opcion == "4":
            sistema.mostrarEmpleados()
        
        elif opcion == "5":
            sistema.toFilePassword(txtpass)
            sistema.toFileEmpleados(txtemp)
            print("\nGuardado con éxito")

        elif opcion == "6":
            sistema.toFilePassword(txtpass)
            sistema.toFileEmpleados(txtemp)
            print("\nGuardado con éxito")
            print("\nCerrando sesión...")
            break

        elif opcion == "7":
            print("\nCerrando sesión...")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")

def menu_empleado():
    while True:
        print("\nMENU EMPLEADO:")
        print("1. Escribir un mensaje")
        print("2. Bandeja de entrada")
        print("3. Mensajes leídos")
        print("4. Proyectar mensajes en borradores")

        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            None
