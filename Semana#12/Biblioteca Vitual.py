#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
==================================================================
SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
==================================================================
Programa creado por: Cristian Chiquimba
Fecha: Septiembre 2025
Curso: Programación Orientada a Objetos (POO)
==================================================================

Descripción:
Este programa implementa un sistema completo para gestionar una
biblioteca digital utilizando conceptos de POO y estructuras de
datos como tuplas, listas, diccionarios y conjuntos.

Funcionalidades principales:
- Gestión de libros (añadir/quitar)
- Administración de usuarios (registro/baja)
- Sistema de préstamos y devoluciones
- Búsqueda de libros por múltiples criterios
- Reportes y estadísticas

==================================================================
"""

# Importar módulos necesarios
import sys
import os


class Libro:
    """
    Clase que representa un libro en la biblioteca digital.
    Utiliza una tupla para almacenar autor y título (datos inmutables).
    """

    def __init__(self, titulo, autor, categoria, isbn):
        """
        Inicializa un libro con sus atributos.

        Args:
            titulo (str): Título del libro
            autor (str): Autor del libro
            categoria (str): Categoría/género del libro
            isbn (str): ISBN único del libro
        """
        # Usamos tupla para autor y título ya que no cambiarán
        self._autor_titulo = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False  # Estado del libro
        self.usuario_prestado = None  # Usuario que tiene el libro prestado

    @property
    def titulo(self):
        """Retorna el título del libro."""
        return self._autor_titulo[1]

    @property
    def autor(self):
        """Retorna el autor del libro."""
        return self._autor_titulo[0]

    def __str__(self):
        """Representación en cadena del libro."""
        estado = "Prestado" if self.prestado else "Disponible"
        return f"'{self.titulo}' por {self.autor} - Categoría: {self.categoria} - ISBN: {self.isbn} - Estado: {estado}"

    def __repr__(self):
        """Representación técnica del libro."""
        return f"Libro('{self.titulo}', '{self.autor}', '{self.categoria}', '{self.isbn}')"


class Usuario:
    """
    Clase que representa un usuario de la biblioteca.
    Mantiene una lista de libros actualmente prestados.
    """

    def __init__(self, nombre, id_usuario):
        """
        Inicializa un usuario.

        Args:
            nombre (str): Nombre del usuario
            id_usuario (str): ID único del usuario
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para gestionar libros prestados al usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        """
        Añade un libro a la lista de libros prestados del usuario.

        Args:
            libro (Libro): El libro a prestar
        """
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        """
        Remueve un libro de la lista de libros prestados del usuario.

        Args:
            libro (Libro): El libro a devolver
        """
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        """Representación en cadena del usuario."""
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"

    def __repr__(self):
        """Representación técnica del usuario."""
        return f"Usuario('{self.nombre}', '{self.id_usuario}')"


