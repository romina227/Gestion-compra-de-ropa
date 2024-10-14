class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.cantidad}")


# Herencia
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # llamada al constructor de la clase Prenda
        self.talla = talla  # atributo de la clase RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # llama al metodo de la clase Prenda
        print(f"Talla: {self.talla}")


# polimorfismo

class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # hereda de Prenda
        self.talla = talla  # Atributo de Ropamujer

    def mostrar_info(self):  # metodo propio de la clase
        super().mostrar_info()
        print(f"Talla: {self.talla}")


# Abstraccion

class Inventario:
    def __init__(self):
        self.prendas = []  # lista para almacenar prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # agregar prenda a la lista

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()  # muestra la info de cada prenda


# implementacion

camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
falda = RopaMujer("Falda de Mujer", 28.00,15,"S")

# crear inventario y agregar prendas
inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(falda)

# mostrar el inventario
inventario.mostrar_inventario()
