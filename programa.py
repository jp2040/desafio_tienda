# programa.py
from tienda import Tienda, Restaurante, Supermercado, Farmacia
from producto import Producto

# Función para ingresar datos de un producto
def ingresar_datos_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto (si no indica, se asumirá 0): "))
    return Producto(nombre, precio, stock)

# Función principal del programa
def main():
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): ")
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery de la tienda: "))
    
    if tipo_tienda.lower() == "restaurante":
        tienda = Restaurante(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        tienda = Supermercado(nombre_tienda, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        tienda = Farmacia(nombre_tienda, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return

    while True:
        print("\nOpciones:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = ingresar_datos_producto()
            tienda.ingresar_producto(producto)
        elif opcion == "2":
            print(tienda.listar_productos())
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto que desea vender: ")
            cantidad = int(input("Ingrese la cantidad requerida: "))
            tienda.realizar_venta(nombre_producto, cantidad)
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Inténtelo nuevamente.")

if __name__ == "__main__":
    main()