class Biblioteca:
    """
    Clase principal que gestiona la biblioteca digital.
    Utiliza diccionarios para libros, conjuntos para IDs únicos de usuarios.
    """

    def __init__(self, nombre="Biblioteca Digital"):
        """
        Inicializa la biblioteca.

        Args:
            nombre (str): Nombre de la biblioteca
        """
        self.nombre = nombre
        # Diccionario para almacenar libros con ISBN como clave para búsquedas eficientes
        self.libros_disponibles = {}
        # Diccionario para almacenar usuarios registrados
        self.usuarios_registrados = {}
        # Conjunto para manejar IDs de usuarios únicos
        self.ids_usuarios = set()
        # Lista para historial de préstamos (opcional para tracking)
        self.historial_prestamos = []

    def añadir_libro(self, libro):
        """
        Añade un libro a la biblioteca.

        Args:
            libro (Libro): El libro a añadir

        Returns:
            bool: True si se añadió exitosamente, False si ya existe
        """
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"✅ Libro añadido: {libro.titulo}")
            return True
        else:
            print(f"❌ El libro con ISBN {libro.isbn} ya existe en la biblioteca")
            return False

    def quitar_libro(self, isbn):
        """
        Quita un libro de la biblioteca.

        Args:
            isbn (str): ISBN del libro a quitar

        Returns:
            bool: True si se quitó exitosamente, False si no existe o está prestado
        """
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles[isbn]
            if not libro.prestado:
                del self.libros_disponibles[isbn]
                print(f"✅ Libro removido: {libro.titulo}")
                return True
            else:
                print(f"❌ No se puede quitar el libro '{libro.titulo}' porque está prestado")
                return False
        else:
            print(f"❌ No se encontró libro con ISBN {isbn}")
            return False

    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca.

        Args:
            usuario (Usuario): El usuario a registrar

        Returns:
            bool: True si se registró exitosamente, False si el ID ya existe
        """
        if usuario.id_usuario not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.id_usuario)
            self.usuarios_registrados[usuario.id_usuario] = usuario
            print(f"✅ Usuario registrado: {usuario.nombre}")
            return True
        else:
            print(f"❌ El ID de usuario {usuario.id_usuario} ya está registrado")
            return False

    def dar_de_baja_usuario(self, id_usuario):
        """
        Da de baja a un usuario de la biblioteca.

        Args:
            id_usuario (str): ID del usuario a dar de baja

        Returns:
            bool: True si se dio de baja exitosamente, False si no existe o tiene libros prestados
        """
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios_registrados[id_usuario]
            if len(usuario.libros_prestados) == 0:
                self.ids_usuarios.remove(id_usuario)
                del self.usuarios_registrados[id_usuario]
                print(f"✅ Usuario dado de baja: {usuario.nombre}")
                return True
            else:
                print(
                    f"❌ No se puede dar de baja al usuario {usuario.nombre} porque tiene {len(usuario.libros_prestados)} libro(s) prestado(s)")
                return False
        else:
            print(f"❌ No se encontró usuario con ID {id_usuario}")
            return False

    def prestar_libro(self, isbn, id_usuario):
        """
        Presta un libro a un usuario.

        Args:
            isbn (str): ISBN del libro a prestar
            id_usuario (str): ID del usuario que solicita el préstamo

        Returns:
            bool: True si el préstamo fue exitoso, False en caso contrario
        """
        # Verificar que el libro existe y está disponible
        if isbn not in self.libros_disponibles:
            print(f"❌ No se encontró libro con ISBN {isbn}")
            return False

        libro = self.libros_disponibles[isbn]
        if libro.prestado:
            print(f"❌ El libro '{libro.titulo}' ya está prestado")
            return False

        # Verificar que el usuario existe
        if id_usuario not in self.ids_usuarios:
            print(f"❌ No se encontró usuario con ID {id_usuario}")
            return False

        usuario = self.usuarios_registrados[id_usuario]

        # Realizar el préstamo
        libro.prestado = True
        libro.usuario_prestado = id_usuario
        usuario.tomar_prestado(libro)

        # Registrar en historial
        self.historial_prestamos.append({
            'accion': 'prestamo',
            'libro': libro.titulo,
            'usuario': usuario.nombre,
            'isbn': isbn,
            'id_usuario': id_usuario
        })

        print(f"✅ Libro '{libro.titulo}' prestado a {usuario.nombre}")
        return True

    def devolver_libro(self, isbn, id_usuario):
        """
        Procesa la devolución de un libro.

        Args:
            isbn (str): ISBN del libro a devolver
            id_usuario (str): ID del usuario que devuelve el libro

        Returns:
            bool: True si la devolución fue exitosa, False en caso contrario
        """
        # Verificar que el libro existe
        if isbn not in self.libros_disponibles:
            print(f"❌ No se encontró libro con ISBN {isbn}")
            return False

        libro = self.libros_disponibles[isbn]

        # Verificar que el libro está prestado al usuario correcto
        if not libro.prestado or libro.usuario_prestado != id_usuario:
            print(f"❌ El libro '{libro.titulo}' no está prestado a este usuario")
            return False

        # Verificar que el usuario existe
        if id_usuario not in self.ids_usuarios:
            print(f"❌ No se encontró usuario con ID {id_usuario}")
            return False

        usuario = self.usuarios_registrados[id_usuario]

        # Procesar devolución
        libro.prestado = False
        libro.usuario_prestado = None
        usuario.devolver_libro(libro)

        # Registrar en historial
        self.historial_prestamos.append({
            'accion': 'devolucion',
            'libro': libro.titulo,
            'usuario': usuario.nombre,
            'isbn': isbn,
            'id_usuario': id_usuario
        })

        print(f"✅ Libro '{libro.titulo}' devuelto por {usuario.nombre}")
        return True

    def buscar_libros(self, criterio, valor):
        """
        Busca libros por título, autor o categoría.

        Args:
            criterio (str): 'titulo', 'autor' o 'categoria'
            valor (str): Valor a buscar

        Returns:
            list: Lista de libros que coinciden con la búsqueda
        """
        resultados = []
        valor_lower = valor.lower()

        for libro in self.libros_disponibles.values():
            if criterio == 'titulo' and valor_lower in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == 'autor' and valor_lower in libro.autor.lower():
                resultados.append(libro)
            elif criterio == 'categoria' and valor_lower in libro.categoria.lower():
                resultados.append(libro)

        return resultados

    def listar_libros_prestados_usuario(self, id_usuario):
        """
        Lista todos los libros prestados a un usuario específico.

        Args:
            id_usuario (str): ID del usuario

        Returns:
            list: Lista de libros prestados al usuario
        """
        if id_usuario not in self.ids_usuarios:
            print(f"❌ No se encontró usuario con ID {id_usuario}")
            return []

        usuario = self.usuarios_registrados[id_usuario]
        return usuario.libros_prestados.copy()

    def mostrar_estadisticas(self):
        """Muestra estadísticas generales de la biblioteca."""
        total_libros = len(self.libros_disponibles)
        libros_prestados = sum(1 for libro in self.libros_disponibles.values() if libro.prestado)
        libros_disponibles = total_libros - libros_prestados
        total_usuarios = len(self.usuarios_registrados)

        print(f"\n📊 Estadísticas de {self.nombre}:")
        print(f"   📚 Total de libros: {total_libros}")
        print(f"   ✅ Libros disponibles: {libros_disponibles}")
        print(f"   📖 Libros prestados: {libros_prestados}")
        print(f"   👥 Usuarios registrados: {total_usuarios}")
        print(f"   📜 Transacciones en historial: {len(self.historial_prestamos)}")


def pausar():
    """Función para pausar la ejecución y permitir leer los resultados"""
    input("\nPresiona ENTER para continuar...")


def demo_biblioteca():
    """
    Función de demostración que prueba todas las funcionalidades del sistema.
    Creado por: Cristian Chiquimba
    """
    print("🏛️ SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL 🏛️")
    print("=" * 60)
    print("Programa creado por: Cristian Chiquimba")
    print("Curso: Programación Orientada a Objetos")
    print("=" * 60)

    # Crear biblioteca
    biblioteca = Biblioteca("Biblioteca Central Universitaria")

    print(f"\n📚 Biblioteca creada: {biblioteca.nombre}")
    pausar()

    # Crear libros usando tuplas para autor-título
    # FÁBULAS
    libro1 = Libro("Fábulas de Esopo", "Esopo", "Fábulas", "978-8420651234")
    libro2 = Libro("Fábulas de La Fontaine", "Jean de La Fontaine", "Fábulas", "978-8420651567")
    libro3 = Libro("Fábulas de Iriarte", "Tomás de Iriarte", "Fábulas", "978-8420651890")

    # FÍSICA
    libro4 = Libro("Física General", "Frederick J. Keller", "Física", "978-0070234567")
    libro5 = Libro("Fundamentos de Física", "Raymond A. Serway", "Física", "978-6074817892")
    libro6 = Libro("Física Universitaria", "Young & Freedman", "Física", "978-6073218000")

    # LENGUAJE Y LITERATURA
    libro7 = Libro("Gramática de la Lengua Española", "RAE", "Lenguaje", "978-8467007893")
    libro8 = Libro("Ortografía y Redacción", "María Moliner", "Lenguaje", "978-8424506789")
    libro9 = Libro("Literatura Española", "José García López", "Lenguaje", "978-8431673456")

    # DERECHO
    libro10 = Libro("Derecho Civil", "Manuel Albaladejo", "Derecho", "978-8491234567")
    libro11 = Libro("Derecho Penal", "Francisco Muñoz Conde", "Derecho", "978-8498765432")
    libro12 = Libro("Derecho Constitucional", "Pedro de Vega", "Derecho", "978-8413567890")

    # FILOSOFÍA
    libro13 = Libro("Introducción a la Filosofía", "Will Durant", "Filosofía", "978-8471239876")
    libro14 = Libro("Ética a Nicómaco", "Aristóteles", "Filosofía", "978-8420654321")
    libro15 = Libro("El Mundo de Sofía", "Jostein Gaarder", "Filosofía", "978-8478884567")

    # Añadir libros
    print(f"\n➕ AÑADIENDO LIBROS:")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)
    biblioteca.añadir_libro(libro4)
    biblioteca.añadir_libro(libro5)
    biblioteca.añadir_libro(libro6)
    biblioteca.añadir_libro(libro7)
    biblioteca.añadir_libro(libro8)
    biblioteca.añadir_libro(libro9)
    biblioteca.añadir_libro(libro10)
    biblioteca.añadir_libro(libro11)
    biblioteca.añadir_libro(libro12)
    biblioteca.añadir_libro(libro13)
    biblioteca.añadir_libro(libro14)
    biblioteca.añadir_libro(libro15)

    pausar()

    # Crear usuarios
    usuario1 = Usuario("María González", "USR001")
    usuario2 = Usuario("Carlos López", "USR002")
    usuario3 = Usuario("Ana Rodríguez", "USR003")
    usuario4 = Usuario("Juan Pérez", "USR004")
    usuario5 = Usuario("Laura Martín", "USR005")

    # Registrar usuarios
    print(f"\n👥 REGISTRANDO USUARIOS:")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)
    biblioteca.registrar_usuario(usuario3)
    biblioteca.registrar_usuario(usuario4)
    biblioteca.registrar_usuario(usuario5)

    # Mostrar estadísticas iniciales
    biblioteca.mostrar_estadisticas()
    pausar()

    # Realizar préstamos
    print(f"\n📖 REALIZANDO PRÉSTAMOS:")
    biblioteca.prestar_libro("978-8420651234", "USR001")  # Fábulas de Esopo a María
    biblioteca.prestar_libro("978-0070234567", "USR002")  # Física General a Carlos
    biblioteca.prestar_libro("978-8467007893", "USR003")  # Gramática RAE a Ana
    biblioteca.prestar_libro("978-8491234567", "USR004")  # Derecho Civil a Juan
    biblioteca.prestar_libro("978-8471239876", "USR005")  # Filosofía a Laura
    biblioteca.prestar_libro("978-8420651567", "USR001")  # Fábulas La Fontaine a María

    pausar()

    # Intentar préstamo de libro ya prestado
    print(f"\n❌ INTENTANDO PRÉSTAMO DE LIBRO YA PRESTADO:")
    biblioteca.prestar_libro("978-8420651234", "USR003")  # Ya prestado a María

    # Buscar libros
    print(f"\n🔍 BÚSQUEDA DE LIBROS:")

    print(f"\n📚 Búsqueda por categorías:")
    categorias = ["Fábulas", "Física", "Lenguaje", "Derecho", "Filosofía"]
    for categoria in categorias:
        resultados = biblioteca.buscar_libros("categoria", categoria)
        print(f"\n{categoria} ({len(resultados)} libros encontrados):")
        for libro in resultados[:3]:  # Mostrar solo los primeros 3
            print(f"   - {libro.titulo} por {libro.autor}")

    pausar()

    print(f"\n🔍 Búsqueda por autor:")
    resultados_autor = biblioteca.buscar_libros("autor", "Esopo")
    print(f"Libros de Esopo: {len(resultados_autor)}")
    for libro in resultados_autor:
        print(f"   - {libro}")

    print(f"\n🔍 Búsqueda por título:")
    resultados_titulo = biblioteca.buscar_libros("titulo", "Derecho")
    print(f"Libros con 'Derecho' en el título: {len(resultados_titulo)}")
    for libro in resultados_titulo:
        print(f"   - {libro.titulo} por {libro.autor}")

    pausar()

    # Listar libros prestados por usuario
    print(f"\n📋 LIBROS PRESTADOS POR USUARIO:")
    libros_maria = biblioteca.listar_libros_prestados_usuario("USR001")
    print(f"Libros prestados a {usuario1.nombre}:")
    for libro in libros_maria:
        print(f"   - {libro}")

    libros_carlos = biblioteca.listar_libros_prestados_usuario("USR002")
    print(f"Libros prestados a {usuario2.nombre}:")
    for libro in libros_carlos:
        print(f"   - {libro}")

    pausar()

    # Devolver libros
    print(f"\n🔄 DEVOLVIENDO LIBROS:")
    biblioteca.devolver_libro("978-8420651234", "USR001")  # María devuelve Fábulas de Esopo
    biblioteca.devolver_libro("978-0070234567", "USR002")  # Carlos devuelve Física General

    # Intentar dar de baja usuario con libros prestados
    print(f"\n❌ INTENTANDO DAR DE BAJA USUARIO CON LIBROS PRESTADOS:")
    biblioteca.dar_de_baja_usuario("USR001")  # María aún tiene Fábulas de La Fontaine

    # Devolver libro restante y dar de baja
    print(f"\n🔄 DEVOLVIENDO LIBRO RESTANTE:")
    biblioteca.devolver_libro("978-8420651567", "USR001")  # María devuelve Fábulas La Fontaine

    print(f"\n➖ DANDO DE BAJA USUARIO:")
    biblioteca.dar_de_baja_usuario("USR001")  # Ahora sí se puede dar de baja

    # Estadísticas finales
    biblioteca.mostrar_estadisticas()

    print(f"\n✨ DEMOSTRACIÓN COMPLETADA ✨")
    pausar()


def main():
    """Función principal del programa"""
    try:
        print("\n" + "=" * 80)
        print("              PROGRAMA CREADO POR: CRISTIAN CHIQUIMBA")
        print("              SISTEMA DE BIBLIOTECA DIGITAL - POO")
        print("=" * 80)

        demo_biblioteca()

        print("\n" + "=" * 80)
        print("           ¡GRACIAS POR USAR EL SISTEMA DE BIBLIOTECA!")
        print("              © 2025 - Cristian Chiquimba")
        print("=" * 80)

    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(f"\nError durante la ejecución: {e}")
        print("Por favor, verifica que Python esté correctamente instalado.")
    finally:
        input("\nPresiona ENTER para salir...")


# Ejecutar demostración si el script se ejecuta directamente
if __name__ == "__main__":
    main()