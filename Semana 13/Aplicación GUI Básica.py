import tkinter as tk
from tkinter import messagebox

# Función para agregar un dato a la lista
def agregar_dato():
    dato = campo_texto.get()  # Obtiene el texto del campo de texto
    if dato != "":  # Verifica que el campo no esté vacío
        lista_datos.insert(tk.END, dato)  # Inserta el dato en la lista
        campo_texto.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese un dato.")  # Muestra un mensaje de advertencia

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)  # Elimina todos los elementos de la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos - Cristian Chiquimba")  # Título descriptivo con tu nombre
ventana.geometry("500x400")  # Establece el tamaño de la ventana
ventana.config(bg="#f0f0f0")  # Establece un color de fondo suave

# Crear y ubicar los componentes
etiqueta_titulo = tk.Label(ventana, text="Bienvenida a la Gestión de Datos de Cristian Chiquimba", font=("Arial", 16), bg="#f0f0f0", fg="#333333")  # Etiqueta para el título con tu nombre
etiqueta_titulo.pack(pady=20)

campo_texto = tk.Entry(ventana, width=40, font=("Arial", 12), borderwidth=2, relief="solid")  # Campo de texto con borde
campo_texto.pack(pady=10)

# Botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", width=20, font=("Arial", 12), bg="#4CAF50", fg="white", command=agregar_dato)  # Botón verde
boton_agregar.pack(pady=5)

# Botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", width=20, font=("Arial", 12), bg="#f44336", fg="white", command=limpiar_lista)  # Botón rojo
boton_limpiar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(ventana, width=40, height=10, font=("Arial", 12), bg="#ffffff", fg="#333333", selectmode=tk.SINGLE, bd=2, relief="solid")
lista_datos.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
