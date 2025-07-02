"""
Sistema de Gestión de Vehículos
Aplicación de Conceptos de POO en Python

Mi programa demuestra:
1. Herencia: Clase base Vehiculo y clases derivadas Auto, Motocicleta, Camion
2. Encapsulación: Atributos privados y métodos getter/setter
3. Polimorfismo: Métodos sobrescritos y comportamiento diferente según el tipo de objeto

Autor: Cristian David Chiquimba Mena
Fecha: 02 de Julio de 2025
"""

from abc import ABC, abstractmethod
from typing import List


class Vehiculo(ABC):
    """
    Clase base abstracta que representa un vehículo genérico.
    Demuestra ENCAPSULACIÓN con atributos privados y métodos de acceso.
    """

    def __init__(self, marca: str, modelo: str, año: int, precio: float):
        # Atributos privados (encapsulación)
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__precio = precio
        self.__kilometraje = 0.0
        self.__encendido = False

    # Métodos getter para acceder a atributos privados (encapsulación)
    @property
    def marca(self) -> str:
        return self.__marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @property
    def año(self) -> int:
        return self.__año

    @property
    def precio(self) -> float:
        return self.__precio

    @property
    def kilometraje(self) -> float:
        return self.__kilometraje

    @property
    def encendido(self) -> bool:
        return self.__encendido

    # Métodos setter con validación (encapsulación)
    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser positivo")

    def encender(self):
        """Enciende el vehículo"""
        self.__encendido = True
        print(f"{self.__marca} {self.__modelo} ha sido encendido.")

    def apagar(self):
        """Apaga el vehículo"""
        self.__encendido = False
        print(f"{self.__marca} {self.__modelo} ha sido apagado.")

    def conducir(self, kilometros: float):
        """Conduce el vehículo una cierta cantidad de kilómetros"""
        if self.__encendido and kilometros > 0:
            self.__kilometraje += kilometros
            print(f"Has conducido {kilometros} km. Kilometraje total: {self.__kilometraje} km")
        elif not self.__encendido:
            print("Debes encender el vehículo primero.")
        else:
            print("Los kilómetros deben ser positivos.")

    # Método abstracto que debe ser implementado por las clases derivadas (polimorfismo)
    @abstractmethod
    def mostrar_info(self) -> str:
        """Método abstracto para mostrar información del vehículo"""
        pass

    # Método que será sobrescrito en las clases derivadas (polimorfismo)
    def calcular_impuesto(self) -> float:
        """Calcula el impuesto base del vehículo"""
        return self.__precio * 0.05

    def __str__(self) -> str:
        return f"{self.__marca} {self.__modelo} ({self.__año})"


class Auto(Vehiculo):
    """
    Clase derivada que representa un automóvil.
    Demuestra HERENCIA heredando de Vehiculo.
    """

    def __init__(self, marca: str, modelo: str, año: int, precio: float,
                 num_puertas: int, tipo_combustible: str):
        # Llamada al constructor de la clase padre (herencia)
        super().__init__(marca, modelo, año, precio)
        self.__num_puertas = num_puertas
        self.__tipo_combustible = tipo_combustible

    @property
    def num_puertas(self) -> int:
        return self.__num_puertas

    @property
    def tipo_combustible(self) -> str:
        return self.__tipo_combustible

    # Implementación del método abstracto (polimorfismo)
    def mostrar_info(self) -> str:
        return (f"🚗 AUTO: {self.marca} {self.modelo} ({self.año})\n"
                f"   Puertas: {self.__num_puertas}\n"
                f"   Combustible: {self.__tipo_combustible}\n"
                f"   Precio: ${self.precio:,.2f}\n"
                f"   Kilometraje: {self.kilometraje} km")

    # Sobrescritura del método calcular_impuesto (polimorfismo)
    def calcular_impuesto(self) -> float:
        """Calcula impuesto específico para autos"""
        impuesto_base = super().calcular_impuesto()
        # Los autos híbridos tienen descuento del 20%
        if "híbrido" in self.__tipo_combustible.lower():
            return impuesto_base * 0.8
        return impuesto_base

    def abrir_puertas(self):
        """Método específico de los autos"""
        print(f"Se han abierto las {self.__num_puertas} puertas del {self.marca} {self.modelo}")


