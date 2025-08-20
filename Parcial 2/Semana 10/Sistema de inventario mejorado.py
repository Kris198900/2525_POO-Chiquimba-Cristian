# sistema_inventario_json.py
# Autor: Cristian Chiquimba
# Descripción: Sistema de inventario usando JSON con productos iniciales

import json
import os

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()
        if not self.productos:
            self.productos_iniciales()

    def productos_iniciales(self):
        """Crea productos iniciales si el inventario está vacío"""
        iniciales = {
            "jabon": {"precio": 1.50, "cantidad": 20},
            "gel": {"precio": 0.55, "cantidad": 15},
            "shampoo": {"precio": 2.00, "cantidad": 25},
            "detergente": {"precio": 0.75, "cantidad": 18},
            "rasuradora": {"precio": 2.00, "cantidad": 12},
            "crema de peinar": {"precio": 1.50, "cantidad": 10},
            "cotonetes": {"precio": 0.55, "cantidad": 30},
            "papel higienico": {"precio": 0.45, "cantidad": 40},
            "paños humedos": {"precio": 1.00, "cantidad": 22}
        }
        self.productos.update(iniciales)
        self.guardar_inventario()
        print("✅ Inventario inicial cargado.")

    def cargar_inventario(self):
        """Carga productos desde JSON"""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r", encoding="utf-8") as f:
                    self.productos = json.load(f)
            else:
                self.productos = {}
                self.guardar_inventario()
        except (json.JSONDecodeError, FileNotFoundError):
            print("⚠ Error en archivo. Se creará inventario nuevo.")
            self.productos = {}
            self.guardar_inventario()
        except PermissionError:
            print("❌ No tienes permisos para leer el archivo.")

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.productos, f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("❌ No tienes permisos para escribir en el archivo.")

    def agregar_producto(self, nombre, precio, cantidad):
        nombre = nombre.lower()
        self.productos[nombre] = {"precio": precio, "cantidad": cantidad}
        self.guardar_inventario()
        print(f"✅ Producto '{nombre}' agregado correctamente.")

    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        nombre = nombre.lower()
        if nombre in self.productos:
            if precio is not None:
                self.productos[nombre]["precio"] = precio
            if cantidad is not None:
                self.productos[nombre]["cantidad"] = cantidad
            self.guardar_inventario()
            print(f"✅ Producto '{nombre}' actualizado.")
        else:
            print(f"⚠ Producto '{nombre}' no existe.")

    def eliminar_producto(self, nombre):
        nombre = nombre.lower()
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar_inventario()
            print(f"🗑 Producto '{nombre}' eliminado.")
        else:
            print(f"⚠ Producto '{nombre}' no existe.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario actual:")
            for nombre, datos in self.productos.items():
                print(f"- {nombre}: precio ${datos['precio']}, cantidad {datos['cantidad']}")


# =========================
# PROGRAMA PRINCIPAL
# =========================
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            inventario.mostrar_inventario()
        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            inventario.agregar_producto(nombre, precio, cantidad)
        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            precio = input("Nuevo precio (dejar vacío si no cambia): ")
            cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
            inventario.actualizar_producto(
                nombre,
                float(precio) if precio else None,
                int(cantidad) if cantidad else None
            )
        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠ Opción no válida, intenta de nuevo.")
