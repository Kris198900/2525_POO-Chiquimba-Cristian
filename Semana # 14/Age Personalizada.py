import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import json
import os


class Evento:
    """Clase para representar un evento en la agenda."""

    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion

    def __repr__(self):
        return f"{self.fecha} {self.hora} - {self.descripcion}"


class Agenda:
    """Clase para representar la agenda personal."""

    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personalizada David")  # Título personalizado
        self.root.geometry("900x700")
        self.root.configure(bg='#f1f1f1')  # Fondo gris claro, similar al estilo de Windows

        self.eventos = []  # Lista de objetos Evento

        self.configurar_estilos()
        self.crear_interfaz()
        self.cargar_eventos()

    def configurar_estilos(self):
        """Configurar los estilos para la interfaz."""
        style = ttk.Style()

        # Estilo general para TreeView (tabla de eventos)
        style.configure("Custom.Treeview",
                        background="#ffffff",  # Fondo blanco
                        foreground="#000000",  # Texto negro
                        rowheight=30,
                        fieldbackground="#f4f4f4",  # Fondo gris claro
                        font=('Arial', 12),
                        borderwidth=1)

        style.configure("Custom.Treeview.Heading",
                        font=('Arial', 14, 'bold'),
                        foreground="#0078d4",  # Color azul, similar al de Windows
                        background="#e4e4e4")  # Color gris claro de encabezados

        # Estilo para botones (fondo azul claro, texto blanco)
        style.configure("TButton",
                        background="#0066cc",  # Azul claro
                        foreground="white",  # Texto blanco
                        font=('Arial', 12, 'bold'),
                        relief="flat")

        # Estilo para los botones cuando están en "hover" (enfoque)
        style.map("TButton",
                  background=[('active', '#0055a3')])  # Cambia a azul más oscuro cuando el botón está activo

    def crear_interfaz(self):
        """Crear los componentes de la interfaz."""
        frame_eventos = tk.Frame(self.root, bg='#f1f1f1')
        frame_eventos.pack(padx=20, pady=20, fill="both", expand=True)

        # Título de la aplicación (centrado)
        titulo = tk.Label(frame_eventos, text="Agenda Personalizada", font=("Helvetica", 24, 'bold'), bg="#f1f1f1",
                          fg="#333333")
        titulo.grid(row=0, column=0, columnspan=3, pady=20)

        # Nombre "David" debajo del título (centrado)
        nombre_label = tk.Label(frame_eventos, text="David", font=("Helvetica", 18), bg="#f1f1f1", fg="#333333")
        nombre_label.grid(row=1, column=0, columnspan=3, pady=10)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings",
                                 style="Custom.Treeview")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

        # Campos de entrada (con letras negras)
        self.fecha_entry = DateEntry(frame_eventos, width=12, background="lightblue", foreground="black", borderwidth=2)
        self.fecha_entry.grid(row=3, column=0, padx=5, pady=5)

        self.hora_entry = tk.Entry(frame_eventos, width=12, font=('Arial', 12), bg="white", fg="black",
                                   insertbackground="black")
        self.hora_entry.grid(row=3, column=1, padx=5, pady=5)

        self.descripcion_entry = tk.Entry(frame_eventos, width=30, font=('Arial', 12), bg="white", fg="black",
                                          insertbackground="black")
        self.descripcion_entry.grid(row=3, column=2, padx=5, pady=5)

        # Botones con color azul claro y texto blanco
        self.agregar_button = ttk.Button(frame_eventos, text="Agregar Evento", command=self.agregar_evento)
        self.agregar_button.grid(row=4, column=0, padx=10, pady=10)

        self.eliminar_button = ttk.Button(frame_eventos, text="Eliminar Evento Seleccionado",
                                          command=self.eliminar_evento)
        self.eliminar_button.grid(row=4, column=1, padx=10, pady=10)

        self.salir_button = ttk.Button(frame_eventos, text="Salir", command=self.root.quit)
        self.salir_button.grid(row=4, column=2, padx=10, pady=10)

    def agregar_evento(self):
        """Agregar un evento a la lista y actualizar la interfaz."""
        fecha = self.fecha_entry.get_date()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if fecha and hora and descripcion:
            # Crear un objeto Evento y agregarlo a la lista
            evento = Evento(fecha, hora, descripcion)
            self.eventos.append(evento)

            # Actualizar la vista
            self.tree.insert("", "end", values=(evento.fecha, evento.hora, evento.descripcion))

            # Limpiar campos
            self.fecha_entry.delete(0, "end")
            self.hora_entry.delete(0, "end")
            self.descripcion_entry.delete(0, "end")
        else:
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        """Eliminar el evento seleccionado."""
        selected_item = self.tree.selection()

        if selected_item:
            confirmation = messagebox.askyesno("Confirmar Eliminación",
                                               "¿Está seguro de que desea eliminar este evento?")
            if confirmation:
                # Eliminar el evento de la vista
                self.tree.delete(selected_item)

                # Eliminar el evento de la lista de objetos
                for evento in self.eventos:
                    if evento.fecha == self.tree.item(selected_item)['values'][0] and evento.hora == \
                            self.tree.item(selected_item)['values'][1]:
                        self.eventos.remove(evento)
                        break
        else:
            messagebox.showwarning("Selección Vacía", "Por favor, seleccione un evento para eliminar.")

    def cargar_eventos(self):
        """Cargar eventos desde el archivo JSON."""
        if os.path.exists("eventos.json"):
            try:
                with open("eventos.json", "r") as f:
                    eventos_data = json.load(f)
                    # Verificamos que el archivo tenga datos válidos
                    if eventos_data is not None:
                        for evento_data in eventos_data:
                            evento = Evento(evento_data['Fecha'], evento_data['Hora'], evento_data['Descripción'])
                            self.eventos.append(evento)
                            self.tree.insert("", "end", values=(evento.fecha, evento.hora, evento.descripcion))
            except json.JSONDecodeError:
                # Si el archivo está vacío o tiene datos no válidos, muestra un mensaje
                messagebox.showerror("Error", "El archivo eventos.json está vacío o tiene un formato incorrecto.")
                # Se puede inicializar una lista vacía si el archivo está mal o vacío
                self.eventos = []
        else:
            # Si el archivo no existe, lo creamos vacío
            with open("eventos.json", "w") as f:
                json.dump([], f)  # Crear un archivo JSON vacío

    def guardar_eventos(self):
        """Guardar los eventos en el archivo JSON."""
        eventos_data = [{'Fecha': evento.fecha, 'Hora': evento.hora, 'Descripción': evento.descripcion} for evento in
                        self.eventos]
        with open("eventos.json", "w") as f:
            json.dump(eventos_data, f)


if __name__ == "__main__":
    root = tk.Tk()
    agenda = Agenda(root)
    root.protocol("WM_DELETE_WINDOW", agenda.guardar_eventos)  # Guardar eventos al cerrar la aplicación
    root.mainloop()
