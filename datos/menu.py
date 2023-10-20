from .sistema import Sistema
from .empleados import Empleado

class Menu(Sistema):
    def __init__(self):
        self
    
    def menu_admin(self, cargo, sistema):
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
                    #imprime todos los empleados
                    current = sistema.empleados.head
                    while current is not None:
                        print(current.get_data())  # Aquí asumimos que get_data() devuelve el valor almacenado en el nodo
                        current = current.get_next()
                        
                #elif opcion == "2":
                #       cambiar_contraseña(usuarios)
                #elif opcion == "3":
                 #       eliminar_usuario(empleados, usuarios)
                
                elif opcion == "6":
                    
                    break
                '''else:
                    print("Opción no válida. Intente nuevamente.")'''