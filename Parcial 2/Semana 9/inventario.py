# inventario.py
# Autor: Cristian Chiquimba Mena

from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        # Verificar que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("⚠️ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("🗑 Producto eliminado correctamente.")
                return
        print("⚠️ Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("🔄 Producto actualizado correctamente.")
                return
        print("⚠️ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos(self):
        print("\n📦 LISTA DE PRODUCTOS EN INVENTARIO 📦")
        if not self.productos:
            print("Inventario vacío.")
        for p in self.productos:
            print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}")
