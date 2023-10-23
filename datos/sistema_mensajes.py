from listas.double_list import DoubleList
from .empleado import Empleado
from ..main_mensaje import *

class Mensaje:
    def __init__(self, id_mensaje, nombre_emisor, correo_receptor, titulo, mensaje, fecha, estado):
        self.id_mensaje = id_mensaje
        self.nombre_emisor = nombre_emisor
        self.correo_receptor = correo_receptor
        self.titulo = titulo
        self.mensaje = mensaje
        self.fecha = fecha
        self.estado = estado

class Sistema_Mensajes(Empleado, Mensaje):
    def __init__(self):
        self.mensajes = DoubleList()
        self.noMensajes = 0

    def agregarMensaje(self, mensaje):
        # Agregar un nuevo usuario
        nombre_emisor = id_usuario #Se importa del usuario que inicia sesión en main_mensaje
        correo = int(input("\nCorreo del usuario: "))
        emisor = sistema.buscarCorreo(correo)
        id_receptor = emisor.get_Id()
        archivo_mensaje = f"/txt/{id_receptor}.txt"

        mensajes_receptor = self.cargarMensajes(archivo_mensaje, id_receptor)

        id_mensaje = sistema.mensajes_receptor.noMensajes + 1

        titulo = input("Titulo del mensaje: ")
        mensaje = input("Escriba el mensaje: ")
        fecha = None

        mensaje = Mensaje(id_mensaje, nombre_emisor, correo, titulo, mensaje, fecha)
                
        self.empleados.addOrder(empleado)
        id +=1
        self.createtxt(empleado.id)
        
            print("\nUsuario agregado con éxito.")
       
        return True

    def cargarMensajes(self, archivo_mensaje, id):

        archivo_mensaje = f"/txt/{id}.txt"
        
        with open(archivo_mensaje, 'r') as file:
            for line in file:
                data = [x.strip() for x in line.split(" ")]
                id_mensaje = data[0]
                nombre_emisor = data[1]
                correo = data[2]
                titulo = data[3]
                mensaje = data[4]
                fecha = data[5]

                mensaje = Mensaje(id_mensaje, nombre_emisor, correo, titulo, mensaje, fecha)
                               
                self.mensajes.addOrder()
                self.noMensajes +=1

        return self.mensajes

    def buscarMensaje(self, id):
        current = self.mensajes.head
        while current:
            if current.data.id == id:
                return current
            current = current.next
        return None
