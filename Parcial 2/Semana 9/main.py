# main.py
# Autor: Cristian Chiquimba Mena

from inventario import Inventario
from producto import Producto

# Crear inventario y añadir productos iniciales con tus precios y cantidades
inventario = Inventario()
inventario.agregar_producto(Producto("P1", "Mochila", 15, 12.00))
inventario.agregar_producto(Producto("P2", "Cartuchera", 20, 5.75))
inventario.agregar_producto(Producto("P3", "Canguro", 18, 6.00))
inventario.agregar_producto(Producto("P4", "Maleta de viaje", 10, 15.00))
inventario.agregar_producto(Producto("P5", "Monedero", 25, 2.00))
inventario.agregar_producto(Producto("P6", "Zapatos", 12, 35.00))

while True:
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("Creado por: Cristian Chiquimba Mena")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id = input("ID: ")
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        inventario.agregar_producto(Producto(id, nombre, cantidad, precio))

    elif opcion == "2":
        id = input("ID del producto a eliminar: ")
        inventario.eliminar_producto(id)

    elif opcion == "3":
        id = input("ID del producto a actualizar: ")
        cantidad = input("Nueva cantidad (dejar vacío si no cambia): ")
        precio = input("Nuevo precio (dejar vacío si no cambia): ")
        inventario.actualizar_producto(
            id,
            int(cantidad) if cantidad else None,
            float(precio) if precio else None
        )

    elif opcion == "4":
        nombre = input("Nombre a buscar: ")
        resultados = inventario.buscar_por_nombre(nombre)
        if resultados:
            print("\n🔍 Resultados de búsqueda:")
            for p in resultados:
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}")
        else:
            print("⚠️ No se encontraron productos con ese nombre.")

    elif opcion == "5":
        inventario.mostrar_todos()

    elif opcion == "6":
        print("👋 Saliendo del sistema...")
        break

    else:
        print("❌ Opción inválida, intente nuevamente.")