class Motocicleta(Vehiculo):
    """
    Clase derivada que representa una motocicleta.
    Demuestra HERENCIA heredando de Vehiculo.
    """

    def __init__(self, marca: str, modelo: str, año: int, precio: float,
                 cilindrada: int, tipo: str):
        super().__init__(marca, modelo, año, precio)
        self.__cilindrada = cilindrada
        self.__tipo = tipo  # deportiva, cruiser, touring, etc.

    @property
    def cilindrada(self) -> int:
        return self.__cilindrada

    @property
    def tipo(self) -> str:
        return self.__tipo

    # Implementación del método abstracto (polimorfismo)
    def mostrar_info(self) -> str:
        return (f"🏍️  MOTOCICLETA: {self.marca} {self.modelo} ({self.año})\n"
                f"   Cilindrada: {self.__cilindrada}cc\n"
                f"   Tipo: {self.__tipo}\n"
                f"   Precio: ${self.precio:,.2f}\n"
                f"   Kilometraje: {self.kilometraje} km")

    # Sobrescritura del método calcular_impuesto (polimorfismo)
    def calcular_impuesto(self) -> float:
        """Calcula impuesto específico para motocicletas"""
        impuesto_base = super().calcular_impuesto()
        # Las motocicletas pagan menos impuesto
        return impuesto_base * 0.6

    def hacer_wheelie(self):
        """Método específico de las motocicletas"""
        if self.encendido:
            print(f"¡La {self.marca} {self.modelo} está haciendo un wheelie! 🤸‍♂️")
        else:
            print("Debes encender la motocicleta primero.")


class Camion(Vehiculo):
    """
    Clase derivada que representa un camión.
    Demuestra HERENCIA heredando de Vehiculo.
    """

    def __init__(self, marca: str, modelo: str, año: int, precio: float,
                 capacidad_carga: float, num_ejes: int):
        super().__init__(marca, modelo, año, precio)
        self.__capacidad_carga = capacidad_carga  # en toneladas
        self.__num_ejes = num_ejes
        self.__carga_actual = 0.0

    @property
    def capacidad_carga(self) -> float:
        return self.__capacidad_carga

    @property
    def num_ejes(self) -> int:
        return self.__num_ejes

    @property
    def carga_actual(self) -> float:
        return self.__carga_actual

    # Implementación del método abstracto (polimorfismo)
    def mostrar_info(self) -> str:
        return (f"🚛 CAMIÓN: {self.marca} {self.modelo} ({self.año})\n"
                f"   Capacidad: {self.__capacidad_carga} toneladas\n"
                f"   Ejes: {self.__num_ejes}\n"
                f"   Carga actual: {self.__carga_actual} toneladas\n"
                f"   Precio: ${self.precio:,.2f}\n"
                f"   Kilometraje: {self.kilometraje} km")

    # Sobrescritura del método calcular_impuesto (polimorfismo)
    def calcular_impuesto(self) -> float:
        """Calcula impuesto específico para camiones"""
        impuesto_base = super().calcular_impuesto()
        # Los camiones pagan más impuesto según su capacidad
        factor_capacidad = 1 + (self.__capacidad_carga / 50)
        return impuesto_base * factor_capacidad

    def cargar(self, peso: float):
        """Método específico para cargar el camión"""
        if peso > 0 and (self.__carga_actual + peso) <= self.__capacidad_carga:
            self.__carga_actual += peso
            print(f"Se han cargado {peso} toneladas. Carga actual: {self.__carga_actual} toneladas")
        elif peso <= 0:
            print("El peso debe ser positivo.")
        else:
            print(f"No se puede cargar. Excedería la capacidad máxima de {self.__capacidad_carga} toneladas.")

    def descargar(self, peso: float):
        """Método específico para descargar el camión"""
        if peso > 0 and peso <= self.__carga_actual:
            self.__carga_actual -= peso
            print(f"Se han descargado {peso} toneladas. Carga actual: {self.__carga_actual} toneladas")
        elif peso <= 0:
            print("El peso debe ser positivo.")
        else:
            print(f"No se puede descargar {peso} toneladas. Solo hay {self.__carga_actual} toneladas cargadas.")


class Concesionario:
    """
    Clase que gestiona una colección de vehículos.
    Demuestra POLIMORFISMO al trabajar con diferentes tipos de vehículos de manera uniforme.
    """

    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__vehiculos: List[Vehiculo] = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    def agregar_vehiculo(self, vehiculo: Vehiculo):
        """Agrega un vehículo al concesionario"""
        self.__vehiculos.append(vehiculo)
        print(f"✅ {vehiculo} agregado al concesionario {self.__nombre}")

    def mostrar_inventario(self):
        """Muestra todos los vehículos del concesionario (POLIMORFISMO)"""
        if not self.__vehiculos:
            print(f"El concesionario {self.__nombre} no tiene vehículos en inventario.")
            return

        print(f"\n{'=' * 50}")
        print(f"📋 INVENTARIO - {self.__nombre}")
        print(f"{'=' * 50}")

        for i, vehiculo in enumerate(self.__vehiculos, 1):
            print(f"\n{i}. {vehiculo.mostrar_info()}")
            print(f"   Impuesto anual: ${vehiculo.calcular_impuesto():,.2f}")

    def calcular_valor_total(self) -> float:
        """Calcula el valor total del inventario"""
        return sum(vehiculo.precio for vehiculo in self.__vehiculos)

    def buscar_por_marca(self, marca: str) -> List[Vehiculo]:
        """Busca vehículos por marca"""
        return [v for v in self.__vehiculos if v.marca.lower() == marca.lower()]

    def vehiculos_por_tipo(self):
        """Cuenta vehículos por tipo (POLIMORFISMO)"""
        tipos = {}
        for vehiculo in self.__vehiculos:
            tipo = type(vehiculo).__name__
            tipos[tipo] = tipos.get(tipo, 0) + 1
        return tipos


