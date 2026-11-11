from .home import HomePage
from .settings import SettingsPage
from .download import DownloadPage
# Página inicial al arrancar la app
START_PAGE = "home"

# Lista de todas las páginas registradas.
# Para añadir una nueva vista, solo la agregas aquí.
PAGES = (
    HomePage,
    SettingsPage,
    DownloadPage,
)