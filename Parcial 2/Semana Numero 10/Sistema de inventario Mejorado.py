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
        """Carga productos desde archivo JSON"""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r", encoding="utf-8") as f:
                    contenido = f.read().strip()
                    if contenido:  # Verificar que el archivo no esté vacío
                        self.productos = json.loads(contenido)
                        print(f"✅ Inventario cargado desde {self.archivo}")
                    else:
                        self.productos = {}
                        print("📝 Archivo vacío, se inicializará inventario nuevo.")
            else:
                self.productos = {}
                print(f"📁 Archivo {self.archivo} no existe, se creará uno nuevo.")
                self.guardar_inventario()
        except json.JSONDecodeError as e:
            print(f"⚠ Error al leer JSON: {e}. Se creará inventario nuevo.")
            self.productos = {}
            self.guardar_inventario()
        except FileNotFoundError:
            print(f"⚠ Archivo {self.archivo} no encontrado. Se creará uno nuevo.")
            self.productos = {}
            self.guardar_inventario()
        except PermissionError:
            print(f"❌ No tienes permisos para leer el archivo {self.archivo}.")
            self.productos = {}
        except Exception as e:
            print(f"❌ Error inesperado al cargar inventario: {e}")
            self.productos = {}

    def guardar_inventario(self):
        """Guarda el inventario actual en archivo JSON"""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump(self.productos, f, indent=4, ensure_ascii=False)
            print(f"💾 Inventario guardado en {self.archivo}")
        except PermissionError:
            print(f"❌ No tienes permisos para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"❌ Error inesperado al guardar inventario: {e}")

    def agregar_producto(self, nombre, precio, cantidad):
        """Agrega un nuevo producto al inventario"""
        try:
            nombre = nombre.strip().lower()
            if not nombre:
                print("⚠ El nombre del producto no puede estar vacío.")
                return

            if precio <= 0:
                print("⚠ El precio debe ser mayor que 0.")
                return

            if cantidad < 0:
                print("⚠ La cantidad no puede ser negativa.")
                return

            self.productos[nombre] = {"precio": precio, "cantidad": cantidad}
            self.guardar_inventario()
            print(f"✅ Producto '{nombre}' agregado correctamente.")
        except Exception as e:
            print(f"❌ Error al agregar producto: {e}")

    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        """Actualiza precio y/o cantidad de un producto existente"""
        try:
            nombre = nombre.strip().lower()
            if nombre in self.productos:
                if precio is not None:
                    if precio <= 0:
                        print("⚠ El precio debe ser mayor que 0.")
                        return
                    self.productos[nombre]["precio"] = precio
                if cantidad is not None:
                    if cantidad < 0:
                        print("⚠ La cantidad no puede ser negativa.")
                        return
                    self.productos[nombre]["cantidad"] = cantidad
                self.guardar_inventario()
                print(f"✅ Producto '{nombre}' actualizado.")
            else:
                print(f"⚠ Producto '{nombre}' no existe en el inventario.")
        except Exception as e:
            print(f"❌ Error al actualizar producto: {e}")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario"""
        try:
            nombre = nombre.strip().lower()
            if nombre in self.productos:
                del self.productos[nombre]
                self.guardar_inventario()
                print(f"🗑 Producto '{nombre}' eliminado del inventario.")
            else:
                print(f"⚠ Producto '{nombre}' no existe en el inventario.")
        except Exception as e:
            print(f"❌ Error al eliminar producto: {e}")

    def mostrar_inventario(self):
        """Muestra todos los productos del inventario"""
        try:
            if not self.productos:
                print("📦 El inventario está vacío.")
            else:
                print(f"\n📋 Inventario actual ({len(self.productos)} productos):")
                print("-" * 50)
                total_productos = 0
                valor_total = 0

                for nombre, datos in sorted(self.productos.items()):
                    precio = datos['precio']
                    cantidad = datos['cantidad']
                    valor_producto = precio * cantidad
                    total_productos += cantidad
                    valor_total += valor_producto

                    print(
                        f"• {nombre.title():<20} | Precio: ${precio:>6.2f} | Cantidad: {cantidad:>3} | Valor: ${valor_producto:>7.2f}")

                print("-" * 50)
                print(f"Total productos: {total_productos} | Valor total del inventario: ${valor_total:.2f}")
        except Exception as e:
            print(f"❌ Error al mostrar inventario: {e}")

    def buscar_producto(self, nombre):
        """Busca un producto específico en el inventario"""
        try:
            nombre = nombre.strip().lower()
            if nombre in self.productos:
                datos = self.productos[nombre]
                print(f"\n🔍 Producto encontrado:")
                print(f"Nombre: {nombre.title()}")
                print(f"Precio: ${datos['precio']:.2f}")
                print(f"Cantidad: {datos['cantidad']}")
                print(f"Valor total: ${datos['precio'] * datos['cantidad']:.2f}")
            else:
                print(f"⚠ Producto '{nombre}' no encontrado en el inventario.")
        except Exception as e:
            print(f"❌ Error al buscar producto: {e}")


def obtener_numero(mensaje, tipo=float, minimo=None):
    """Función auxiliar para obtener números con validación"""
    while True:
        try:
            valor = input(mensaje)
            if valor.strip() == "":
                return None
            numero = tipo(valor)
            if minimo is not None and numero < minimo:
                print(f"⚠ El valor debe ser mayor o igual a {minimo}")
                continue
            return numero
        except ValueError:
            print(f"⚠ Por favor ingresa un {'número entero' if tipo == int else 'número'} válido.")


# =========================
# PROGRAMA PRINCIPAL
# =========================
if __name__ == "__main__":
    print("🏪 Sistema de Gestión de Inventarios")
    print("=" * 40)

    try:
        inventario = Inventario()

        while True:
            print("\n--- MENÚ DE INVENTARIO ---")
            print("1. Mostrar inventario completo")
            print("2. Agregar nuevo producto")
            print("3. Actualizar producto existente")
            print("4. Buscar producto")
            print("5. Eliminar producto")
            print("6. Salir del sistema")
            print("-" * 30)

            opcion = input("Elige una opción (1-6): ").strip()

            if opcion == "1":
                inventario.mostrar_inventario()

            elif opcion == "2":
                print("\n--- AGREGAR PRODUCTO ---")
                nombre = input("Nombre del producto: ").strip()
                if not nombre:
                    print("⚠ El nombre no puede estar vacío.")
                    continue

                precio = obtener_numero("Precio del producto: $", float, 0.01)
                if precio is None:
                    print("⚠ El precio es obligatorio.")
                    continue

                cantidad = obtener_numero("Cantidad en stock: ", int, 0)
                if cantidad is None:
                    print("⚠ La cantidad es obligatoria.")
                    continue

                inventario.agregar_producto(nombre, precio, cantidad)

            elif opcion == "3":
                print("\n--- ACTUALIZAR PRODUCTO ---")
                nombre = input("Nombre del producto a actualizar: ").strip()
                if not nombre:
                    print("⚠ El nombre no puede estar vacío.")
                    continue

                print("(Dejar vacío para no cambiar)")
                precio = obtener_numero("Nuevo precio: $", float, 0.01)
                cantidad = obtener_numero("Nueva cantidad: ", int, 0)

                if precio is None and cantidad is None:
                    print("⚠ Debes especificar al menos un valor para actualizar.")
                    continue

                inventario.actualizar_producto(nombre, precio, cantidad)

            elif opcion == "4":
                print("\n--- BUSCAR PRODUCTO ---")
                nombre = input("Nombre del producto a buscar: ").strip()
                if not nombre:
                    print("⚠ El nombre no puede estar vacío.")
                    continue
                inventario.buscar_producto(nombre)

            elif opcion == "5":
                print("\n--- ELIMINAR PRODUCTO ---")
                nombre = input("Nombre del producto a eliminar: ").strip()
                if not nombre:
                    print("⚠ El nombre no puede estar vacío.")
                    continue

                confirmacion = input(f"¿Estás seguro de eliminar '{nombre}'? (s/n): ").strip().lower()
                if confirmacion == 's' or confirmacion == 'si':
                    inventario.eliminar_producto(nombre)
                else:
                    print("❌ Eliminación cancelada.")

            elif opcion == "6":
                print("👋 Gracias por usar el sistema de inventarios. ¡Hasta luego!")
                break

            else:
                print("⚠ Opción no válida. Por favor elige una opción del 1 al 6.")

    except KeyboardInterrupt:
        print("\n\n👋 Sistema interrumpido por el usuario. ¡Hasta luego!")
    except Exception as e:
        print(f"\n❌ Error crítico en el sistema: {e}")
        print("El programa se cerrará.")