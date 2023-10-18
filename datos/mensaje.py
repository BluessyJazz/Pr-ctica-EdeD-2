class Message:
    def __init__(self, cedula_emisor, cedula_receptor, titulo, mensaje, fecha_envio):
        self.cedula_emisor = cedula_emisor
        self.cedula_receptor = cedula_receptor
        self.titulo = titulo
        self.mensaje = mensaje
        self.fecha_envio = fecha_envio
