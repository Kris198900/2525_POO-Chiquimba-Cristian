# Autor: Cristian David Chiquimba Mena
# Descripción: Programa tradicional para calcular el promedio semanal del clima

def ingresar_temperaturas():
    """Solicita al usuario ingresar la temperatura diaria por una semana."""
    temperaturas = []
    print("Ingresa las temperaturas de los 7 días de la semana:")
    for dia in range(1, 8):
        temp = float(input(f"Temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de las temperaturas ingresadas."""
    return sum(temperaturas) / len(temperaturas)

def main():
    datos = ingresar_temperaturas()
    promedio = calcular_promedio(datos)
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Punto de entrada
if __name__ == "__main__":
    main()
