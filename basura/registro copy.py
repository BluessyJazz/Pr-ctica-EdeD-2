import csv
from datos.fecha import Fecha
from datos.direccion import Direccion
from datos.usuario import Usuario

from .list import List  # Asegúrate de tener la implementación de la clase List disponible

class Registro:
    def __init__(self):
        self.registro = List()  # Inicializa la lista enlazada

    def agregarUsuario(self, usuario):
        if self.registro.search(usuario.id):
            print(f"Ya existe un usuario con el ID {usuario.id}.")
            return False
        self.registro.add(usuario)
        return True

    def eliminarUsuario(self, id):
        if self.registro.search(id):
            return self.registro.remove(id)
        return None

    def buscarUsuario(self, id):
        if self.registro.search(id):
            return self.registro.search(id).data
        return None

    def toFile(self, filename):
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)

            # Escribir los encabezados
            writer.writerow(["ID", "Nombre", "Fecha de nacimiento", "Ciudad de nacimiento", "Direccion", "Telefono", "Correo electronico"])

            # Escribir los datos de los usuarios
            current = self.registro.head
            while current:
                usuario = current.data

                # Formatear la dirección con espacios en lugar de comas
                direccion_str = f"{usuario.dir.calle}-{usuario.dir.noCalle}-{usuario.dir.nomenclatura}-{usuario.dir.barrio}-{usuario.dir.ciudad}"

                writer.writerow([usuario.id, usuario.nombre, usuario.fecha_nac.obtener_fecha(),
                                usuario.ciudad_nac, direccion_str, usuario.tel, usuario.email])
                current = current.next

    def importar(self, filename):
        with open(filename, "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
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

                usuario = Usuario(id, nombre, fecha_nac, ciudad_nac, dir, tel, email)
                self.agregar(usuario)
