import csv
from datos.direccion import Direccion
from datos.fecha import Fecha
from datos.registro import Registro
from datos.usuario import Usuario

#Ubicación del CSV
filename = "txt/datos.txt"

def mostrar_menu():
    print("\nMENU:")
    print("1. Agregar usuario")
    print("2. Eliminar usuario")
    print("3. Buscar usuario por ID")
    print("4. Mostrar todos los usuarios")
    print("5. Guardar en archivo CSV")
    print("6. Guardar y SALIR")
    print("7. Salir SIN GUARDAR")

# Crear un registro con capacidad para 100 usuarios
registro = Registro(100)

# Importar datos de un archivo CSV (si existe)
registro.importar(filename)
print(len(registro.registro))
print(registro.noRegistros)

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Agregar un nuevo usuario
        id = int(input("ID del usuario: "))
        nombre = input("Nombre del usuario: ")
        fecha_nac = Fecha(*map(int, input("Fecha de nacimiento (dd/mm/aaaa): ").split("/")))
        ciudad_nac = input("Ciudad de nacimiento: ")
        dir = Direccion(*input("Dirección (calle, noCalle, nomenclatura, barrio, ciudad): ").split(", "))
        tel = int(input("Teléfono: "))
        email = input("Correo electrónico: ")

        nuevo_usuario = Usuario(id, nombre, fecha_nac, ciudad_nac, dir, tel, email)
        if registro.agregar(nuevo_usuario):
            print("Usuario agregado con éxito.")
        else:
            print("No se pudo agregar el usuario.")

    elif opcion == "2":
        # Eliminar un usuario por ID
        id = int(input("ID del usuario a eliminar: "))
        usuario_eliminado = registro.eliminar(id)
        if usuario_eliminado:
            print(f"Usuario eliminado:\n{usuario_eliminado}")
        else:
            print("Usuario no encontrado.")

    elif opcion == "3":
        # Buscar un usuario por ID
        id = int(input("ID del usuario a buscar: "))
        usuario_buscado = registro.buscarUsuario(id)
        if usuario_buscado:
            print(usuario_buscado)
        else:
            print("Usuario no encontrado.")

    elif opcion == "4":
        # Mostrar todos los usuarios
        print("\nLISTA DE USUARIOS:")
        for i in range(registro.noRegistros):
            print(registro.registro[i])

    elif opcion == "5":
        # Guardar los datos en un archivo CSV
        registro.toFile(filename)
        print("Datos guardados en el archivo 'datos.csv'.")

    elif opcion == "6":
        # Guardar los datos en un archivo CSV
        registro.toFile(filename)
        print("Datos guardados en el archivo 'datos.csv'.")
        break

    elif opcion == "7":
        # Salir del programa
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")