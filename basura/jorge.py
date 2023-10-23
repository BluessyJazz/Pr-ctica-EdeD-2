def funcioninutil():
    
    print("hola")    
    
def cargar_empleados():
    empleados = []
    with open("txt/Empleados.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(" ")  # Suponiendo que los campos están separados por espacios
            empleado = {
                "nombre": datos[0],
                "cedula": datos[1],
                "fecha_nacimiento": f"{datos[2]}/{datos[3]}/{datos[4]}",  # Corrección en esta línea
                "ciudad_nacimiento": datos[5],
                "telefono": datos[6],
                "correo_electronico": datos[7],
                "direccion": {
                    "calle": datos[8],
                    "nomenclatura": datos[9],
                    "barrio": datos[10],
                    "ciudad": datos[11],
                    "urbanizacion": datos[12],
                    "numero_apartamento": datos[13] if datos[13] != "null" else None
                }
            }

    return empleados

def cargar_contraseñas():
    contraseñas = {}
    with open("txt/Password.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split()
            cedula = datos[0]
            contraseña = datos[1]
            rol = datos[2]
            contraseñas[cedula] = {"contraseña": contraseña, "rol": rol}
    return contraseñas

def verificar_acceso(usuarios, cedula, contraseña):
    if cedula in usuarios:
        if usuarios[cedula]["contraseña"] == contraseña:
            return usuarios[cedula]["rol"]
    return None

# Cargar las contraseñas y roles desde el archivo Password.txt
usuarios = cargar_contraseñas()

# Pedir al usuario que ingrese su cedula y contraseña
cedula_ingresada = input("Ingrese su número de identificación (cedula): ")
contraseña_ingresada = input("Ingrese su contraseña: ")

# Verificar el acceso y obtener el rol del usuario
rol_usuario = verificar_acceso(usuarios, cedula_ingresada, contraseña_ingresada)

if rol_usuario is not None:
    print(f"Bienvenido, usted es un {rol_usuario}.")  # Puedes personalizar el mensaje según el rol.
else:
    print("Acceso denegado. Verifique sus datos.")


def guardar_empleados(empleados):
    with open("txt/Empleados.txt", "w") as archivo_empleados:
        for empleado in empleados:
            empleado_info = " ".join([empleado["nombre"], empleado["cedula"], empleado["fecha_nacimiento"], empleado["ciudad_nacimiento"], empleado["telefono"], empleado["correo_electronico"]] + list(empleado["direccion"].values()))
            archivo_empleados.write(empleado_info + "\n")

def guardar_contraseñas(usuarios):
    with open("txt/Password.txt", "w") as archivo_password:
        for cedula, datos in usuarios.items():
            usuario_info = f"{cedula} {datos['contraseña']} {datos['rol']}"
            archivo_password.write(usuario_info + "\n")

def registrar_usuario(empleados, usuarios):
    cedula = input("Ingrese la cédula del nuevo usuario: ")
    if cedula in usuarios:
        print("El usuario ya existe.")
        return

    nombre = input("Ingrese el nombre y apellido  del nuevo usuario, separado por guiones: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd mm aaaa): ")
    ciudad_nacimiento = input("Ingrese la ciudad de nacimiento: ")
    telefono = input("Ingrese el número de teléfono: ")
    correo_electronico = input("Ingrese el correo electrónico: ")
    direccion = {
        "calle": input("Ingrese la calle: "),
        "nomenclatura": input("Ingrese la nomenclatura: "),
        "barrio": input("Ingrese el barrio: "),
        "ciudad": input("Ingrese la ciudad: "),
        "urbanizacion": input("Ingrese la urbanización: "),
        "numero_apartamento": input("Ingrese el número de apartamento (deje en blanco si no aplica): ") or "null"
    }
    contraseña = input("Ingrese la contraseña: ")
    rol = input("Ingrese el rol (empleado o administrador): ")

    # Agregar el nuevo usuario a la lista de empleados
    empleado = {
        "nombre": nombre,
        "cedula": cedula,
        "fecha_nacimiento": fecha_nacimiento,
        "ciudad_nacimiento": ciudad_nacimiento,
        "telefono": telefono,
        "correo_electronico": correo_electronico,
        "direccion": direccion
    }



    # Agregar el nuevo usuario a usuarios
    usuarios[cedula] = {"contraseña": contraseña, "rol": rol}

    # Actualizar los archivos Empleados.txt y Password.txt
    guardar_empleados(empleados)
    guardar_contraseñas(usuarios)

    print(f"Usuario {nombre} registrado con éxito.")

def cambiar_contraseña(usuarios):
    cedula = input("Ingrese la cédula del usuario cuya contraseña desea cambiar: ")
    if cedula in usuarios:
        nueva_contraseña = input("Ingrese la nueva contraseña: ")
        usuarios[cedula]["contraseña"] = nueva_contraseña
        print(f"Contraseña cambiada con éxito para el usuario con cédula {cedula}.")
        guardar_contraseñas(usuarios)
    else:
        print("Usuario no encontrado.")

def eliminar_usuario(empleados, usuarios):
    cedula = input("Ingrese la cédula del usuario que desea eliminar: ")
    if cedula in usuarios:
        # Eliminar el usuario de la lista de empleados
        empleados = [empleado for empleado in empleados if empleado["cedula"] != cedula]

        # Eliminar el usuario de usuarios
        del usuarios[cedula]

        # Actualizar los archivos Empleados.txt y Password.txt
        guardar_empleados(empleados)
        guardar_contraseñas(usuarios)

        print(f"Usuario con cédula {cedula} eliminado con éxito.")
    else:
        print("Usuario no encontrado.")

# Ejemplo de uso:
empleados = cargar_empleados()
usuarios = cargar_contraseñas()

if rol_usuario == "administrador":
    while True:
        print("\nMenú de administrador:")
        print("1. Registrar nuevo usuario")
        print("2. Cambiar contraseña de usuario")
        print("3. Eliminar usuario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(empleados, usuarios)
        elif opcion == "2":
            cambiar_contraseña(usuarios)
        elif opcion == "3":
            eliminar_usuario(empleados, usuarios)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")