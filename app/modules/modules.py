import yt_dlp
import customtkinter as ctk

def text_boton(activate):

    texto = ""

    if activate == True:
        texto = ctk.StringVar(value="PROCESANDO")
    else:
        texto = ctk.StringVar(value="ENVIAR")

    return texto

def dowld_maximaDefinicion(url):

    url = url

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
