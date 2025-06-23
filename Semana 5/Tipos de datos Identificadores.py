"""
Sistema de Gestión de Biblioteca Personal
========================================
Este programa permite gestionar una biblioteca personal, donde se pueden
agregar libros, buscar por título o autor, mostrar todos los libros,
y calcular estadísticas básicas de la colección.

Autor: Cristian David Chiquimba Mena
Fecha: 23 de Junio 2025
Materia: Programación Orientada a Objetos
"""


def agregar_libro(biblioteca, titulo, autor, paginas, leido):
    """
    Agrega un nuevo libro a la biblioteca

    Args:
        biblioteca (list): Lista de libros
        titulo (str): Título del libro
        autor (str): Autor del libro
        paginas (int): Número de páginas
        leido (bool): Estado de lectura del libro
    """
    # Crear diccionario con información del libro
    nuevo_libro = {
        'titulo': titulo,
        'autor': autor,
        'paginas': paginas,
        'leido': leido,
        'id_libro': len(biblioteca) + 1
    }

    biblioteca.append(nuevo_libro)
    print(f"✓ Libro '{titulo}' agregado exitosamente a la biblioteca.")


def mostrar_todos_libros(biblioteca):
    """
    Muestra todos los libros en la biblioteca

    Args:
        biblioteca (list): Lista de libros
    """
    if not biblioteca:
        print("📚 La biblioteca está vacía.")
        return

    print("\n📚 BIBLIOTECA PERSONAL - TODOS LOS LIBROS")
    print("=" * 60)

    for libro in biblioteca:
        estado_lectura = "✓ Leído" if libro['leido'] else "⏳ Pendiente"
        print(f"ID: {libro['id_libro']}")
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Páginas: {libro['paginas']}")
        print(f"Estado: {estado_lectura}")
        print("-" * 40)


def buscar_libro(biblioteca, termino_busqueda):
    """
    Busca libros por título o autor

    Args:
        biblioteca (list): Lista de libros
        termino_busqueda (str): Término a buscar

    Returns:
        list: Lista de libros encontrados
    """
    libros_encontrados = []
    termino_minuscula = termino_busqueda.lower()

    for libro in biblioteca:
        titulo_minuscula = libro['titulo'].lower()
        autor_minuscula = libro['autor'].lower()

        if termino_minuscula in titulo_minuscula or termino_minuscula in autor_minuscula:
            libros_encontrados.append(libro)

    return libros_encontrados


def calcular_estadisticas(biblioteca):
    """
    Calcula estadísticas de la biblioteca

    Args:
        biblioteca (list): Lista de libros

    Returns:
        dict: Diccionario con estadísticas
    """
    if not biblioteca:
        return None

    total_libros = len(biblioteca)
    libros_leidos = sum(1 for libro in biblioteca if libro['leido'])
    libros_pendientes = total_libros - libros_leidos
    total_paginas = sum(libro['paginas'] for libro in biblioteca)
    promedio_paginas = total_paginas / total_libros

    # Calcular porcentaje de libros leídos
    porcentaje_leidos = (libros_leidos / total_libros) * 100

    estadisticas = {
        'total_libros': total_libros,
        'libros_leidos': libros_leidos,
        'libros_pendientes': libros_pendientes,
        'total_paginas': total_paginas,
        'promedio_paginas': promedio_paginas,
        'porcentaje_leidos': porcentaje_leidos
    }

    return estadisticas


def mostrar_estadisticas(biblioteca):
    """
    Muestra las estadísticas de la biblioteca

    Args:
        biblioteca (list): Lista de libros
    """
    stats = calcular_estadisticas(biblioteca)

    if stats is None:
        print("📊 No hay estadísticas disponibles - La biblioteca está vacía.")
        return

    print("\n📊 ESTADÍSTICAS DE LA BIBLIOTECA")
    print("=" * 40)
    print(f"Total de libros: {stats['total_libros']}")
    print(f"Libros leídos: {stats['libros_leidos']}")
    print(f"Libros pendientes: {stats['libros_pendientes']}")
    print(f"Total de páginas: {stats['total_paginas']}")
    print(f"Promedio de páginas por libro: {stats['promedio_paginas']:.1f}")
    print(f"Porcentaje de libros leídos: {stats['porcentaje_leidos']:.1f}%")


def mostrar_menu():
    """
    Muestra el menú principal del programa
    """
    print("\n📚 SISTEMA DE GESTIÓN DE BIBLIOTECA PERSONAL")
    print("=" * 50)
    print("1. Agregar nuevo libro")
    print("2. Mostrar todos los libros")
    print("3. Buscar libro")
    print("4. Ver estadísticas")
    print("5. Salir del programa")
    print("=" * 50)


