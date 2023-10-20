from .sistema import Sistema
from .empleados import Empleado

class Menu(Sistema):
    def __init__(self):
        self
    
    def menu_admin(self, cargo, sistema, txtemp, txtpass):
        if cargo == "administrador":
            while True:
                print("\nMENU ADMIN:")
                print("1. Registrar nuevo usuario")
                print("* Mostrar empleados")
                print("2. Cambiar contraseña de usuario")
                print("3. Eliminar usuario")
                print("4. Guardar en archivo CSV")
                print("5. Guardar y SALIR")
                print("6. Salir SIN GUARDAR")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    sistema.agregarEmpleado(Empleado)

                elif opcion == "*":
                    sistema.mostrarEmpleados()
                        
                elif opcion == "2":
                    sistema.cambiarPassword()
                
                #elif opcion == "3":
                 #       eliminar_usuario(empleados, usuarios)
                
                elif opcion == "4":
                    sistema.toFilePassword(txtpass)
                    sistema.toFileEmpleados(txtemp)


                elif opcion == "6":
                    
                    break
                '''else:
                    print("Opción no válida. Intente nuevamente.")'''