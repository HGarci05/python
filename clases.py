class Cliente:
    def __init__(self, nombre, direccion, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = {}  # diccionario de productos y cantidades

    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:  # verificar si hay suficiente stock
            if producto in self.productos:
                self.productos[producto] += cantidad
            else:
                self.productos[producto] = cantidad
            producto.stock -= cantidad  # actualizar el stock del producto
            print(f"Producto '{producto.nombre}' agregado al pedido")
        else:
            print(f"No hay suficiente stock de '{producto.nombre}'")

    def generar_factura(self):
        print("Factura:")
        print(f"Cliente: {self.cliente.nombre}")
        print("Productos comprados:")
        for producto, cantidad in self.productos.items():
            print(f"- {cantidad} unidades de '{producto.nombre}'")

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos.items())
        return total


cliente1 = Cliente("Juan Perez", "Calle A, Ciudad B", "123456789", "juan@example.com")
producto1 = Producto("Producto1", 10.0, 20)
pedido1 = Pedido(cliente1)

pedido1.agregar_producto(producto1, 5)
pedido1.agregar_producto(producto1, 10)  # Intentar agregar más productos de los disponibles
pedido1.generar_factura()

total_pedido1 = pedido1.calcular_total()
print(f"Total del pedido: ${total_pedido1}")

