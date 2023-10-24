from listas.double_list import DoubleList
from .empleado import Empleado
from .sistema_empleados import Sistema_Empleados
from datetime import datetime
from dequeues.queue import Queue
from dequeues.stack import Stack 
#from main_mensaje import *

class Mensaje:
    def __init__(self, id_mensaje, nombre_emisor, correo_emisor, nombre_receptor, correo_receptor, titulo, mensaje, fecha, estado):
        self.id_mensaje = id_mensaje
        self.nombre_emisor = nombre_emisor
        self.nombre_receptor = nombre_receptor
        self.correo_receptor = correo_receptor
        self.correo_emisor = correo_emisor
        self.titulo = titulo
        self.mensaje = mensaje
        self.fecha = fecha
        self.estado = estado

    def __str__(self):
        return f"#{self.id_mensaje} '{self.titulo}', Fecha: {self.fecha}\nDe: '{self.nombre_emisor}' ({self.correo_emisor}), Para: {self.correo_receptor}"
    
    def __lt__(self, other):
        #return self.id_mensaje < other.id_mensaje
        return self.fecha < other.fecha

class Sistema_Mensajes():
    def __init__(self):
        self.mensajes = DoubleList()
        self.mensajesEnviar = DoubleList()
        self.mensajesLeidos = Queue()
        self.mensajesBorradores = Stack()
        self.noMensajes = 0

    def escribirMensaje(self, sistemaemp, id_emisor):
        correo_receptor = input("\nPara(correo) : ")
        receptor = sistemaemp.buscarCorreo(correo_receptor)
        id_receptor = receptor.data.id
        nombre_receptor = receptor.data.nombre
        archivo_mensaje = f"/txt/{id_receptor}_BA.txt"
        
        emisor = sistemaemp.buscarUsuario(id_emisor)
        nombre_emisor = emisor.data.nombre
        correo_emisor = emisor.data.email

        titulo = input("Titulo del mensaje: ")
        mensaje = input("Escriba el mensaje: ")
        fecha = None

        mensaje = Mensaje(0, nombre_emisor, correo_emisor, nombre_receptor, correo_receptor, titulo, mensaje, fecha, None)
               
        return mensaje

    def cargarEntrada(self, archivo_mensaje, id):

        archivo_mensaje = f"txt/{id}_BA.txt"
        
        id_mensaje = 0

        with open(archivo_mensaje, 'r') as file:
            for line in file:
                data = [x.strip() for x in line.split("|")]
                id_mensaje += 1
                nombre_emisor = data[1]
                correo_emisor = data[2]
                nombre_receptor = data[3]
                correo_receptor = data[4]
                titulo = data[5]
                mensaje = data[6]
                fecha = data[7]
                estado = data[8]

                mensaje = Mensaje(id_mensaje, nombre_emisor, correo_emisor, nombre_receptor, correo_receptor, titulo, mensaje, fecha, estado)
                
            
                if estado == "entrada":
                    self.mensajes.addOrder(mensaje)
                else:
                    return None
                self.noMensajes +=1
                
        return id_mensaje
    
    def cargarLeidos(self, archivo_mensaje, id):

        archivo_mensaje = f"txt/{id}_ML.txt"
        
        id_mensaje = 0

        with open(archivo_mensaje, 'r') as file:
            for line in file:
                data = [x.strip() for x in line.split("|")]
                id_mensaje += 1
                nombre_emisor = data[1]
                correo_emisor = data[2]
                nombre_receptor = data[3]
                correo_receptor = data[4]
                titulo = data[5]
                mensaje = data[6]
                fecha = data[7]
                estado = data[8]

                mensaje = Mensaje(id_mensaje, nombre_emisor, correo_emisor, nombre_receptor, correo_receptor, titulo, mensaje, fecha, estado)
                

                self.mensajesLeidos.enqueue(mensaje)
                                    
        return id_mensaje
    
    def cargarBorradores(self, archivo_mensaje, id):

        archivo_mensaje = f"txt/{id}_B.txt"
        
        id_mensaje = 0

        with open(archivo_mensaje, 'r') as file:
            for line in file:
                data = [x.strip() for x in line.split("|")]
                id_mensaje += 1
                nombre_emisor = data[1]
                correo_emisor = data[2]
                nombre_receptor = data[3]
                correo_receptor = data[4]
                titulo = data[5]
                mensaje = data[6]
                fecha = data[7]
                estado = data[8]

                mensaje = Mensaje(id_mensaje, nombre_emisor, correo_emisor, nombre_receptor, correo_receptor, titulo, mensaje, fecha, estado)
                
                if estado == "borrador":
                    self.mensajesBorradores.push(mensaje)
                                    
        return id_mensaje

    def guardarMensajes(self, sistemaemp, mensaje):
        receptor = sistemaemp.buscarCorreo(mensaje.correo_receptor)
        id_receptor = receptor.data.id
        nombre_receptor = receptor.data.nombre
        archivo_entrada = f"txt/{id_receptor}_BA.txt"
        fecha_actual = datetime.now().strftime("%d/%m/%Y-%H:%M")
        with open(archivo_entrada, "a") as file:

            line = f"0|{mensaje.nombre_emisor}|{mensaje.correo_emisor}|{mensaje.nombre_receptor}|{mensaje.correo_receptor}|{mensaje.titulo}|{mensaje.mensaje}|{fecha_actual}|entrada\n"
            file.write(line)
        
        return print(f"\nMensaje enviado con éxito a {nombre_receptor}.")     
        
    def guardarBorradores(self, id_usuario, mensaje):
        archivo_entrada = f"txt/{id_usuario}_B.txt"
        fecha_actual = datetime.now().strftime("%d/%m/%Y-%H:%M")
        with open(archivo_entrada, "a") as file:
            line = f"0|{mensaje.nombre_emisor}|{mensaje.correo_emisor}|{mensaje.nombre_receptor}|{mensaje.correo_receptor}|{mensaje.titulo}|{mensaje.mensaje}|{fecha_actual}|borrador\n"
            file.write(line)

        return print(f"\nMensaje guardado con éxito en borradores.")
              
    def mostrarBandejaEntrada(self):
        print("\nBANDEJA DE ENTRADA\n")
        current = self.mensajes.head
        while current is not None:
            if current.data.estado == "entrada":
                print(f"{current.get_data()}\n")  # Aquí asumimos que get_data() devuelve el valor almacenado en el nodo
            current = current.next
        return self.mensajes
    
    def buscarMensaje(self, id):
        current = self.mensajes.head
        while current:
            if current.data.id_mensaje == id:
                return current
            current = current.next
        return None
    
    def buscarMensajem(self, mensaje):
        current = self.mensajes.head
        while current:
            if current == mensaje:
                return current
            current = current.next
        return None

    def mostrarMensaje(self, id, id_usuario):
        mensajeleer = self.buscarMensaje(id)
        print(f"\n{mensajeleer.data.titulo}\n{mensajeleer.data.mensaje}")
        mensajeleer.estado = "leido"
        self.mensajes.remove(mensajeleer)
        self.mensajesLeidos.enqueue(mensajeleer)
        self.actualizarEntrada(id_usuario, mensajeleer)

    def actualizarEntrada(self, id_usuario, mensaje):
        # Llama al método guardarLeidos
        self.guardarLeidos(id_usuario, mensaje)
        archivo_entrada = f"txt/{id_usuario}_BA.txt"              
        with open(archivo_entrada, "w") as file:
            mensaje = self.mensajes.head
            while mensaje is not None:
                line = f"0|{mensaje.data.nombre_emisor}|{mensaje.data.correo_emisor}|{mensaje.data.nombre_receptor}|{mensaje.data.correo_receptor}|{mensaje.data.titulo}|{mensaje.data.mensaje}|{mensaje.data.fecha}|entrada\n"
                file.write(line)
                mensaje = mensaje.next
                                     
    def guardarLeidos(self, id_usuario, mensaje):
        archivo_leidos = f"txt/{id_usuario}_ML.txt"
        with open(archivo_leidos, "a") as file:
            mensaje = mensaje.data
            line = f"0|{mensaje.nombre_emisor}|{mensaje.correo_emisor}|{mensaje.nombre_receptor}|{mensaje.correo_receptor}|{mensaje.titulo}|{mensaje.mensaje}|{mensaje.fecha}|leido\n"
            file.write(line)

    def guardarBorradoresPop(self, id_usuario):
        archivo_leidos = f"txt/{id_usuario}_B.txt"
        with open(archivo_leidos, "w") as file:
            while self.mensajesBorradores.top() is not None:
                mensaje = self.mensajesBorradores.pop()
                line = f"0|{mensaje.nombre_emisor}|{mensaje.correo_emisor}|{mensaje.nombre_receptor}|{mensaje.correo_receptor}|{mensaje.titulo}|{mensaje.mensaje}|{mensaje.fecha}|borrador\n"
                file.write(line)