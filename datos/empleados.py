from .usuario import Usuario

class Empleado(Usuario):
    def __init__(self, id, nombre, fecha_nac, ciudad_nac, dir, tel, email, cargo, password):
        super().__init__(id, nombre, fecha_nac, ciudad_nac, dir, tel, email)
        self.cargo = cargo
        self.password = password
    
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Fecha de Nacimiento: {self.fecha_nac.obtener_fecha()}, Ciudad de Nacimiento: {self.ciudad_nac}, Direccion: {self.dir}, Telefono: {self.tel}, Email: {self.email}, Cargo: {self.cargo}, Password: {self.password}"
    
    def setPassword(self, password):
        self.password = password

    def setCargo(self, cargo):
        self.cargo = cargo