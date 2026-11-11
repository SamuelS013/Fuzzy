import customtkinter as ctk
import tkinter.font as tkfont

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("light")  # "light" o "dark"
ctk.set_default_color_theme("blue")

# Crear ventana principal
root = ctk.CTk()
root.title("Lista de fuentes disponibles")
root.geometry("500x400")

# Obtener y ordenar las fuentes del sistema
fuentes = sorted(tkfont.families())

# Crear un cuadro de texto para mostrar las fuentes
textbox = ctk.CTkTextbox(root, width=480, height=350)
textbox.pack(pady=10)

# Insertar las fuentes en el cuadro de texto
for fuente in fuentes:
    textbox.insert("end", fuente + "\n")

# Deshabilitar edición para que sea solo lectura
textbox.configure(state="disabled")

root.mainloop()
