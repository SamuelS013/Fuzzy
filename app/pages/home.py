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

class HomePage(BasePage):
    name = "home"

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Atributos de estado que no son widgets (datos, banderas, etc.)
        self.usuario_actual = None
        self.filtro = "todos"
        self.texto_boton = ctk.StringVar(value="Enviar")

        # Construcción de la UI, en orden
        self._crear_header()
        self._crear_main()
        self._crear_footer()

        # Conexión de eventos
        self._conectar_eventos()

    def _crear_header(self):     
        ### <header>
        self.header = ctk.CTkFrame(master=self, fg_color=colorPricipal, corner_radius=0)
        self.header.pack(fill="both", expand=True)

        self.header_nav = ctk.CTkFrame(master=self.header, fg_color=colorPricipal, corner_radius=0)
        self.header_nav.pack(fill="x")

        self.boton_config = ctk.CTkButton(
            master=self.header_nav,
            image=src.img_settings,
            text="",
            height=30,
            width=30,
            fg_color=colorPricipal,
            hover_color=colorSecundario,

        )
        self.boton_config.pack(pady=(15,0), padx=15, side="right")

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

        self.entry_container = ctk.CTkFrame(master=self.main, corner_radius=0, fg_color=(colorBlanco, colorNegro))
        self.entry_container.pack(side="top", pady=10)

        ctk.CTkLabel(
            master=self.entry_container,
            text="Ingresa o pega tu enlace aquí",
            font=("Arial", 18, "normal"),
            justify="center",
            text_color=(colorNegro, colorBlanco),
        ).pack(side="top", pady=(0, 5))

        self.entrada_url_entry = ctk.CTkEntry(
            master=self.entry_container,
            placeholder_text="https://ruta-de-ejemplo/a-tu-archivo...",
            font=("Arial", 18, "normal"),
            width=280,
            border_width=1,
            border_color=(colorPricipal, colorBlanco),
        )
        self.entrada_url_entry.pack(pady=(0, 5))

        self.boton_enviar = ctk.CTkButton(
            master=self.entry_container,
            textvariable=self.texto_boton,
            font=("Arial", 15, "bold"),
            text_color=(colorNegro, colorBlanco),
            fg_color=colorPricipal,
            hover_color=colorSecundario,
            corner_radius=12,
        )
        self.boton_enviar.pack(pady=(8, 10), side="bottom")


    def _crear_footer(self):
                
        ### <footer>
        self.footer = ctk.CTkFrame(master=self, fg_color=(colorBlanco, colorNegro), corner_radius=0)
        self.footer.pack(fill="both", expand=True, side="bottom")

        ctk.CTkLabel(
            master=self.footer,
            text="PLATAFORMAS POPULARES",
            font=("Arial", 15, "bold"),
            fg_color=(colorBlanco, colorNegro),
            justify="left",
            anchor="w"

        ).pack(pady=(10, 15), padx=(40, 0), fill="x")
        ##
        self.footer_grid = ctk.CTkFrame(
            master=self.footer,
            fg_color=(colorBlanco, colorNegro),
            corner_radius=0
        )
        self.footer_grid.pack(fill="x", side="bottom", expand=True, pady=(0,30))

        self.tarjeta_footer_uno = ctk.CTkLabel(
            master=self.footer_grid,
            image=src.img_youtube,
            text="",
            font=("Arial", 10, "normal"),
            width=100,
            height=100,
            fg_color=colorFondoTarjetas,
            corner_radius=10
        )
        self.tarjeta_footer_uno.grid(column=0, row=0, padx=(60, 60))

        self.tarjeta_footer_dos = ctk.CTkLabel(
            master=self.footer_grid,
            image=src.img_instagram,
            text="",
            font=("Arial", 10, "normal"),
            width=100,
            height=100,
            fg_color=colorFondoTarjetas,
            corner_radius=10
        )
        self.tarjeta_footer_dos.grid(column=1, row=0, padx=(0, 60))

        self.tarjeta_footer_tres = ctk.CTkLabel(
            master=self.footer_grid,
            image=src.img_facebook,
            text="",
            font=("Arial", 10, "normal"),
            width=100,
            height=100,
            fg_color=colorFondoTarjetas,
            corner_radius=10
        )
        self.tarjeta_footer_tres.grid(column=2, row=0, padx=(0, 60))


        self.tarjeta_footer_cuatro = ctk.CTkLabel(
            master=self.footer_grid,
            image=src.img_tiktok,
            text="",
            font=("Arial", 10, "normal"),
            width=100,
            height=100,
            fg_color=colorFondoTarjetas,
            corner_radius=10
        )
        self.tarjeta_footer_cuatro.grid(column=3, row=0, padx=(0, 60))

    def _on_nav_download(self):
        self.controller.show_page("download")

    def _on_nav_settings(self):
        self.controller.show_page("settings")

    def descargar(self):
        url = self.entrada_url_entry.get()
        module.dowld_maximaDefinicion(url)
        print("Descarga exitosa!")

    def boton_activate(self):
        self._on_nav_download()
        self.descargar()

    def _conectar_eventos(self):
        self.boton_enviar.configure(command=self.boton_activate)
        self.boton_config.configure(command=self._on_nav_settings)