def demostrar_polimorfismo(vehiculos: List[Vehiculo]):
    """
    Función que demuestra POLIMORFISMO.
    Recibe una lista de vehículos y llama a métodos que se comportan
    de manera diferente según el tipo específico de cada vehículo.
    """
    print(f"\n{'*' * 60}")
    print("🔄 DEMOSTRACIÓN DE POLIMORFISMO")
    print(f"{'*' * 60}")

    for vehiculo in vehiculos:
        print(f"\n--- Procesando {vehiculo} ---")
        # El método mostrar_info() se comporta diferente para cada tipo de vehículo
        print(vehiculo.mostrar_info())
        # El método calcular_impuesto() también tiene comportamiento específico
        print(f"💰 Impuesto: ${vehiculo.calcular_impuesto():,.2f}")


def main():
    """
    Función principal que demuestra todos los conceptos de POO.
    """
    print("🚗 SISTEMA DE GESTIÓN DE VEHÍCULOS")
    print("Demostrando Conceptos de POO en Python")
    print("=" * 50)

    # Crear instancias de diferentes tipos de vehículos (HERENCIA)
    auto1 = Auto("Chevrolet", "Family", 2023, 15000, 4, "Híbrido")
    auto2 = Auto("Honda", "Civic", 2022, 28000, 4, "Gasolina")

    moto1 = Motocicleta("Suzuki", "125", 2023, 3000, 125, "Pasola")
    moto2 = Motocicleta("Harley-Davidson", "Street Glide", 2022, 25000, 1750, "Cruiser")

    camion1 = Camion("Volvo", "FH16", 2023, 120000, 40, 6)
    camion2 = Camion("Mercedes-Benz", "Actros", 2022, 110000, 35, 5)

    # Crear concesionario
    concesionario = Concesionario("Patio Tuerca")

    # Agregar vehículos al concesionario
    vehiculos = [auto1, auto2, moto1, moto2, camion1, camion2]
    for vehiculo in vehiculos:
        concesionario.agregar_vehiculo(vehiculo)

    # Mostrar inventario (demuestra POLIMORFISMO)
    concesionario.mostrar_inventario()

    # Demostrar funcionalidades específicas de cada tipo
    print(f"\n{'*' * 60}")
    print("🔧 DEMOSTRANDO FUNCIONALIDADES ESPECÍFICAS")
    print(f"{'*' * 60}")

    # Operaciones con auto
    print(f"\n--- Operaciones con {auto1} ---")
    auto1.encender()
    auto1.conducir(150)
    auto1.abrir_puertas()
    auto1.apagar()

    # Operaciones con motocicleta
    print(f"\n--- Operaciones con {moto1} ---")
    moto1.encender()
    moto1.hacer_wheelie()
    moto1.conducir(80)
    moto1.apagar()

    # Operaciones con camión
    print(f"\n--- Operaciones con {camion1} ---")
    camion1.encender()
    camion1.cargar(25)
    camion1.conducir(200)
    camion1.descargar(10)
    camion1.apagar()

    # Demostrar polimorfismo explícitamente
    demostrar_polimorfismo([auto1, moto1, camion1])

    # Estadísticas del concesionario
    print(f"\n{'*' * 60}")
    print("📊 ESTADÍSTICAS DEL CONCESIONARIO")
    print(f"{'*' * 60}")
    print(f"Valor total del inventario: ${concesionario.calcular_valor_total():,.2f}")
    print(f"Vehículos por tipo: {concesionario.vehiculos_por_tipo()}")

    # Demostrar encapsulación intentando acceder a atributos privados
    print(f"\n{'*' * 60}")
    print("🔒 DEMOSTRANDO ENCAPSULACIÓN")
    print(f"{'*' * 60}")
    print(f"Precio del {auto1} (a través de property): ${auto1.precio:,.2f}")

    try:
        # Cambiar precio usando el setter (con validación)
        auto1.precio = 36000
        print(f"Nuevo precio del {auto1}: ${auto1.precio:,.2f}")

        # Intentar asignar precio inválido
        auto1.precio = -1000
    except ValueError as e:
        print(f"❌ Error capturado: {e}")

    print(f"\n✅ Demostración completada exitosamente!")
    print("Los conceptos de POO demostrados:")
    print("• HERENCIA: Auto, Motocicleta y Camion heredan de Vehiculo")
    print("• ENCAPSULACIÓN: Atributos privados con getters/setters")
    print("• POLIMORFISMO: Métodos sobrescritos y comportamiento específico por tipo")


if __name__ == "__main__":
    main()