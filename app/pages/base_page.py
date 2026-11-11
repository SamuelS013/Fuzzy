import customtkinter as ctk


class BasePage(ctk.CTkFrame):
    """
    Clase base que heredan todas las páginas.
    Cada página recibe una referencia al 'controller' (la App)
    para poder pedir cambios de estado.
    """

    # Nombre único del estado. Cada subclase DEBE sobrescribirlo.
    name: str = "base"

    def __init__(self, parent, controller):
        super().__init__(
            parent,
            fg_color="transparent",
            corner_radius=0,
            border_width=0
        )
        self.controller = controller

    def on_show(self):
        pass