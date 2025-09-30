import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas UEA")
        self.root.geometry("800x650")
        self.root.configure(bg='#1a1a2e')

        # Configurar tema de colores institucionales de la UEA
        self.colors = {
            'primary': '#1b5e20',  # Verde oscuro UEA
            'secondary': '#2e7d32',  # Verde medio UEA
            'accent': '#607d8b',  # Gris azulado elegante
            'accent_hover': '#78909c',  # Gris azulado claro hover
            'bg': '#0d3d0d',  # Verde muy oscuro fondo
            'text': '#ffffff',
            'completed': '#9e9e9e',
            'pending': '#b0bec5',  # Gris claro para pendientes
            'delete': '#d32f2f'
        }

        self.tasks = []
        self.selected_index = None

        self.create_header()
        self.create_input_section()
        self.create_tasks_section()
        self.create_footer()
        self.setup_bindings()

    def create_header(self):
        """Crear encabezado con información del estudiante"""
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=120)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)

        # Título principal
        title_label = tk.Label(
            header_frame,
            text="🌿 Gestor de Tareas UEA",
            font=('Helvetica', 32, 'bold'),
            bg=self.colors['primary'],
            fg=self.colors['accent']
        )
        title_label.pack(pady=(15, 5))

        # Información del estudiante
        student_info = tk.Label(
            header_frame,
            text="Desarrollado por: Cristian Chiquimba\nUniversidad Estatal Amazónica",
            font=('Helvetica', 11),
            bg=self.colors['primary'],
            fg=self.colors['text'],
            justify='center'
        )
        student_info.pack()

        # Fecha actual
        date_label = tk.Label(
            header_frame,
            text=datetime.now().strftime("%d/%m/%Y"),
            font=('Helvetica', 10),
            bg=self.colors['primary'],
            fg=self.colors['accent']
        )
        date_label.pack(pady=(5, 10))

    def create_input_section(self):
        """Crear sección de entrada de tareas"""
        input_frame = tk.Frame(self.root, bg=self.colors['bg'])
        input_frame.pack(fill='x', padx=30, pady=20)

        # Label de instrucción
        instruction_label = tk.Label(
            input_frame,
            text="Nueva Tarea:",
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['text']
        )
        instruction_label.pack(anchor='w', pady=(0, 5))

        # Frame para entrada y botón
        entry_frame = tk.Frame(input_frame, bg=self.colors['bg'])
        entry_frame.pack(fill='x')

        # Campo de entrada con estilo
        self.task_entry = tk.Entry(
            entry_frame,
            font=('Helvetica', 13),
            bg=self.colors['secondary'],
            fg=self.colors['text'],
            insertbackground=self.colors['accent'],
            relief='flat',
            bd=0
        )
        self.task_entry.pack(side='left', fill='x', expand=True, ipady=10, ipadx=10)
        self.task_entry.focus()

        # Botón añadir
        self.add_button = tk.Button(
            entry_frame,
            text="➕ Añadir (Enter)",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['accent'],
            fg=self.colors['primary'],
            activebackground=self.colors['accent_hover'],
            activeforeground=self.colors['primary'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.add_task
        )
        self.add_button.pack(side='left', padx=(10, 0), ipady=10, ipadx=15)

    def create_tasks_section(self):
        """Crear sección de lista de tareas"""
        tasks_frame = tk.Frame(self.root, bg=self.colors['bg'])
        tasks_frame.pack(fill='both', expand=True, padx=30, pady=(0, 20))

        # Header de la lista
        list_header = tk.Frame(tasks_frame, bg=self.colors['secondary'], height=40)
        list_header.pack(fill='x')
        list_header.pack_propagate(False)

        header_label = tk.Label(
            list_header,
            text="📋 Mis Tareas",
            font=('Helvetica', 14, 'bold'),
            bg=self.colors['secondary'],
            fg=self.colors['accent']
        )
        header_label.pack(side='left', padx=15, pady=8)

        # Contador de tareas
        self.counter_label = tk.Label(
            list_header,
            text="Total: 0 | Pendientes: 0 | Completadas: 0",
            font=('Helvetica', 10),
            bg=self.colors['secondary'],
            fg=self.colors['text']
        )
        self.counter_label.pack(side='right', padx=15)

        # Frame para listbox y scrollbar
        list_frame = tk.Frame(tasks_frame, bg=self.colors['secondary'])
        list_frame.pack(fill='both', expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame, bg=self.colors['secondary'])
        scrollbar.pack(side='right', fill='y')

        # Listbox para tareas
        self.tasks_listbox = tk.Listbox(
            list_frame,
            font=('Helvetica', 12),
            bg=self.colors['secondary'],
            fg=self.colors['text'],
            selectbackground=self.colors['accent'],
            selectforeground=self.colors['primary'],
            relief='flat',
            bd=0,
            yscrollcommand=scrollbar.set,
            activestyle='none'
        )
        self.tasks_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=self.tasks_listbox.yview)

        # Botones de acción
        buttons_frame = tk.Frame(tasks_frame, bg=self.colors['bg'])
        buttons_frame.pack(fill='x', pady=(15, 0))

        # Botón completar
        complete_btn = tk.Button(
            buttons_frame,
            text="✓ Completar (C)",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['accent'],
            fg=self.colors['primary'],
            activebackground=self.colors['accent_hover'],
            activeforeground=self.colors['primary'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.complete_task
        )
        complete_btn.pack(side='left', expand=True, fill='x', padx=(0, 5), ipady=10)

        # Botón eliminar
        delete_btn = tk.Button(
            buttons_frame,
            text="🗑 Eliminar (D/Del)",
            font=('Helvetica', 11, 'bold'),
            bg=self.colors['delete'],
            fg=self.colors['text'],
            activebackground='#e74c3c',
            activeforeground=self.colors['text'],
            relief='flat',
            bd=0,
            cursor='hand2',
            command=self.delete_task
        )
        delete_btn.pack(side='left', expand=True, fill='x', padx=(5, 0), ipady=10)

    def create_footer(self):
        """Crear pie de página con atajos"""
        footer_frame = tk.Frame(self.root, bg=self.colors['primary'], height=60)
        footer_frame.pack(fill='x', side='bottom')
        footer_frame.pack_propagate(False)

        shortcuts_label = tk.Label(
            footer_frame,
            text="⌨️ Atajos: Enter=Añadir | C=Completar | D/Delete=Eliminar | ESC=Cerrar",
            font=('Helvetica', 10),
            bg=self.colors['primary'],
            fg=self.colors['text']
        )
        shortcuts_label.pack(expand=True)

    def setup_bindings(self):
        """Configurar atajos de teclado"""
        # Enter para añadir tarea
        self.task_entry.bind('<Return>', lambda e: self.add_task())

        # C para completar tarea
        self.root.bind('<c>', lambda e: self.complete_task())
        self.root.bind('<C>', lambda e: self.complete_task())

        # D o Delete para eliminar tarea
        self.root.bind('<d>', lambda e: self.delete_task())
        self.root.bind('<D>', lambda e: self.delete_task())
        self.root.bind('<Delete>', lambda e: self.delete_task())

        # ESC para cerrar aplicación
        self.root.bind('<Escape>', lambda e: self.close_app())

        # Click en listbox para seleccionar
        self.tasks_listbox.bind('<<ListboxSelect>>', self.on_select)

    def add_task(self):
        """Añadir nueva tarea"""
        task_text = self.task_entry.get().strip()

        if not task_text:
            messagebox.showwarning(
                "Advertencia",
                "Por favor, ingresa una tarea antes de añadir."
            )
            return

        # Crear diccionario de tarea
        task = {
            'text': task_text,
            'completed': False,
            'timestamp': datetime.now().strftime("%H:%M")
        }

        self.tasks.append(task)
        self.update_listbox()
        self.task_entry.delete(0, tk.END)
        self.task_entry.focus()

    def complete_task(self):
        """Marcar tarea como completada"""
        selection = self.tasks_listbox.curselection()

        if not selection:
            messagebox.showinfo(
                "Información",
                "Por favor, selecciona una tarea para marcar como completada."
            )
            return

        index = selection[0]
        self.tasks[index]['completed'] = not self.tasks[index]['completed']
        self.update_listbox()

        # Mantener la selección
        self.tasks_listbox.selection_set(index)

    def delete_task(self):
        """Eliminar tarea seleccionada"""
        selection = self.tasks_listbox.curselection()

        if not selection:
            messagebox.showinfo(
                "Información",
                "Por favor, selecciona una tarea para eliminar."
            )
            return

        index = selection[0]
        task_text = self.tasks[index]['text']

        if messagebox.askyesno(
                "Confirmar eliminación",
                f"¿Estás seguro de eliminar la tarea:\n\n'{task_text}'?"
        ):
            del self.tasks[index]
            self.update_listbox()

    def update_listbox(self):
        """Actualizar la visualización de la lista de tareas"""
        self.tasks_listbox.delete(0, tk.END)

        pending_count = 0
        completed_count = 0

        for i, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "○"
            time = task['timestamp']
            display_text = f"{status} {task['text']} [{time}]"

            self.tasks_listbox.insert(tk.END, display_text)

            # Cambiar color según estado
            if task['completed']:
                self.tasks_listbox.itemconfig(i, fg=self.colors['completed'])
                completed_count += 1
            else:
                self.tasks_listbox.itemconfig(i, fg=self.colors['pending'])
                pending_count += 1

        # Actualizar contador
        total = len(self.tasks)
        self.counter_label.config(
            text=f"Total: {total} | Pendientes: {pending_count} | Completadas: {completed_count}"
        )

    def on_select(self, event):
        """Manejar selección de tarea"""
        selection = self.tasks_listbox.curselection()
        if selection:
            self.selected_index = selection[0]

    def close_app(self):
        """Cerrar aplicación"""
        if messagebox.askyesno(
                "Cerrar aplicación",
                "¿Estás seguro de que deseas cerrar el Gestor de Tareas?"
        ):
            self.root.quit()


def main():
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()