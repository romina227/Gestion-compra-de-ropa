Sistema de Compras de Ropa con POO

Descripción:
Este proyecto es un sistema de compra de ropa implementado en Python utilizando los 4 pilares de la Programación Orientada a Objetos (POO): Encapsulamiento, Herencia, Polimorfismo y Abstracción. El usuario puede seleccionar distintos tipos de ropa, agregarlos al carrito y ver un resumen de su compra.

Estructura del Proyecto:
El proyecto sigue una jerarquía clara de clases para representar los productos y el proceso de compra.

Producto:
Clase base que representa un producto genérico. Define los atributos comunes como nombre y precio.

Ropa (hereda de Producto):
Subclase que representa ropa en general, añadiendo el atributo talla.

Camisa (hereda de Ropa):
Clase específica para camisas, con un atributo adicional tipo_tejido.

Pantalon (hereda de Ropa):
Clase específica para pantalones, con un atributo adicional tipo.

Carrito:
Clase que gestiona los productos seleccionados y permite calcular el total de la compra.

Pilares de POO Implementados
Encapsulamiento:

Los atributos de las clases son privados y accesibles solo a través de métodos get y set.
Herencia:

Las clases Camisa y Pantalon heredan de Ropa, que a su vez hereda de Producto.
Polimorfismo:

Cada clase específica (Camisa y Pantalon) sobrescribe el método mostrar_info() para mostrar su información personalizada.
Abstracción:

La clase Carrito oculta los detalles del manejo de productos y se encarga de toda la lógica de la compra.
Uso del Sistema
*****************
Menú de opciones:

Agregar una camisa.
Agregar un pantalón.
Ver el contenido del carrito.
Finalizar la compra.
Interacción con el usuario:

El usuario selecciona productos y la aplicación calcula el total automáticamente al finalizar la compra.
Cómo ejecutar el proyecto:
Asegúrate de tener Python 3 instalado en tu sistema.
Clona este repositorio:


git clone <URL_del_Repositorio>
cd <directorio_del_proyecto>

Ejecuta el archivo principal:

python SistemaDeCompra.py

Ejemplo de Ejecución:

--- Menu ---
1. Agregar Camisa
2. Agregar Pantalon
3. Ver carrito
4. Finalizar compra
Seleccione una opcion: 1
Nombre de la camisa: Polo
Precio: 25
Talla: M
Tipo de tejido: Algodon
Polo agregado al carrito.

--- Menu ---
1. Agregar Camisa
2. Agregar Pantalon
3. Ver carrito
4. Finalizar compra
Seleccione una opcion: 3

Resumen de compra:
Producto: Polo, Precio: 25.0
Talla: M
Tipo de Tejido: Algodon
Total a pagar: 25.0

