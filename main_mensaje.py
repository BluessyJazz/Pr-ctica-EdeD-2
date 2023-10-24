import csv
from datos.direccion import Direccion
from datos.fecha import Fecha
from datos.empleado import Empleado
from datos.sistema_empleados import Sistema_Empleados
from datos.menu import Menu
from datos.menu_admin import *
from datos.sistema_mensajes import Sistema_Mensajes

txtempleados = "txt/Empleados.txt"
txtpassword = "txt/Password.txt"

sistema = Sistema_Empleados()
empleados = sistema.empleados

sistema.cargarEmpleados(txtempleados)
sistema.cargarPassword(txtpassword)

while True:
    # Pedir al usuario que ingrese su cedula y contraseña
    id_usuario = int(input("\nIngrese su número de identificación (cedula): "))
    
    if id_usuario == 0000:
        print("\nGOOD BYE!\n")
        break

    contraseña_ingresada = str(input("Ingrese su contraseña: "))

    # Verificar el acceso y obtener el rol del usuario
    rol_usuario = sistema.verificarAcceso(id_usuario, contraseña_ingresada)

    if rol_usuario == "administrador":
        print(f"\nBienvenido, usted es {rol_usuario}.")

        #Opción de menú de admin y menú de mensajes
        
        #menu = Menu()

        #menu.menu_admin(sistema, txtempleados, txtpassword)
        menu_admin(sistema, txtempleados, txtpassword)


    if rol_usuario == "empleado" or rol_usuario == "administrador":
        print(f"\nBienvenido, usted es un {rol_usuario}.\n")

        sistema_mensajes = Sistema_Mensajes()

        archivo_mensaje = f"txt/{id_usuario}_BA.txt"

        print("Usted tiene", sistema_mensajes.cargarEntrada(archivo_mensaje, id_usuario), "mensajes nuevos.")


        while True:
            print("\nUsted tiene", sistema_mensajes.cargarLeidos(archivo_mensaje, id_usuario), "mensajes leídos.")
            print("\nUsted tiene", sistema_mensajes.cargarBorradores(archivo_mensaje, id_usuario), "borradores.")

            print("\nMENU DE MENSAJES:")
            print("\n1. Escribir mensaje")
            print("\n2. Ver bandeja de entrada")
            print("\n3. Ver mensajes leídos")
            print("\n4. Ver mensajes en borradores")
            print("\n5. Cerrar Sesión")
            
            opcion = int(input("\nSeleccione una opción: "))

            if opcion == 1:
                mensajeescrito = sistema_mensajes.escribirMensaje(sistema, id_usuario)

                print("\n1. Enviar el mensaje")
                print("\n2. Guardar como borrador")
                print("\n3. Descartar el mensaje")

                select = int(input("\nQué desea hacer?: "))

                if select == 1:
                    sistema_mensajes.guardarMensajes(sistema, mensajeescrito)
                elif select == 2:
                    sistema_mensajes.guardarBorradores(id_usuario, mensajeescrito)
                    print("Usted tiene", sistema_mensajes.cargarBorradores(archivo_mensaje, id_usuario), "borradores.")

                elif select == 3:
                    print("\nMensaje descartado")
            
            elif opcion == 2:
                sistema_mensajes.mostrarBandejaEntrada()

                print("\n1. Leer un mensaje")
                print("\n2. Ir Atrás")

                select = int(input("\nQué desea hacer?: "))
                
                if select == 1:
                    id = int(input(("\nQué número de mensaje desea leer?: ")))

                    sistema_mensajes.mostrarMensaje(id, id_usuario)
                    
                elif select == 2:
                    print("\n")

            elif opcion == 3:
                mensajecero = (sistema_mensajes.mensajesLeidos.first())
                print(f"\n{mensajecero.titulo}\n{mensajecero.mensaje}")
                sistema_mensajes.mensajesLeidos.enqueue(mensajecero)
                sistema_mensajes.mensajesLeidos.dequeue()
                while (sistema_mensajes.mensajesLeidos.first()) != mensajecero:
                    print("\nExit para salir")
                    select = input("\nEnter: siguiente mensaje: ")
                    primerMensaje = (sistema_mensajes.mensajesLeidos.first())
                    print(f"\n{primerMensaje.titulo}\n{primerMensaje.mensaje}")
                    sistema_mensajes.mensajesLeidos.enqueue(primerMensaje)
                    sistema_mensajes.mensajesLeidos.dequeue()
                    

                    #select = input("\nEnter: siguiente mensaje: ")

                    if select == "exit":
                        break
                    else:
                        print("\n")
                        
            elif opcion == 4:
                while True:
                    borrador = (sistema_mensajes.mensajesBorradores.top())

                    if borrador is not None:
                        print(f"\nTitulo: {borrador.titulo}\nMensaje: {borrador.mensaje}\nPara: {borrador.nombre_receptor}")

                        print("\n1. Enviar el mensaje")
                        print("\n2. Descartar borrador")
                        print("\n3. Volver atrás")

                        select = int(input("\nQué desea hacer?: "))

                        if select == 1:
                            sistema_mensajes.guardarMensajes(sistema, borrador)
                            sistema_mensajes.mensajesBorradores.pop()
                        elif select == 2:
                            descartado = sistema_mensajes.mensajesBorradores.pop()
                            print("\nHa sido descartado el mensaje", descartado.titulo)
                        elif select == 3:
                            sistema_mensajes.guardarBorradoresPop(id_usuario)
                            break
                        else:
                            print("\nOpción no válida.")
                        
                    else:
                        print("\nNo hay borradores aquí")
                        sistema_mensajes.guardarBorradoresPop(id_usuario)
                        break
                
            elif opcion == 5:
                break
                            
        
    else:
        print("\nAcceso denegado. Verifique sus datos e intente nuevamente.")