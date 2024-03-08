class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)

    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_precio(self):
        return self.__precio
    
    def obtener_stock(self):
        return self.__stock
    
    def modificar_stock(self, cantidad):
        self.__stock = max(0, cantidad)