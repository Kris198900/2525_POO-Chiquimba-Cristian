# sistema_inventario_aseo.py
# Autor: Cristian David Chiquimba Mena
# Descripción: Sistema de Gestión de Inventarios para productos de aseo personal
# Almacena y recupera datos desde archivo, maneja excepciones y proporciona interfaz de usuario en consola

import os

class Producto:
    """Representa un producto de aseo personal"""
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        """Formato para guardar en archivo"""
        return f"{self.nombre},{self.categoria},{self.precio},{self.cantidad}"


class Inventario:
    """Maneja el inventario de productos con almacenamiento en archivo"""
    def __init__(self, archivo="inventario_aseo.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Carga productos desde el archivo si existe, crea archivo si no"""
        if not os.path.exists(self.archivo):
            try:
                with open(self.archivo, "w") as f:
                    pass
            except PermissionError:
                print("Error: No se puede crear el archivo de inventario (permiso denegado).")
                return

        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        partes = linea.split(",")
                        if len(partes) == 4:
                            nombre, categoria, precio, cantidad = partes
                            producto = Producto(nombre, categoria, float(precio), int(cantidad))
                            self.productos.append(producto)
                        else:
                            print(f"Advertencia: Línea inválida en archivo: {linea}")
        except Exception as e:
            print(f"Error al leer el archivo de inventario: {e}")

    def guardar_en_archivo(self):
        """Guarda todos los productos en el archivo"""
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos:
                    f.write(str(producto) + "\n")
        except Exception as e:
            print(f"Error al guardar el archivo de inventario: {e}")

    def agregar_producto(self, producto):
        """Agrega un producto al inventario"""
        self.productos.append(producto)
        self.guardar_en_archivo()
        print(f"Producto '{producto.nombre}' agregado correctamente.")

    def actualizar_producto(self, nombre, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o precio de un producto existente"""
        encontrado = False
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                encontrado = True
                break
        if encontrado:
            self.guardar_en_archivo()
            print(f"Producto '{nombre}' actualizado correctamente.")
        else:
            print(f"Producto '{nombre}' no encontrado.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario"""
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print(f"Producto '{nombre}' eliminado correctamente.")
                return
        print(f"Producto '{nombre}' no encontrado.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario"""
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("\nInventario de Aseo Personal:")
        print(f"{'Nombre':<20}{'Categoría':<15}{'Precio ($)':<12}{'Cantidad':<10}")
        print("-"*60)
        for p in self.productos:
            print(f"{p.nombre:<20}{p.categoria:<15}{p.precio:<12}{p.cantidad:<10}")
        print("-"*60)


# ------------------------------
# Interfaz de consola
# ------------------------------
def main():
    inventario = Inventario()

    # Productos de ejemplo iniciales (aseo personal)
    if not inventario.productos:  # Solo si el archivo estaba vacío
        productos_iniciales = [
            Producto("Jabón Líquido", "Jabón", 2.5, 20),
            Producto("Shampoo", "Cabello", 5.0, 15),
            Producto("Pasta Dental", "Dental", 3.0, 30),
            Producto("Cepillo de Dientes", "Dental", 1.5, 25),
            Producto("Desodorante", "Higiene", 4.0, 10),
        ]
        for p in productos_iniciales:
            inventario.agregar_producto(p)

    while True:
        print("\n--- Sistema de Inventario de Aseo Personal ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            categoria = input("Categoría: ")
            try:
                precio = float(input("Precio ($): "))
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Error: Precio debe ser un número y cantidad un entero.")
                continue
            producto = Producto(nombre, categoria, precio, cantidad)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            try:
                nueva_cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = input("Nuevo precio (dejar vacío si no cambia): ")
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            except ValueError:
                print("Error: Precio debe ser un número y cantidad un entero.")
                continue
            inventario.actualizar_producto(nombre, nueva_cantidad, nuevo_precio)

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            print("Saliendo del sistema... ¡Gracias por usarlo!")
            break

        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    main()
