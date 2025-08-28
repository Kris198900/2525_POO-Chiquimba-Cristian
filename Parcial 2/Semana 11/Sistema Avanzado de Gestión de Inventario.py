import json
import os


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print(f"Error: Ya existe un producto con ID {producto.id}")
            return False
        self.productos[producto.id] = producto
        return True

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            return True
        print(f"Error: No existe un producto con ID {id}")
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id not in self.productos:
            print(f"Error: No existe un producto con ID {id}")
            return False

        if cantidad is not None:
            self.productos[id].cantidad = cantidad
        if precio is not None:
            self.productos[id].precio = precio
        return True

    def buscar_producto(self, nombre):
        nombre = nombre.lower()
        resultados = []
        for producto in self.productos.values():
            if nombre in producto.nombre.lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n=== INVENTARIO COMPLETO ===")
        print(f"{'ID':<5} {'Nombre':<25} {'Cantidad':<10} {'Precio':<10}")
        print("-" * 55)
        for producto in self.productos.values():
            print(f"{producto.id:<5} {producto.nombre:<25} {producto.cantidad:<10} ${producto.precio:<9.2f}")

    def guardar_a_json(self, nombre_archivo="inventario.json"):
        datos = {
            'carniceria': 'Sabores Andinos',
            'dueño': 'Cristian Chiquimba',
            'productos': []
        }

        for producto in self.productos.values():
            datos['productos'].append({
                'id': producto.id,
                'nombre': producto.nombre,
                'cantidad': producto.cantidad,
                'precio': producto.precio
            })

        with open(nombre_archivo, 'w') as f:
            json.dump(datos, f, indent=4)
        print(f"Inventario guardado en {nombre_archivo}")

    def cargar_desde_json(self, nombre_archivo="inventario.json"):
        # Verificar si el archivo existe sin mostrar mensaje de error
        if not os.path.exists(nombre_archivo):
            return False

        try:
            with open(nombre_archivo, 'r') as f:
                datos = json.load(f)

            self.productos = {}
            for item in datos['productos']:
                producto = Producto(
                    item['id'],
                    item['nombre'],
                    item['cantidad'],
                    item['precio']
                )
                self.productos[producto.id] = producto

            print(f"Inventario cargado desde {nombre_archivo}")
            print(f"Carnicería: {datos.get('carniceria', 'Desconocida')}")
            print(f"Dueño: {datos.get('dueño', 'Desconocido')}")
            return True
        except:
            print(f"Error al cargar el archivo {nombre_archivo}")
            return False


