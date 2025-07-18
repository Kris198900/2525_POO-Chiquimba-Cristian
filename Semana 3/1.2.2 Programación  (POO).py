# Autor: Cristian David Chiquimba Mena
# Descripción: Programa POO para calcular el promedio semanal del clima

class DiaClima:
    """Clase que representa un día de clima."""

    def __init__(self, temperatura):
        self.__temperatura = temperatura  # Encapsulamiento

    def get_temperatura(self):
        return self.__temperatura


class SemanaClima:
    """Clase que gestiona la semana completa de datos climáticos."""

    def __init__(self):
        self.dias = []

    def agregar_dia(self, temperatura):
        dia = DiaClima(temperatura)
        self.dias.append(dia)

    def calcular_promedio(self):
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)


def main():
    semana = SemanaClima()
    print("Ingresa las temperaturas de los 7 días de la semana:")
    for i in range(1, 8):
        temp = float(input(f"Temperatura del día {i}: "))
        semana.agregar_dia(temp)

    promedio = semana.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")


# Punto de entrada
if __name__ == "__main__":
    main()