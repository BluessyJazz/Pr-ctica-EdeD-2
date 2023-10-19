class Usuario:
    def __init__(self, id, nombre, fecha_nac, ciudad_nac, dir, tel, email):
        self.id = id
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.ciudad_nac = ciudad_nac
        self.dir = dir
        self.tel = tel
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Fecha de Nacimiento: {self.fecha_nac.obtener_fecha()}, Ciudad de Nacimiento: {self.ciudad_nac}, Direccion: {self.dir}, Telefono: {self.tel}, Email: {self.email}"

    def __lt__(self, other):
        return self.id < other.id
    
    def getId(self):
        return self.id