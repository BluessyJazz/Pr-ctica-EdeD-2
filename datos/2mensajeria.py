from usuario import Usuario
from empleados import Empleado
from registro import Registro
from datos.fecha import Fecha
from datos.direccion import Direccion
import csv

class Mensajeria(Registro):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.bandeja_entrada = []
        self.mensajes_leidos = []
        self.borradores = []

    def cargar_password_desde_archivo(self, archivo_password):
        with open(archivo_password, "r") as file:
            reader = csv.reader(file, delimiter=" ")
            for row in reader:
                # Obtener los datos del archivo
                cedula = int(row[0])
                password = row[1]
                descripcion = row[2]

                # Realizar las operaciones necesarias con los datos

    def verificar_credenciales(self, cedula, password):
        # Implementación para verificar las credenciales del usuario

    def agregar_empleado(self, empleado, es_administrador=False):
        if es_administrador:
            return self.agregar(empleado)
        else:
            print("No tienes los permisos necesarios para realizar esta acción.")

    def eliminar_empleado(self, cedula, es_administrador=False):
        if es_administrador:
            return self.eliminar(cedula)
        else:
            print("No tienes los permisos necesarios para realizar esta acción.")

    def cambiar_contrasena(self, empleado, nueva_contrasena, es_administrador=False):
        if es_administrador:
            # Cambia la contraseña del empleado
            empleado.password = nueva_contrasena
            # Actualiza el archivo Password.txt
        else:
            print("No tienes los permisos necesarios para realizar esta acción.")

    def cargar_mensajes_desde_archivo(self, archivo):
        with open(archivo, "r") as file:
            # Implementación para cargar los mensajes desde un archivo

    def guardar_borrador(self, mensaje):
        # Implementación para guardar el mensaje como borrador

    def descartar_borrador(self, mensaje):
        # Implementación para descartar un mensaje en borrador

    def enviar_mensaje(self, mensaje):
        # Implementación para enviar un mensaje a la bandeja de entrada del destinatario

    def bandeja_entrada_to_file(self, cedula):
        # Implementación para guardar la bandeja de entrada en un archivo

    def mensajes_leidos_to_file(self, cedula):
        # Implementación para guardar los mensajes leídos en un archivo

    def borradores_to_file(self, cedula):
        # Implementación para guardar los borradores en un archivo

    def abrir_bandeja_entrada_from_file(self, cedula):
        # Implementación para abrir la bandeja de entrada desde un archivo

    def abrir_mensajes_leidos_from_file(self, cedula):
        # Implementación para abrir los mensajes leídos desde un archivo

    def abrir_borradores_from_file(self, cedula):
        # Implementación para abrir los borradores desde un archivo
