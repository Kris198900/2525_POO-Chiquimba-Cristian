import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class ListaDeTareas:
    def __init__(self, root):
        """
        Inicializa la interfaz de usuario y configura los elementos.
        Args:
            root (tk.Tk): Ventana principal de la aplicación.
        """
        self.root = root
        self.root.title("Aplicación de Lista de Tareas - DAVID MENA")
        self.root.geometry("600x600")

        # Lista de tareas con fechas de creación y estado
        self.tareas = []

        # Crear widgets
        self.crear_widgets()

    def crear_widgets(self):
        """Crea los widgets de la interfaz gráfica."""
        # Frame principal
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame para el encabezado
        self.header_frame = tk.Frame(self.main_frame, bg="#4CAF50", padx=10, pady=10)
        self.header_frame.pack(fill=tk.X, pady=10)

        # Título de la aplicación
        self.encabezado = tk.Label(self.header_frame, text="📋 LISTA DE TAREAS DE DAVID MENA",
                                   font=("Arial", 16, "bold"), fg="white", bg="#4CAF50")
        self.encabezado.pack()

        # Frame para la entrada de tarea
        self.input_frame = tk.Frame(self.main_frame, padx=10, pady=10)
        self.input_frame.pack(fill=tk.X)

        # Campo de entrada para nuevas tareas
        self.input_tarea = tk.Entry(self.input_frame, width=50, font=("Arial", 12))
        self.input_tarea.grid(row=0, column=0, padx=10)

        # Botón para añadir tarea
        self.boton_añadir = tk.Button(self.input_frame, text="Añadir Tarea", width=20, command=self.añadir_tarea,
                                      font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
        self.boton_añadir.grid(row=0, column=1)

        # Frame para la lista de tareas
        self.list_frame = tk.Frame(self.main_frame, padx=10, pady=10)
        self.list_frame.pack(fill=tk.BOTH, expand=True)

        # Lista de tareas (usando Listbox)
        self.lista_tareas = tk.Listbox(self.list_frame, width=60, height=15, selectmode=tk.SINGLE, font=("Arial", 12))
        self.lista_tareas.pack(pady=10)

        # Frame para botones de acción
        self.action_frame = tk.Frame(self.main_frame, padx=10, pady=10)
        self.action_frame.pack(fill=tk.X)

        # Botón para marcar como completada
        self.boton_completar = tk.Button(self.action_frame, text="Marcar como Completada", width=20,
                                         command=self.marcar_completada, font=("Arial", 12, "bold"), bg="#4CAF50",
                                         fg="white")
        self.boton_completar.grid(row=0, column=0, padx=10)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(self.action_frame, text="Eliminar Tarea", width=20, command=self.eliminar_tarea,
                                        font=("Arial", 12, "bold"), bg="#FF5722", fg="white")
        self.boton_eliminar.grid(row=0, column=1, padx=10)

        # Asociar la tecla Enter al añadir tarea
        self.input_tarea.bind('<Return>', lambda event: self.añadir_tarea())

        # Barra de estado en la parte inferior
        self.status_bar = tk.Label(self.root, text="Bienvenido a la Lista de Tareas", bg="#333", fg="white",
                                   font=("Arial", 10))
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def añadir_tarea(self):
        """Añade una nueva tarea a la lista con la fecha de creación y estado 'Pendiente'."""
        tarea = self.input_tarea.get()
        if tarea != "":
            fecha_creacion = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.tareas.append({"descripcion": tarea, "fecha": fecha_creacion, "estado": "Pendiente"})
            self.actualizar_lista()
            self.input_tarea.delete(0, tk.END)
            self.update_status("Tarea añadida correctamente", "success")
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

    def marcar_completada(self):
        """Marca una tarea seleccionada como completada."""
        try:
            seleccion = self.lista_tareas.curselection()
            if seleccion:
                tarea_completada = self.lista_tareas.get(seleccion)
                indice = seleccion[0]
                tarea_completada = f"{tarea_completada} - Completada"
                self.tareas[indice]["descripcion"] = tarea_completada
                self.tareas[indice]["estado"] = "Completada"
                self.actualizar_lista()
                self.update_status("Tarea marcada como completada", "success")
            else:
                messagebox.showwarning("Selección requerida",
                                       "Por favor, selecciona una tarea para marcar como completada.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema: {e}")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada con confirmación."""
        try:
            seleccion = self.lista_tareas.curselection()
            if seleccion:
                indice = seleccion[0]
                confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar esta tarea?")
                if confirmacion:
                    self.tareas.pop(indice)
                    self.actualizar_lista()
                    self.update_status("Tarea eliminada correctamente", "error")
            else:
                messagebox.showwarning("Selección requerida", "Por favor, selecciona una tarea para eliminarla.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema: {e}")

    def actualizar_lista(self):
        """Actualiza la lista de tareas en la interfaz."""
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            tarea_mostrada = f"{tarea['descripcion']} - {tarea['fecha']} - {tarea['estado']}"
            self.lista_tareas.insert(tk.END, tarea_mostrada)

    def update_status(self, message, status_type):
        """Actualiza la barra de estado."""
        if status_type == "success":
            self.status_bar.config(text=message, bg="#4CAF50", fg="white")
        elif status_type == "error":
            self.status_bar.config(text=message, bg="#FF5722", fg="white")
        else:
            self.status_bar.config(text=message, bg="#333", fg="white")


if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareas(root)
    root.mainloop()
