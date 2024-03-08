# tienda.py
from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, producto):
        # Verificar si el producto ya existe en la tienda
        for p in self.__productos:
            if p.obtener_nombre() == producto.obtener_nombre():
                p.modificar_stock(p.obtener_stock() + producto.obtener_stock())
                return

        # Si el producto no existe, agregarlo a la lista de productos
        self.__productos.append(producto)

    def listar_productos(self):
        output = ""
        for producto in self.__productos:
            output += f"Nombre: {producto.obtener_nombre()}, Precio: ${producto.obtener_precio()}"
            if self.__es_supermercado() and producto.obtener_stock() < 10:
                output += " - Pocos productos disponibles"
            elif self.__es_farmacia() and producto.obtener_precio() > 15000:
                output += " - Envío gratis al solicitar este producto"
            elif self.__es_farmacia() or self.__es_supermercado():
                output += f", Stock: {producto.obtener_stock()}"
            output += "\n"
        return output

    def realizar_venta(self, nombre_producto, cantidad):
        # Verificar si el producto existe en la tienda
        for producto in self.__productos:
            if producto.obtener_nombre() == nombre_producto:
                if self.__es_restaurante():
                    # Productos de Restaurante siempre tienen stock 0, no es necesario hacer validaciones
                    pass
                elif self.__es_farmacia() and cantidad > 3:
                    # No se puede solicitar una cantidad superior a 3 en Farmacia
                    return
                elif self.__es_farmacia() or self.__es_supermercado():
                    # Verificar si hay suficiente stock para realizar la venta
                    cantidad_disponible = min(cantidad, producto.obtener_stock())
                    producto.modificar_stock(producto.obtener_stock() - cantidad_disponible)
                    return
        # Si el producto no existe en la tienda, no se realiza ninguna acción

    def __es_restaurante(self):
        return type(self) == Restaurante

    def __es_supermercado(self):
        return type(self) == Supermercado

    def __es_farmacia(self):
        return type(self) == Farmacia

class Restaurante(Tienda):
    pass

class Supermercado(Tienda):
    pass

class Farmacia(Tienda):
    pass
