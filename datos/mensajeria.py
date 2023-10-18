import csv
from listas.list import List  # Importa la clase List para usarla en el sistema de mensajería
from listas.double_list import DoubleList  # Importa la clase DoubleList para usarla en el sistema de mensajería
from dequeues.stack import Stack  # Importa la clase Stack para usarla en el sistema de mensajería
from dequeues.queue import Queue  # Importa la clase Queue para usarla en el sistema de mensajería
from .empleados import Empleado
from .admin import Administrador
from .fecha import Fecha
from .direccion import Direccion
from registro import Registro

class Mensajeria:
    def __init__(self):
        self.empleados = List()  # Lista de empleados
        self.noEmpleados = 0
        self.message_queue = Queue()  # Cola de mensajes leídos
        self.draft_stack = Stack()  # Pila de borradores

    def agregarEmpleado(self, empleado):
        if self.registro.search(empleado.id):
            print(f"Ya existe un usuario con el ID {empleado.id}.")
            return False
        self.empleados.add(empleado)
        self.noEmpleados +=1
        return True

    def eliminarEmpleado(self, id):
        if self.empleados.search(id):
            return self.empleados.remove(id)
            self.noEmpleados -= 1
        return None

    def buscarUsuario(self, id):
        if self.empleados.search(id):
            return self.empleados.search(id).data
        return None
    
    def cargarEmpleados(self, archivo_empleados):

        with open(archivo_empleados, "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.noEmpleados = 0
            for row in reader:
                id = int(row['ID'])
                nombre = row['Nombre']
                fecha_nac_str = row['Fecha de nacimiento']
                fecha_nac_data = fecha_nac_str.split('/')
                dia, mes, año = map(int, fecha_nac_data)
                fecha_nac = Fecha(dia, mes, año)
                ciudad_nac = row['Ciudad de nacimiento']

                direccion_data = row['Direccion'].split('-')
                calle = direccion_data[0]
                noCalle = direccion_data[1]
                nomenclatura = direccion_data[2]
                barrio = direccion_data[3]
                ciudad = direccion_data[-1]

                dir = Direccion(calle, noCalle, nomenclatura, barrio, ciudad)
                tel = int(row['Telefono'])
                email = row['Correo electronico']

                empleado = Empleado(id, nombre, fecha_nac, ciudad_nac, dir, tel, email)
                self.agregarEmpleado(empleado)
                self.noEmpleados +=1

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
        # Implementación para verificar las credenciales del usuario
            def verificar_credenciales(self, id, password):
        for empleado in self.employee_list:
            if empleado.id == id and empleado.password == password:
                return empleado
        return None

    def agregar_empleado(self, empleado, es_administrador=False):
        if es_administrador:
            return self.agregar(empleado)
        else:
            print("No tienes los permisos necesarios para realizar esta acción.")

    def eliminar_empleado(self, id, es_administrador=False):
        if es_administrador:
            return self.eliminar(id)
        else:
            print("No tienes los permisos necesarios para realizar esta acción.")

    def cambiar_contrasena(self, empleado, nueva_contrasena, es_administrador=False):
        if es_administrador:
            # Cambia la contraseña del empleado
            empleado.password = nueva_contrasena
            # Actualiza el archivo Password.txt
        else:
            print("No tienes los permisos necesarios para realizar esta acción.")
