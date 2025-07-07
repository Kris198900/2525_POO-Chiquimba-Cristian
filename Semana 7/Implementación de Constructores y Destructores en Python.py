# Videojuego Simple con Constructores y Destructores
# Hecho para demostrar como funcionan __init__ y __del__ en Python
# Autor: Cristian David Chiquimba Mena
# Fecha: 07 de Julio, 2025

import random


class Jugador:
    """
    Esta clase representa un jugador en el juego.
    Aquí vamos a ver como trabajan los constructores y destructores.
    """

    def __init__(self, nombre):
        """
        CONSTRUCTOR: Este método se ejecuta cuando creamos un nuevo jugador
        Se llama automáticamente al hacer: jugador = Jugador("Ana")
        """
        self.nombre = nombre
        self.vida = 100
        self.puntos = 0
        self.nivel = 1

        # Esto se muestra cuando se crea el jugador
        print(f"¡Jugador {self.nombre} se ha unido al juego!")
        print(f"Vida: {self.vida}, Puntos: {self.puntos}, Nivel: {self.nivel}")

    def __del__(self):
        """
        DESTRUCTOR: Este método se ejecuta cuando el jugador se elimina
        Se activa cuando el objeto se borra de la memoria
        """
        print(f"¡{self.nombre} ha salido del juego!")
        print(f"Puntos finales: {self.puntos}")
        print("Guardando progreso...")

    def atacar(self):
        """El jugador ataca y gana puntos"""
        damage = random.randint(10, 30)
        self.puntos += damage
        print(f"{self.nombre} ataca y gana {damage} puntos")

        # Subir de nivel cada 100 puntos
        if self.puntos >= self.nivel * 100:
            self.nivel += 1
            print(f"¡{self.nombre} subió al nivel {self.nivel}!")

    def recibir_damage(self, damage):
        """El jugador recibe daño"""
        self.vida -= damage
        print(f"{self.nombre} recibe {damage} de daño. Vida: {self.vida}")

        if self.vida <= 0:
            print(f"{self.nombre} ha muerto en el juego")
            return False
        return True


class Enemigo:
    """
    Clase para crear enemigos en el juego.
    También usa constructor y destructor para mostrar como funcionan.
    """

    # Esta variable cuenta cuantos enemigos se han creado
    enemigos_creados = 0

    def __init__(self, tipo="Zombie"):
        """
        CONSTRUCTOR: Se ejecuta al crear un enemigo nuevo
        Inicializa las características del enemigo
        """
        Enemigo.enemigos_creados += 1
        self.tipo = tipo
        self.vida = random.randint(50, 80)
        self.ataque = random.randint(15, 25)
        self.id = Enemigo.enemigos_creados

        print(f"¡Apareció un {self.tipo} #{self.id}!")
        print(f"Vida: {self.vida}, Ataque: {self.ataque}")

    def __del__(self):
        """
        DESTRUCTOR: Se ejecuta cuando el enemigo muere o se elimina
        Hace limpieza y muestra mensaje de eliminación
        """
        print(f"El {self.tipo} #{self.id} fue derrotado")
        print("Liberando recursos del enemigo...")

    def atacar_jugador(self, jugador):
        """El enemigo ataca al jugador"""
        print(f"El {self.tipo} ataca a {jugador.nombre}!")
        return jugador.recibir_damage(self.ataque)

    def recibir_damage(self, damage):
        """El enemigo recibe daño"""
        self.vida -= damage
        print(f"El {self.tipo} recibe {damage} de daño. Vida: {self.vida}")

        if self.vida <= 0:
            print(f"¡El {self.tipo} ha sido eliminado!")
            return False
        return True


class PartidaJuego:
    """
    Esta clase maneja toda la partida del juego.
    Demuestra como usar constructores y destructores para manejar recursos.
    """

    def __init__(self, nombre_jugador):
        """
        CONSTRUCTOR: Inicializa una nueva partida
        Crea el jugador y prepara el juego
        """
        print("=== NUEVA PARTIDA ===")
        self.jugador = Jugador(nombre_jugador)
        self.enemigos = []
        self.rondas = 0
        print("Partida iniciada correctamente")

    def __del__(self):
        """
        DESTRUCTOR: Se ejecuta cuando termina la partida
        Hace limpieza final y muestra estadísticas
        """
        print("\n=== FIN DE LA PARTIDA ===")
        print(f"Rondas jugadas: {self.rondas}")
        print(f"Enemigos enfrentados: {len(self.enemigos)}")
        print("Cerrando partida...")

    def crear_enemigo(self):
        """Crea un nuevo enemigo para la batalla"""
        tipos_enemigos = ["Zombie", "Esqueleto", "Araña", "Goblin"]
        tipo = random.choice(tipos_enemigos)
        enemigo = Enemigo(tipo)
        self.enemigos.append(enemigo)
        return enemigo

    def batalla(self):
        """Simula una batalla entre jugador y enemigo"""
        print(f"\n--- RONDA {self.rondas + 1} ---")
        enemigo = self.crear_enemigo()

        # Batalla por turnos
        while self.jugador.vida > 0 and enemigo.vida > 0:
            # Turno del jugador
            self.jugador.atacar()
            if not enemigo.recibir_damage(random.randint(20, 40)):
                print("¡Enemigo derrotado!")
                break

            # Turno del enemigo
            if not enemigo.atacar_jugador(self.jugador):
                print("¡Jugador derrotado!")
                break

        self.rondas += 1

        # Eliminamos el enemigo manualmente para ver el destructor
        del enemigo

        return self.jugador.vida > 0


def main():
    """
    Función principal que demuestra constructores y destructores
    """
    print("DEMO: Constructores y Destructores en Python")
    print("Los constructores (__init__) se ejecutan al crear objetos")
    print("Los destructores (__del__) se ejecutan al eliminar objetos")
    print("-" * 50)

    # Creamos una partida - se ejecuta el constructor de PartidaJuego
    partida = PartidaJuego("Cristian")

    # Jugamos algunas rondas
    for i in range(3):
        if not partida.batalla():
            print("¡Game Over!")
            break

        print(f"\nEstado del jugador:")
        print(f"Vida: {partida.jugador.vida}")
        print(f"Puntos: {partida.jugador.puntos}")
        print(f"Nivel: {partida.jugador.nivel}")

    # Mostramos cuantos enemigos se crearon en total
    print(f"\nTotal de enemigos creados: {Enemigo.enemigos_creados}")

    # Creamos una segunda partida para Oscar
    print("\n" + "=" * 50)
    print("SEGUNDA PARTIDA - TURNO DE OSCAR")
    partida2 = PartidaJuego("Oscar")

    # Oscar juega 2 rondas
    for i in range(2):
        if not partida2.batalla():
            print("¡Game Over para Oscar!")
            break

        print(f"\nEstado de Oscar:")
        print(f"Vida: {partida2.jugador.vida}")
        print(f"Puntos: {partida2.jugador.puntos}")
        print(f"Nivel: {partida2.jugador.nivel}")

    # Al terminar la función, se ejecutan automáticamente los destructores
    print("\nTerminando programa...")

    # Podemos eliminar objetos manualmente para ver el destructor
    del partida
    del partida2


# Ejecutamos el programa
if __name__ == "__main__":
    main()
    print("Programa terminado - destructores ejecutados")