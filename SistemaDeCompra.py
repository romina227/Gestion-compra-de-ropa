# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    # Getter para el nombre
    def get_nombre(self):
        return self._nombre

    # Getter para el precio
    def get_precio(self):
        return self._precio

    # Metodo para mostrar informacion del producto
    def mostrar_info(self):
        print(f"Producto: {self._nombre}, Precio: {self._precio}")


# Clase Ropa que hereda de Producto
class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    # Getter para la talla
    def get_talla(self):
        return self._talla

    # Metodo para mostrar informacion de la ropa
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self._talla}")


# Clase Camisa que hereda de Ropa
class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tejido):
        super().__init__(nombre, precio, talla)
        self._tipo_tejido = tipo_tejido

    # Metodo para mostrar informacion de la camisa
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Tejido: {self._tipo_tejido}")


# Clase Pantalon que hereda de Ropa
class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo):
        super().__init__(nombre, precio, talla)
        self._tipo = tipo

    # Metodo para mostrar informacion del pantalon
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de Pantalon: {self._tipo}")


# Clase Carrito para gestionar la compra
class Carrito:
    def __init__(self):
        self.productos = []  # Lista para almacenar los productos seleccionados

    # Metodo para agregar un producto al carrito
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"{producto.get_nombre()} agregado al carrito.")

    # Metodo para mostrar el resumen de la compra
    def mostrar_resumen(self):
        total = 0
        print("\nResumen de compra:")
        for producto in self.productos:
            producto.mostrar_info()
            total += producto.get_precio()
        print(f"Total a pagar: {total}")


# Funcion para mostrar el menu al usuario
def menu():
    carrito = Carrito()

    while True:
        print("\n--- Menu ---")
        print("1. Agregar Camisa")
        print("2. Agregar Pantalon")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            # Solicitar los datos de la camisa
            nombre = input("Nombre de la camisa: ")
            precio = float(input("Precio: "))
            talla = input("Talla: ")
            tipo_tejido = input("Tipo de tejido: ")
            camisa = Camisa(nombre, precio, talla, tipo_tejido)
            carrito.agregar_producto(camisa)

        elif opcion == "2":
            # Solicitar los datos del pantalon
            nombre = input("Nombre del pantalon: ")
            precio = float(input("Precio: "))
            talla = input("Talla: ")
            tipo = input("Tipo de pantalon: ")
            pantalon = Pantalon(nombre, precio, talla, tipo)
            carrito.agregar_producto(pantalon)

        elif opcion == "3":
            # Mostrar el contenido del carrito
            carrito.mostrar_resumen()

        elif opcion == "4":
            # Finalizar la compra y mostrar el resumen
            print("Compra finalizada.")
            carrito.mostrar_resumen()
            break

        else:
            # Manejar opcion invalida
            print("Opcion invalida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()

