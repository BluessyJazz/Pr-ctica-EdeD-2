from listas.double_list import DoubleList
from .empleado import Empleado
#from main_mensaje import *

class Mensaje:
    def __init__(self, id_mensaje, nombre_emisor, correo_receptor, titulo, mensaje, fecha, estado):
        self.id_mensaje = id_mensaje
        self.nombre_emisor = nombre_emisor
        self.correo_receptor = correo_receptor
        self.titulo = titulo
        self.mensaje = mensaje
        self.fecha = fecha
        self.estado = estado

    def __lt__(self, other):
        return self.id_mensaje < other.id_mensaje

class Sistema_Mensajes():
    def __init__(self):
        self.mensajes = DoubleList()
        self.noMensajes = 0

    '''def agregarMensaje(self, mensaje, nombre_emisor):
        # Agregar un nuevo usuario
        #Se importa del usuario que inicia sesión en main_mensaje
        correo = int(input("\nCorreo del usuario: "))
        emisor = sistema.buscarCorreo(correo)
        id_receptor = emisor.get_Id()
        archivo_mensaje = f"/txt/{id_receptor}_BA.txt"

        mensajes_receptor = self.cargarMensajes(archivo_mensaje, id_receptor)

        id_mensaje = sistema.mensajes_receptor + 1

        titulo = input("Titulo del mensaje: ")
        mensaje = input("Escriba el mensaje: ")
        fecha = None

        mensaje = Mensaje(id_mensaje, nombre_emisor, correo, titulo, mensaje, fecha)
                
        self.mensajes.addOrder(mensaje)
        self.noMensajes += 1

        
        print("\nMensaje enviado con éxito.")
       
        return True'''

    def cargarMensajes(self, archivo_mensaje, id):

        archivo_mensaje = f"txt/{id}_BA.txt"
        
        with open(archivo_mensaje, 'r') as file:
            for line in file:
                data = [x.strip() for x in line.split(" ")]
                id_mensaje = line
                nombre_emisor = data[1]
                correo = data[2]
                titulo = data[3]
                mensaje = data[4]
                fecha = data[5]

                mensaje = Mensaje(id_mensaje, nombre_emisor, correo, titulo, mensaje, fecha, None)
                               
                self.mensajes.addOrder(mensaje)
                self.noMensajes +=1

        return self.noMensajes

    def buscarMensaje(self, id):
        current = self.mensajes.head
        while current:
            if current.data.id == id:
                return current
            current = current.next
        return None
