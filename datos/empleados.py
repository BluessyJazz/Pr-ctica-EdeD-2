from usuario import Usuario

class Empleado(Usuario):
    def __init__(self, id, nombre, fecha_nac, ciudad_nac, dir, tel, email, cargo, password):
        super().__init__(id, nombre, fecha_nac, ciudad_nac, dir, tel, email)
        self.cargo = cargo
        self.password = password
