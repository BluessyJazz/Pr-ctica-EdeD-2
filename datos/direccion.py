class Direccion:
    def __init__(self, calle, noCalle, nomenclatura, barrio, ciudad):
        self.calle = calle
        self.noCalle = noCalle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad

    def __str__(self):
        direccion_str = f"Calle {self.calle} No {self.noCalle} - {self.nomenclatura} Barrio {self.barrio} - {self.ciudad}"
        return direccion_str