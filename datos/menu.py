from .sistema_empleados import Sistema_Empleados

class Menu(Sistema_Empleados):
    def __init__(self):
        self
    
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