def obtener_opcion_valida():
    """
    Obtiene una opción válida del menú

    Returns:
        int: Opción seleccionada por el usuario
    """
    while True:
        try:
            opcion_usuario = int(input("Selecciona una opción (1-5): "))
            if 1 <= opcion_usuario <= 5:
                return opcion_usuario
            else:
                print("❌ Por favor, selecciona una opción válida (1-5).")
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")


def main():
    """
    Función principal que ejecuta el sistema de gestión de biblioteca
    """
    # Lista para almacenar todos los libros (estructura de datos principal)
    mi_biblioteca = []

    # Variable de control del programa principal
    programa_ejecutandose = True

    # Mensaje de bienvenida
    print("🎉 ¡Bienvenido a tu Sistema de Gestión de Biblioteca Personal!")
    print("Aquí podrás organizar y gestionar tu colección de libros.")

    # Agregar algunos libros de ejemplo para demostración
    libros_ejemplo = [
        ("Las fábulas de Esopo", "Esopo", 280, True),
        ("Las sombras de Grey", "E.L. James", 514, False),
        ("Cálculo diferencial", "Frank Ayres Jr.", 456, True),
        ("Álgebra de Baldor", "Aurelio Baldor", 736, False),
        ("La culpa es de la vaca", "Jaime Lopera", 192, True)
    ]

    print("\n📚 Agregando libros de ejemplo...")
    for titulo, autor, paginas, leido in libros_ejemplo:
        agregar_libro(mi_biblioteca, titulo, autor, paginas, leido)

    # Bucle principal del programa
    while programa_ejecutandose:
        mostrar_menu()
        opcion_seleccionada = obtener_opcion_valida()

        if opcion_seleccionada == 1:
            # Agregar nuevo libro
            print("\n📖 AGREGAR NUEVO LIBRO")
            print("-" * 25)

            try:
                titulo_nuevo = input("Título del libro: ").strip()
                autor_nuevo = input("Autor del libro: ").strip()
                paginas_nuevo = int(input("Número de páginas: "))

                # Validar que las páginas sean positivas
                if paginas_nuevo <= 0:
                    print("❌ El número de páginas debe ser positivo.")
                    continue

                # Preguntar si ya fue leído
                respuesta_leido = input("¿Ya leíste este libro? (s/n): ").lower().strip()
                libro_leido = respuesta_leido in ['s', 'si', 'sí', 'yes', 'y']

                # Validar que los campos no estén vacíos
                if not titulo_nuevo or not autor_nuevo:
                    print("❌ El título y autor no pueden estar vacíos.")
                    continue

                agregar_libro(mi_biblioteca, titulo_nuevo, autor_nuevo, paginas_nuevo, libro_leido)

            except ValueError:
                print("❌ Error: Ingresa un número válido para las páginas.")

        elif opcion_seleccionada == 2:
            # Mostrar todos los libros
            mostrar_todos_libros(mi_biblioteca)

        elif opcion_seleccionada == 3:
            # Buscar libro
            print("\n🔍 BUSCAR LIBRO")
            print("-" * 15)
            termino_busqueda = input("Ingresa el título o autor a buscar: ").strip()

            if termino_busqueda:
                resultados_busqueda = buscar_libro(mi_biblioteca, termino_busqueda)

                if resultados_busqueda:
                    print(f"\n🔍 RESULTADOS DE BÚSQUEDA PARA: '{termino_busqueda}'")
                    print("=" * 50)

                    for libro in resultados_busqueda:
                        estado_lectura = "✓ Leído" if libro['leido'] else "⏳ Pendiente"
                        print(f"• {libro['titulo']} - {libro['autor']}")
                        print(f"  Páginas: {libro['paginas']} | Estado: {estado_lectura}")
                        print("-" * 30)
                else:
                    print(f"❌ No se encontraron libros con el término: '{termino_busqueda}'")
            else:
                print("❌ Por favor, ingresa un término de búsqueda válido.")

        elif opcion_seleccionada == 4:
            # Ver estadísticas
            mostrar_estadisticas(mi_biblioteca)

        elif opcion_seleccionada == 5:
            # Salir del programa
            programa_ejecutandose = False
            print("\n📚 ¡Gracias por usar el Sistema de Gestión de Biblioteca!")
            print("¡Sigue leyendo y expandiendo tu conocimiento! 📖✨")

        # Pausa para que el usuario pueda leer los resultados
        if programa_ejecutandose:
            input("\nPresiona Enter para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
