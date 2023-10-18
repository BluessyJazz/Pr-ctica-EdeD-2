from empleados import Empleado

class Administrador(Empleado):
    def __init__(self, id, nombre, fecha_nac, ciudad_nac, dir, tel, email, cargo, password, privilegios):
        super().__init__(id, nombre, fecha_nac, ciudad_nac, dir, tel, email, cargo, password)
        self.privilegios = privilegios
        # Agrega más atributos y métodos específicos para el administrador
