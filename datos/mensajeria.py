from listas.list import List  # Importa la clase List para usarla en el sistema de mensajería
from listas.double_list import DoubleList  # Importa la clase DoubleList para usarla en el sistema de mensajería
from dequeues.stack import Stack  # Importa la clase Stack para usarla en el sistema de mensajería
from dequeues.queue import Queue  # Importa la clase Queue para usarla en el sistema de mensajería

class Mensajeria:
    def __init__(self):
        self.employee_list = List()  # Lista de empleados
        self.message_queue = Queue()  # Cola de mensajes leídos
        self.draft_stack = Stack()  # Pila de borradores

    def verificar_credenciales(self, id, password):
        for empleado in self.employee_list:
            if empleado.id == id and empleado.password == password:
                return empleado
        return None