def precargar_productos(inventario):
    productos_iniciales = [
        # Carnes de Res
        Producto("CR001", "Carne de Res (lomo) kg", 50, 6.50),
        Producto("CR002", "Carne de Res (punta de anca) kg", 40, 5.00),
        Producto("CR003", "Carne de Res (molida) kg", 60, 4.80),
        Producto("CR004", "Carne de Res (costilla) kg", 35, 4.20),
        Producto("CR005", "Hígado de Res kg", 30, 2.50),
        Producto("CR006", "Molleja de Res kg", 25, 3.00),

        # Carnes de Cerdo
        Producto("CC001", "Carne de Cerdo (lomo) kg", 45, 5.20),
        Producto("CC002", "Carne de Cerdo (costeleta) kg", 40, 4.80),
        Producto("CC003", "Chuleta de Cerdo kg", 35, 5.50),
        Producto("CC004", "Panceta de Cerdo kg", 30, 4.00),

        # Pollos
        Producto("PO001", "Pechuga de Pollo (kg)", 50, 3.80),
        Producto("PO002", "Muslo de Pollo (kg)", 45, 3.20),
        Producto("PO003", "Pollo Entero (kg)", 40, 3.00),
        Producto("PO004", "Alitas de Pollo (kg)", 35, 3.50),
        Producto("PO005", "Pata de Muslo (kg)", 40, 2.80),

        # Huevos
        Producto("HO001", "Huevos de Campo (docena)", 100, 2.50),
        Producto("HO002", "Huevos Orgánicos (docena)", 50, 3.75),
        Producto("HO003", "Huevos Extra Grandes (docena)", 80, 3.20),
        Producto("HO004", "Huevos de Granja (docena)", 120, 2.80),

        # Quesos
        Producto("QU001", "Queso Fresco (kg)", 30, 4.50),
        Producto("QU002", "Queso Mozzarella (kg)", 25, 6.80),
        Producto("QU003", "Queso Crema (kg)", 20, 7.50),
        Producto("QU004", "Queso de Cabra (kg)", 15, 8.00),
        Producto("QU005", "Queso Parmesano (kg)", 10, 9.50),
        Producto("QU006", "Queso Provolone (kg)", 15, 7.80),

        # Embutidos
        Producto("EM001", "Salchicha Tipo Viena (kg)", 40, 5.50),
        Producto("EM002", "Mortadela (kg)", 35, 4.80),
        Producto("EM003", "Jamón Cocido (kg)", 30, 6.00),
        Producto("EM004", "Chorizo Español (kg)", 25, 7.20),
        Producto("EM005", "Salchichón (kg)", 20, 6.50),

        # Otros
        Producto("OT001", "Mantequilla (kg)", 40, 5.80),
        Producto("OT002", "Yogur Natural (litro)", 50, 2.20),
        Producto("OT003", "Leche Fresca (litro)", 60, 1.80)
    ]

    for producto in productos_iniciales:
        inventario.añadir_producto(producto)


def menu():
    inventario = Inventario()

    # Intentar cargar inventario desde archivo
    if not inventario.cargar_desde_json():
        precargar_productos(inventario)
        print("\n¡Bienvenido Cristian Chiquimba!")
        print("Se ha inicializado tu inventario con productos predeterminados.")

    while True:
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
        print("Carnicería: Sabores Andinos")
        print("Dueño: Cristian Chiquimba")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo")
        print("7. Cargar inventario desde archivo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Añadir producto
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio (USD): "))
                producto = Producto(id, nombre, cantidad, precio)
                if inventario.añadir_producto(producto):
                    print("Producto añadido exitosamente.")
            except ValueError:
                print("Error: Cantidad y precio deben ser números.")

        elif opcion == "2":  # Eliminar producto
            id = input("ID del producto a eliminar: ")
            if inventario.eliminar_producto(id):
                print("Producto eliminado exitosamente.")

        elif opcion == "3":  # Actualizar producto
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")

            try:
                cant = int(cantidad) if cantidad else None
                prec = float(precio) if precio else None
                if inventario.actualizar_producto(id, cant, prec):
                    print("Producto actualizado exitosamente.")
            except ValueError:
                print("Error: Los valores deben ser números.")

        elif opcion == "4":  # Buscar producto
            nombre = input("Nombre o parte del nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("\n=== RESULTADOS DE BÚSQUEDA ===")
                for producto in resultados:
                    print(
                        f"ID: {producto.id} | Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | Precio: ${producto.precio:.2f}")
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":  # Mostrar todos los productos
            inventario.mostrar_todos()

        elif opcion == "6":  # Guardar inventario
            nombre_archivo = input("Nombre del archivo (por defecto 'inventario.json'): ") or "inventario.json"
            inventario.guardar_a_json(nombre_archivo)

        elif opcion == "7":  # Cargar inventario
            nombre_archivo = input("Nombre del archivo (por defecto 'inventario.json'): ") or "inventario.json"
            inventario.cargar_desde_json(nombre_archivo)

        elif opcion == "8":  # Salir
            if input("¿Desea guardar el inventario antes de salir? (s/n): ").lower() == 's':
                inventario.guardar_a_json()
            print(f"\n¡Gracias por usar el sistema, Cristian Chiquimba!")
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()