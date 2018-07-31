class Articulo(object):
    def __init__(self, nombre, descripcion, cantidad, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.categoria = categoria

    def modificar(self, nombre, descripcion, cantidad, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.categoria= categoria
