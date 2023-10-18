from listas.list import List  # Importa la clase List para usarla en el sistema de mensajería
from listas.double_list import DoubleList  # Importa la clase DoubleList para usarla en el sistema de mensajería
from dequeues.stack import Stack  # Importa la clase Stack para usarla en el sistema de mensajería
from dequeues.queue import Queue  # Importa la clase Queue para usarla en el sistema de mensajería
from empleados import Empleado
from admin import Administrador
from datos.registro import Registro

class Mensajeria:
    def __init__(self):
        self.employee_list = List()  # Lista de empleados
        self.message_queue = Queue()  # Cola de mensajes leídos
        self.draft_stack = Stack()  # Pila de borradores

    def cargar_password(self, archivo_password):
        with open(archivo_password, 'r') as file:
            for line in file:
                data = line.split()
                id = data[0]
                password = data[1]
                role = data[2]
                # Crear objetos de tipo Empleado o Administrador en función del role
                if role == 'empleado':
                    empleado = Empleado(id, password)
                    self.employee_list.append(empleado)
                elif role == 'administrador':
                    administrador = Administrador(id, password)
                    self.employee_list.append(administrador)

    def verificar_credenciales(self, id, password):
        for empleado in self.employee_list:
            if empleado.id == id and empleado.password == password:
                return empleado
        return None
    
    def agregar_empleado(self, usuario, es_administrador=False):
        if es_administrador:
            return self.registro.agregar(usuario)
        else:
            print("No tienes los permisos necesarios para realizar esta acción.")

    def eliminar_empleado(self, id, es_administrador=False):
        if es_administrador:
            return self.registro.eliminar(id)
        else:
            print("No tienes los permisos necesarios para realizar esta acción.")

    def cambiar_contrasena(self, empleado, nueva_contrasena, es_administrador=False):
        if es_administrador:
            # Cambia la contraseña del empleado
            empleado.password = nueva_contrasena
            # Actualiza el archivo Password.txt
        else:
            print("No tienes los permisos necesarios para realizar esta acción.")