# Clase Cliente: Representa a un cliente con nombre y correo electrónico
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Email: {self.email}"

# Clase Habitacion: Representa una habitación en un sistema de reservas
class Habitacion:
    def __init__(self, numero, tipo, disponibilidad=True):
        self.numero = numero
        self.tipo = tipo
        self.disponibilidad = disponibilidad  # Se agrega la disponibilidad de la habitación

    def mostrar_habitacion(self):
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return f"Habitación {self.numero}, Tipo: {self.tipo}, Estado: {estado}"

    def cambiar_disponibilidad(self, disponibilidad):
        self.disponibilidad = disponibilidad

# Clase Reserva: Gestiona las reservas hechas por los clientes
class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def mostrar_reserva(self):
        return f"Reserva para {self.cliente.nombre}: {self.habitacion.mostrar_habitacion()} desde {self.fecha_inicio} hasta {self.fecha_fin}"

    def confirmar_reserva(self):
        if self.habitacion.disponibilidad:  # Verifica si la habitación está disponible
            self.habitacion.cambiar_disponibilidad(False)  # Marca la habitación como no disponible
            return f"Reserva confirmada para {self.cliente.nombre} en la habitación {self.habitacion.numero}."
        else:
            return "La habitación no está disponible para las fechas seleccionadas."

    def cancelar_reserva(self):
        self.habitacion.cambiar_disponibilidad(True)  # Marca la habitación como disponible nuevamente
        return f"Reserva cancelada para {self.cliente.nombre}. La habitación {self.habitacion.numero} ahora está disponible."

# Ejemplo de uso del sistema
cliente1 = Cliente("Juan Pérez", "juan@example.com")
cliente2 = Cliente("Ana Gómez", "ana@example.com")

habitacion1 = Habitacion(101, "Individual")
habitacion2 = Habitacion(102, "Doble", disponibilidad=False)  # Habitacion ya ocupada

# Crear una reserva
reserva1 = Reserva(cliente1, habitacion1, "2023-07-01", "2023-07-05")
reserva2 = Reserva(cliente2, habitacion2, "2023-07-01", "2023-07-05")

# Mostrar información de la reserva y la disponibilidad
print(reserva1.mostrar_reserva())
print(reserva1.confirmar_reserva())  # Confirmar la reserva

print(reserva2.mostrar_reserva())
print(reserva2.confirmar_reserva())  # Intentar confirmar una reserva con habitación no disponible

# Cancelar una reserva
print(reserva1.cancelar_reserva())

# Mostrar el estado de la habitación después de la cancelación
print(habitacion1.mostrar_habitacion())
