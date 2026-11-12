import customtkinter as ctk
from .base_page import BasePage
from modules import modules as module
from modules import resources as src


colorPricipal = "#2D3A3A"
colorSecundario = "#248232"
colorNegro = "#232323"
colorBlanco = "#FEFEFE"
colorFondo =  "#2B3737"
colorFondoTarjetas = "#292929"
activate = False

class SettingsPage(BasePage):
    name = "settings"

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Atributos de estado que no son widgets (datos, banderas, etc.)
        self.usuario_actual = None
        self.filtro = "todos"
        self.texto_boton = ctk.StringVar(value="Enviar")

        # Construcción de la UI, en orden
        self._crear_header()
        self._crear_main()

        # Conexión de eventos
        self._conectar_eventos()

    def _crear_header(self):     
        ### <header>
        self.header = ctk.CTkFrame(master=self, fg_color=colorPricipal, corner_radius=0)
        self.header.pack(fill="both", expand=True)

        self.header_nav = ctk.CTkFrame(master=self.header, fg_color=colorPricipal, corner_radius=0)
        self.header_nav.pack(fill="x")

        self.boton_back = ctk.CTkButton(
            master=self.header_nav,
            image=src.img_back,
            text="",
            height=30,
            width=30,
            fg_color=colorPricipal,
            hover_color=colorSecundario,
        )
        self.boton_back.pack(pady=(15,0), padx=15, side="right")

        self.logo_brand = ctk.CTkLabel(
            master=self.header,
            text="",
            image=src.img_logo,
            fg_color=colorFondo,
            width=90,
            height=100,
            corner_radius=12
        )
        self.logo_brand.pack()

        self.text_brand_frame = ctk.CTkFrame(master=self.header, fg_color=colorPricipal, corner_radius=None)
        self.text_brand_frame.pack()

        self.text_brand_titulo = ctk.CTkLabel(
            master=self.text_brand_frame,
            text="Fuzzy",
            font=("Arial", 25, "bold"),
            fg_color=colorPricipal,
            text_color=colorBlanco
        )
        self.text_brand_titulo.pack(pady=(15,8), side="top")


        self.text_brand_subtitulo = ctk.CTkLabel(
            master=self.text_brand_frame,
            text="Descargador de contenido multimedia con un clic",
            font=("Arial", 15, "normal"),
            fg_color=colorPricipal,
            text_color=colorBlanco
        )
        self.text_brand_subtitulo.pack(pady=(0,10), side="bottom")


    def _crear_main(self):
        ### <main>
        self.main = ctk.CTkFrame(master=self, fg_color=(colorBlanco, colorNegro))
        self.main.pack(fill="both", expand=True)

        ctk.CTkLabel(
            master=self.main,
            text="Configuraciones",
            font=("Arial", 20, "bold"),
            justify="center",
            text_color=(colorNegro, colorBlanco),
        ).pack(side="top", pady=(25, 10))

        self.config_grid = ctk.CTkFrame(master=self.main, fg_color=(colorBlanco, colorNegro), corner_radius=0)
        self.config_grid.pack(fill="both", expand=True)

        self.modoOscuro_text = ctk.CTkLabel(
            master=self.config_grid,
            text="Modo oscuro",
            font=("Arial", 20, "normal"),
            text_color=(colorNegro, colorBlanco)
        )
        self.modoOscuro_text.grid(column=0, row=0, pady=10, padx=(60, 0))

        self.modoOscuro_switch = ctk.CTkSwitch(
            master=self.config_grid,
            progress_color=colorSecundario,
            button_color=colorFondo,
            button_hover_color=colorSecundario,
            text="",
            switch_width=40,
            switch_height=22,
            width=40,
            height=22,
            onvalue=True,
            offvalue=False
        )
        self.modoOscuro_switch.grid(column=1, row=0, pady=10, padx=(15, 50))

    def _conectar_eventos(self):
        self.boton_back.configure(command=lambda: self.controller.show_page("home"))