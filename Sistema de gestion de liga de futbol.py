# ============================================================================
# SISTEMA DE GESTIÓN DE LIGA DE FÚTBOL - EJEMPLO INTEGRAL DE POO
# ============================================================================
#
# Desarrollado por: Cristian Chiquimba
# Materia: Programación Orientada a Objetos
# Fecha: 07/06/2025
# ============================================================================

from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

# ============================================================================
# 1. ABSTRACCIÓN - Clase abstracta para Persona
# ============================================================================

class Persona(ABC):
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self._nombre = nombre
        self._edad = edad
        self._nacionalidad = nacionalidad

    @abstractmethod
    def descripcion(self) -> str:
        pass

    @property
    def nombre(self):
        return self._nombre

# ============================================================================
# 2. HERENCIA - Jugador y Entrenador heredan de Persona
# ============================================================================

class Jugador(Persona):
    def __init__(self, nombre: str, edad: int, nacionalidad: str, posicion: str, dorsal: int):
        super().__init__(nombre, edad, nacionalidad)
        self._posicion = posicion
        self._dorsal = dorsal
        self._goles = 0

    def anotar_gol(self):
        self._goles += 1

    def descripcion(self) -> str:
        return f"Jugador: {self._nombre} | Posición: {self._posicion} | Dorsal: {self._dorsal} | Goles: {self._goles}"

    @property
    def goles(self):
        return self._goles

class Entrenador(Persona):
    def __init__(self, nombre: str, edad: int, nacionalidad: str, estilo: str):
        super().__init__(nombre, edad, nacionalidad)
        self._estilo = estilo

    def descripcion(self) -> str:
        return f"Entrenador: {self._nombre} | Estilo: {self._estilo}"

# ============================================================================
# 3. ENCAPSULAMIENTO - Clase Equipo con atributos protegidos y métodos controlados
# ============================================================================

class Equipo:
    def __init__(self, nombre: str, entrenador: Entrenador):
        self._nombre = nombre
        self._entrenador = entrenador
        self._jugadores: List[Jugador] = []
        self.__puntos = 0  # Encapsulado: solo modificable por métodos internos

    def agregar_jugador(self, jugador: Jugador):
        if len(self._jugadores) < 11:
            self._jugadores.append(jugador)

    def registrar_victoria(self):
        self.__puntos += 3

    def registrar_empate(self):
        self.__puntos += 1

    def puntos(self):
        return self.__puntos

    def plantilla(self):
        return [j.descripcion() for j in self._jugadores]

    def descripcion(self):
        return f"Equipo: {self._nombre} | Entrenador: {self._entrenador.nombre} | Puntos: {self.__puntos}"

# ============================================================================
# 4. POLIMORFISMO - Partido entre diferentes tipos de equipos
# ============================================================================

class Partido:
    def __init__(self, equipo_local: Equipo, equipo_visitante: Equipo, fecha: datetime):
        self._equipo_local = equipo_local
        self._equipo_visitante = equipo_visitante
        self._fecha = fecha
        self._goles_local = 0
        self._goles_visitante = 0

    def jugar(self, goles_local: int, goles_visitante: int):
        self._goles_local = goles_local
        self._goles_visitante = goles_visitante
        if goles_local > goles_visitante:
            self._equipo_local.registrar_victoria()
        elif goles_local < goles_visitante:
            self._equipo_visitante.registrar_victoria()
        else:
            self._equipo_local.registrar_empate()
            self._equipo_visitante.registrar_empate()

    def resumen(self):
        return (f"{self._equipo_local.descripcion()} vs {self._equipo_visitante.descripcion()} | "
                f"Resultado: {self._goles_local}-{self._goles_visitante}")

# ============================================================================
# EJEMPLO DE USO: LIGA BARCELONA
# ============================================================================

if __name__ == "__main__":
    # Entrenadores
    entrenador_bsc = Entrenador("Diego López", 49, "Uruguay", "Ofensivo")
    entrenador_liga = Entrenador("Pablo Repetto", 50, "Uruguay", "Defensivo")

    # Equipos
    barcelona = Equipo("Barcelona SC", entrenador_bsc)
    liga_quito = Equipo("Liga de Quito", entrenador_liga)

    # Agregar jugadores a Barcelona SC
    nombres_bsc = [
        "Javier Burrai", "Pedro Velasco", "Mario Pineida", "Luca Sosa", "Leonel Quiñónez",
        "Gabriel Cortez", "Damián Díaz", "Fidel Martínez", "Adonis Preciado", "Janner Corozo", "Francisco Fydriszewski"
    ]
    for i, nombre in enumerate(nombres_bsc, 1):
        barcelona.agregar_jugador(Jugador(nombre, 25+i, "Ecuador", "Titular", i))

    # Agregar jugadores a Liga de Quito
    nombres_ldu = [
        "Alexander Domínguez", "Luis Caicedo", "Franklin Guerra", "José Quintero", "Luis Ayala",
        "Ezequiel Piovi", "Lucas Villarruel", "Alexander Alvarado", "Jhojan Julio", "Lisandro Alzugaray", "Paolo Guerrero"
    ]
    for i, nombre in enumerate(nombres_ldu, 1):
        liga_quito.agregar_jugador(Jugador(nombre, 24+i, "Ecuador", "Titular", i))

    # Jugar partido
    partido = Partido(barcelona, liga_quito, datetime.now())
    partido.jugar(2, 1)  # Barcelona SC gana 2-1

    print(partido.resumen())
    print("\nPlantilla Barcelona SC:")
    for jugador in barcelona.plantilla():
        print(jugador)
    print("\nPlantilla Liga de Quito:")
    for jugador in liga_quito.plantilla():
        print(jugador)
