import json
import os


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Inicializa un producto con sus atributos básicos.

        Args:
            id (str): Identificador único del producto
            nombre (str): Nombre del producto
            cantidad (int): Cantidad disponible en inventario
            precio (float): Precio unitario en dólares americanos (USD)
        """
        self.__id = id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        """Representación en cadena del producto"""
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"

    def to_dict(self):
        """Convierte el producto a un diccionario para serialización JSON"""
        return {
            'id': self.__id,
            'nombre': self.__nombre,
            'cantidad': self.__cantidad,
            'precio': self.__precio
        }


class Inventario:
    def __init__(self):
        """Inicializa el inventario con un diccionario vacío para almacenar productos."""
        self.__productos = {}  # Diccionario para acceso rápido por ID

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.

        Args:
            producto (Producto): Objeto producto a añadir
        """
        if producto.get_id() in self.__productos:
            print(f"Error: Ya existe un producto con ID {producto.get_id()}")
            return False
        self.__productos[producto.get_id()] = producto
        return True

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.

        Args:
            id (str): ID del producto a eliminar
        """
        if id in self.__productos:
            del self.__productos[id]
            return True
        print(f"Error: No existe un producto con ID {id}")
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o precio de un producto.

        Args:
            id (str): ID del producto a actualizar
            cantidad (int, optional): Nueva cantidad
            precio (float, optional): Nuevo precio
        """
        if id not in self.__productos:
            print(f"Error: No existe un producto con ID {id}")
            return False

        if cantidad is not None:
            self.__productos[id].set_cantidad(cantidad)
        if precio is not None:
            self.__productos[id].set_precio(precio)
        return True

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre (búsqueda parcial, insensible a mayúsculas).

        Args:
            nombre (str): Nombre o parte del nombre a buscar

        Returns:
            list: Lista de productos que coinciden con la búsqueda
        """
        nombre = nombre.lower()
        resultados = []
        for producto in self.__productos.values():
            if nombre in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos(self):
        """Muestra todos los productos en el inventario."""
        if not self.__productos:
            print("El inventario está vacío.")
            return

        print("\n=== INVENTARIO COMPLETO ===")
        print(f"{'ID':<5} {'Nombre':<25} {'Cantidad':<10} {'Precio':<10}")
        print("-" * 55)
        for producto in self.__productos.values():
            print(
                f"{producto.get_id():<5} {producto.get_nombre():<25} {producto.get_cantidad():<10} ${producto.get_precio():<9.2f}")

    def guardar_a_json(self, nombre_archivo="inventario.json"):
        """
        Guarda el inventario en un archivo JSON.

        Args:
            nombre_archivo (str): Nombre del archivo a guardar
        """
        datos = {
            'carniceria': 'Sabores Andinos',
            'dueño': 'Cristian Chiquimba',
            'productos': [producto.to_dict() for producto in self.__productos.values()]
        }

        try:
            with open(nombre_archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
            print(f"Inventario guardado en {nombre_archivo}")
            return True
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")
            return False

    def cargar_desde_json(self, nombre_archivo="inventario.json"):
        """
        Carga el inventario desde un archivo JSON.

        Args:
            nombre_archivo (str): Nombre del archivo a cargar
        """
        if not os.path.exists(nombre_archivo):
            return False

        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as f:
                datos = json.load(f)

            self.__productos = {}
            for item in datos['productos']:
                producto = Producto(
                    item['id'],
                    item['nombre'],
                    item['cantidad'],
                    item['precio']
                )
                self.__productos[producto.get_id()] = producto

            print(f"Inventario cargado desde {nombre_archivo}")
            print(f"Carnicería: {datos.get('carniceria', 'Desconocida')}")
            print(f"Dueño: {datos.get('dueño', 'Desconocido')}")
            return True
        except json.JSONDecodeError:
            print(f"Error: El archivo {nombre_archivo} no tiene un formato JSON válido.")
            return False
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
            return False


def precargar_productos(inventario):
    """Precarga productos iniciales con precios reales de Ecuador."""
    productos_iniciales = [
        Producto("CR001", "Carne de Res (kg)", 50, 5.50),
        Producto("CR002", "Carne de Cerdo (kg)", 30, 4.20),
        Producto("PO001", "Pechuga de Pollo (kg)", 40, 3.80),
        Producto("PO002", "Muslo de Pollo (kg)", 35, 3.20),
        Producto("HO001", "Huevos de Campo (docena)", 100, 2.50),
        Producto("HO002", "Huevos Orgánicos (docena)", 50, 3.75),
        Producto("QU001", "Queso Fresco (kg)", 25, 4.50),
        Producto("QU002", "Queso Mozzarella (kg)", 20, 6.80)
    ]

    for producto in productos_iniciales:
        inventario.añadir_producto(producto)


def menu():
    """Función principal que muestra el menú interactivo al usuario."""
    inventario = Inventario()

    # Intentar cargar inventario desde archivo, si no existe, precargar productos iniciales
    if not inventario.cargar_desde_json():
        precargar_productos(inventario)
        print("\n¡Bienvenido Cristian Chiquimba!")
        print("Se ha inicializado tu inventario con productos predeterminados.")

    while True:
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO - CARNICERÍA SABORES ANDINOS ===")
        print("Dueño: Cristian Chiquimba")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario en archivo JSON")
        print("7. Cargar inventario desde archivo JSON")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
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

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            if inventario.eliminar_producto(id):
                print("Producto eliminado exitosamente.")

        elif opcion == "3":
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

        elif opcion == "4":
            nombre = input("Nombre o parte del nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("\n=== RESULTADOS DE BÚSQUEDA ===")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            nombre_archivo = input("Nombre del archivo JSON (por defecto 'inventario.json'): ") or "inventario.json"
            inventario.guardar_a_json(nombre_archivo)

        elif opcion == "7":
            nombre_archivo = input("Nombre del archivo JSON (por defecto 'inventario.json'): ") or "inventario.json"
            inventario.cargar_desde_json(nombre_archivo)

        elif opcion == "8":
            # Guardar inventario antes de salir
            if input("¿Desea guardar el inventario antes de salir? (s/n): ").lower() == 's':
                inventario.guardar_a_json()
            print(f"\n¡Gracias por usar el sistema, Cristian Chiquimba!")
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()