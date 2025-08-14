import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Semana 2/1.1 Sistema de gestion de liga de futbol.py',
        '2': 'Semana 3/1.2.2 Programación  (POO).py',
        '3': 'Semana 3/1.2 Programación Tradicional.py',
        '4': 'semana 4/1.3 Ejemplos MundoReal_POO.py',
        '5': 'Semana 5/1.4 Tipos de Datos Identificadores.py',
        '6': 'Semana 6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '7': 'Semana 7/1.7 Implementación De Constructores y Destructores en Python.py'
    }

    while True:
        print("\n" + "=" * 60)
        print("        DASHBOARD - MENÚ PRINCIPAL")
        print("=" * 60)
        print("Selecciona el script que deseas visualizar:")
        print("")

        # Imprime las opciones del menú
        for key in opciones:
            nombre_archivo = os.path.basename(opciones[key])
            print(f"  [{key}] {nombre_archivo}")

        print(f"  [0] Salir del programa")
        print("=" * 60)

        eleccion = input("Elige una opción: ")

        if eleccion == '0':
            print("¡Gracias por usar el dashboard!")
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)

            # Pausa para que el usuario pueda leer el código
            input("\nPresiona Enter para volver al menú principal...")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()