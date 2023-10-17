import csv
from datos.fecha import Fecha
from datos.direccion import Direccion
from datos.usuario import Usuario

class Registro:
    def __init__(self, capacity):
        self.registro = [None] * capacity
        self.noRegistros = 0
    
    def agregar(self, usuario):
        # Comprobar si hay espacio en el arreglo
        if self.noRegistros == len(self.registro):
            print("No hay espacio para agregar más usuarios.")
            return False

        # Comprobar si ya existe un usuario con el mismo ID
        for i in range(self.noRegistros):
            if self.registro[i].id == usuario.id:
                print(f"Ya existe un usuario con el ID {usuario.id}.")
                return False

        # Agregar el usuario en orden ascendente por ID
        i = self.noRegistros - 1
        while i >= 0 and self.registro[i].id > usuario.id:
            self.registro[i + 1] = self.registro[i]
            i -= 1
        self.registro[i + 1] = usuario
        self.noRegistros += 1
        return True

    def eliminar(self, id):
        pos = self.buscarPosicion(id)
        if pos != -1:
            usuario_eliminado = self.registro[pos]
            for i in range(pos, self.noRegistros - 1):
                self.registro[i] = self.registro[i + 1]
            self.registro[self.noRegistros - 1] = None
            self.noRegistros -= 1
            return usuario_eliminado
        return None

    def buscarPosicion(self, id):
        for i in range(self.noRegistros):
            if self.registro[i].id == id:
                return i
        return -1

    def buscarUsuario(self, id):
        pos = self.buscarPosicion(id)
        if pos != -1:
            return self.registro[pos]
        return None

    def toFile(self, filename):
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)

            # Escribir los encabezados
            writer.writerow(["ID", "Nombre", "Fecha de nacimiento", "Ciudad de nacimiento", "Direccion", "Telefono", "Correo electronico"])

            # Escribir los datos de los usuarios
            for i in range(self.noRegistros):
                usuario = self.registro[i]

                # Formatear la dirección con espacios en lugar de comas
                direccion_str = f"{usuario.dir.calle}-{usuario.dir.noCalle}-{usuario.dir.nomenclatura}-{usuario.dir.barrio}-{usuario.dir.ciudad}"

                writer.writerow([usuario.id, usuario.nombre, usuario.fecha_nac.obtener_fecha(),
                                usuario.ciudad_nac, direccion_str, usuario.tel, usuario.email])


    def importar(self, filename):


        with open(filename, "r", newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.noRegistros = 0
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