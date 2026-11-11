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

class DownloadPage(BasePage):
    name = "download"

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Atributos de estado que no son widgets (datos, banderas, etc.)
        self.usuario_actual = None
        self.filtro = "todos"
        self.var_nombre = ctk.StringVar(value="Cargando...")
        self.var_fuente = ctk.StringVar(value="Cargando...")
        self.var_calidad = ctk.StringVar(value="Cargando...")

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
            text="Stitch",
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

        self.info_descarga_container = ctk.CTkFrame(master=self, fg_color=(colorBlanco, colorNegro), corner_radius=0)
        self.info_descarga_container.pack(fill="both", expand=True, side="bottom")

        ctk.CTkLabel(
            master=self.info_descarga_container,
            text="RESULTADOS DE TU ENLACE:",
            font=("Arial", 15, "bold"),
            fg_color=(colorBlanco, colorNegro),
            justify="left",
            anchor="w"

        ).pack(pady=(10, 15), padx=(40, 0), fill="x")
        ##
        self.info_grid = ctk.CTkFrame(
            master=self.info_descarga_container,
            fg_color=(colorBlanco, colorNegro),
            corner_radius=0
        )
        self.info_grid.pack(fill="x", side="bottom", expand=True, pady=(0,30))

        self.info_caratula = ctk.CTkLabel(
            master=self.info_grid,
            image=src.img_youtube,
            text="",
            width=100,
            height=100,
            fg_color=colorFondoTarjetas,
            corner_radius=10
        )
        self.info_caratula.grid(column=0, row=0, rowspan=3, padx=(60, 40))

        self.info_nombre = ctk.CTkLabel(
            master=self.info_grid,
            text="Titulo:",
            font=("Arial", 15, "bold"),
            text_color=(colorNegro, colorBlanco),
            anchor="e",
            justify="left"
        )
        self.info_nombre.grid(column=1, row=0, pady=3)

        self.nombre = ctk.CTkLabel(
            master=self.info_grid,
            textvariable=self.var_nombre,
            font=("Arial", 15, "normal"),
            text_color=(colorNegro, colorBlanco),
            anchor="e",
            justify="left"
        )
        self.nombre.grid(column=2, row=0, padx=3, pady=3)


        self.info_fuente = ctk.CTkLabel(
            master=self.info_grid,
            text="Fuente:",
            font=("Arial", 15, "bold"),
            text_color=(colorNegro, colorBlanco),
            anchor="e",
            justify="left"
        )
        self.info_fuente.grid(column=1, row=1, pady=3)

        
        self.fuente = ctk.CTkLabel(
            master=self.info_grid,
            textvariable=self.var_fuente,
            font=("Arial", 15, "normal"),
            text_color=(colorNegro, colorBlanco),
            anchor="e",
            justify="left"
        )
        self.fuente.grid(column=2, row=1, padx=3, pady=3)


        self.info_calidad = ctk.CTkLabel(
            master=self.info_grid,
            text="Calidad:",
            font=("Arial", 15, "bold"),
            text_color=(colorNegro, colorBlanco),
            anchor="e",
            justify="left"
        )
        self.info_calidad.grid(column=1, row=2, pady=3)

        
        self.calidad = ctk.CTkLabel(
            master=self.info_grid,
            textvariable=self.var_calidad,
            font=("Arial", 15, "normal"),
            text_color=(colorNegro, colorBlanco),
            anchor="e",
            justify="left"
        )
        self.calidad.grid(column=2, row=2, padx=3, pady=3)

    def _conectar_eventos(self):
        self.boton_back.configure(command=lambda: self.controller.show_page("home"))