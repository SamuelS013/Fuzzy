import customtkinter as ctk

from pages import PAGES, START_PAGE


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Stitch App")
        self.geometry("750x550")
        self.resizable(False, False)

        # Contenedor donde se apilan todas las páginas
        self.container = ctk.CTkFrame(
            master=self,
            fg_color="transparent",
            corner_radius=0,
            border_width=0
        )
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # ────────── LLENADO DEL DICCIONARIO ──────────
        self.pages: dict[str, ctk.CTkFrame] = {}

        for PageClass in PAGES:
            page = PageClass(parent=self.container, controller=self)
            self.pages[PageClass.name] = page        # clave = atributo 'name'
            page.grid(row=0, column=0, sticky="nsew")  # todas apiladas en (0,0)
        # ─────────────────────────────────────────────

        # Estado inicial
        self.current_page: str | None = None
        self.show_page(START_PAGE)

    def show_page(self, page_name: str):
        """Cambia el estado visible de la app."""
        if page_name not in self.pages:
            raise ValueError(f"Página desconocida: {page_name!r}. "
                             f"Disponibles: {list(self.pages)}")

        page = self.pages[page_name]
        page.tkraise()          # trae al frente sin destruir
        page.on_show()          # hook para refrescar datos
        self.current_page = page_name


if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    App().mainloop()