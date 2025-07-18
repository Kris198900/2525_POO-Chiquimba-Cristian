import os
import datetime
import subprocess
import sys


class DashboardPersonalizado:
    def __init__(self):
        self.ruta_base = os.path.dirname(__file__)
        self.historial_visualizados = []
        self.opciones = {
            '1': 'Semana 2/1.1 Sistema de gestion de liga de futbol.py',
            '2': 'Semana 3/1.2.2 Programación  (POO).py',
            '3': 'Semana 3/1.2 Programación Tradicional.py',
            '4': 'semana 4/1.3 Ejemplos MundoReal_POO.py',
            '5': 'Semana 5/1.4 Tipos de Datos Identificadores.py',
            '6': 'Semana 6/Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
            '7': 'Semana 7/1.7 Implementación De Constructores y Destructores en Python.py'
        }

    def mostrar_banner(self):
        """Muestra el banner personalizado del dashboard"""
        print("\n" + "=" * 70)
        print("🐍 DASHBOARD DE GESTIÓN DE PROYECTOS PYTHON 🐍")
        print("=" * 70)
        print("📚 Curso: Programación Orientada a Objetos")
        print("👨‍💻 Estudiante: [Tu Nombre]")
        print("📅 Fecha:", datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S"))
        print("=" * 70)

    def mostrar_codigo(self, ruta_script):
        """Muestra el código del script seleccionado"""
        ruta_script_absoluta = os.path.abspath(ruta_script)
        try:
            with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()

                # Agregar al historial
                nombre_archivo = os.path.basename(ruta_script)
                self.historial_visualizados.append({
                    'archivo': nombre_archivo,
                    'fecha': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    'ruta': ruta_script
                })

                print(f"\n{'=' * 60}")
                print(f"📄 CÓDIGO: {nombre_archivo}")
                print(f"📁 RUTA: {ruta_script}")
                print(f"📏 LÍNEAS: {len(contenido.splitlines())}")
                print(f"{'=' * 60}")
                print(contenido)
                print(f"{'=' * 60}")

        except FileNotFoundError:
            print("❌ Error: El archivo no se encontró.")
        except Exception as e:
            print(f"❌ Error al leer el archivo: {e}")

    def ejecutar_script(self, ruta_script):
        """Ejecuta el script seleccionado"""
        ruta_script_absoluta = os.path.abspath(ruta_script)
        try:
            print(f"\n🚀 Ejecutando: {os.path.basename(ruta_script)}")
            print("-" * 50)
            subprocess.run([sys.executable, ruta_script_absoluta], check=True)
            print("-" * 50)
            print("✅ Ejecución completada exitosamente")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al ejecutar el script: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    def mostrar_estadisticas(self):
        """Muestra estadísticas del proyecto"""
        print(f"\n{'=' * 60}")
        print("📊 ESTADÍSTICAS DEL PROYECTO")
        print(f"{'=' * 60}")
        print(f"📁 Total de scripts disponibles: {len(self.opciones)}")
        print(f"👀 Scripts visualizados en esta sesión: {len(self.historial_visualizados)}")

        # Contar líneas de código total
        total_lineas = 0
        for opcion in self.opciones.values():
            ruta_completa = os.path.join(self.ruta_base, opcion)
            try:
                with open(ruta_completa, 'r', encoding='utf-8') as archivo:
                    total_lineas += len(archivo.readlines())
            except:
                pass

        print(f"📏 Total de líneas de código: {total_lineas}")
        print(f"💻 Ruta del proyecto: {self.ruta_base}")
        print(f"{'=' * 60}")

    def mostrar_historial(self):
        """Muestra el historial de archivos visualizados"""
        if not self.historial_visualizados:
            print("\n📋 No hay archivos visualizados en esta sesión.")
            return

        print(f"\n{'=' * 60}")
        print("📋 HISTORIAL DE ARCHIVOS VISUALIZADOS")
        print(f"{'=' * 60}")
        for i, item in enumerate(self.historial_visualizados, 1):
            print(f"{i}. {item['archivo']}")
            print(f"   🕒 {item['fecha']}")
            print(f"   📁 {item['ruta']}")
            print()

    def buscar_scripts(self):
        """Busca scripts por palabra clave"""
        print(f"\n{'=' * 60}")
        print("🔍 BÚSQUEDA DE SCRIPTS")
        print(f"{'=' * 60}")
        termino = input("Ingresa una palabra clave para buscar: ").lower()

        resultados = []
        for key, ruta in self.opciones.items():
            nombre_archivo = os.path.basename(ruta).lower()
            if termino in nombre_archivo:
                resultados.append((key, ruta))

        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} resultado(s):")
            for key, ruta in resultados:
                print(f"  [{key}] {os.path.basename(ruta)}")
        else:
            print("❌ No se encontraron resultados.")

    def mostrar_menu_principal(self):
        """Muestra el menú principal con todas las opciones"""
        print(f"\n{'=' * 60}")
        print("🎯 MENÚ PRINCIPAL")
        print(f"{'=' * 60}")
        print("📚 SCRIPTS DISPONIBLES:")

        # Agrupar por semanas
        semanas = {}
        for key, ruta in self.opciones.items():
            semana = ruta.split('/')[0]
            if semana not in semanas:
                semanas[semana] = []
            semanas[semana].append((key, os.path.basename(ruta)))

        for semana, archivos in semanas.items():
            print(f"\n📅 {semana.upper()}:")
            for key, nombre in archivos:
                print(f"  [{key}] {nombre}")

        print(f"\n🔧 OPCIONES ADICIONALES:")
        print(f"  [H] Ver historial")
        print(f"  [E] Mostrar estadísticas")
        print(f"  [B] Buscar scripts")
        print(f"  [0] Salir")
        print(f"{'=' * 60}")

    def procesar_opcion(self, eleccion):
        """Procesa la opción seleccionada por el usuario"""
        if eleccion == '0':
            print("\n🎉 ¡Gracias por usar el Dashboard Personalizado!")
            print("💡 Tip: Recuerda hacer commit de tus cambios regularmente.")
            return False

        elif eleccion.upper() == 'H':
            self.mostrar_historial()

        elif eleccion.upper() == 'E':
            self.mostrar_estadisticas()

        elif eleccion.upper() == 'B':
            self.buscar_scripts()

        elif eleccion in self.opciones:
            ruta_script = os.path.join(self.ruta_base, self.opciones[eleccion])

            print(f"\n🎯 Opciones para {os.path.basename(self.opciones[eleccion])}:")
            print("  [1] Ver código")
            print("  [2] Ejecutar script")
            print("  [3] Ver código y ejecutar")

            sub_eleccion = input("Selecciona una opción: ")

            if sub_eleccion == '1':
                self.mostrar_codigo(ruta_script)
            elif sub_eleccion == '2':
                self.ejecutar_script(ruta_script)
            elif sub_eleccion == '3':
                self.mostrar_codigo(ruta_script)
                input("\nPresiona Enter para ejecutar el script...")
                self.ejecutar_script(ruta_script)
            else:
                print("❌ Opción no válida.")

        else:
            print("❌ Opción no válida. Por favor, intenta de nuevo.")

        return True

    def ejecutar_dashboard(self):
        """Método principal que ejecuta el dashboard"""
        while True:
            self.mostrar_banner()
            self.mostrar_menu_principal()

            eleccion = input("🎯 Selecciona una opción: ")

            if not self.procesar_opcion(eleccion):
                break

            input("\n⏎ Presiona Enter para continuar...")


def main():
    """Función principal del programa"""
    dashboard = DashboardPersonalizado()
    dashboard.ejecutar_dashboard()


# Ejecutar el dashboard
if __name__ == "__main__":
    main()