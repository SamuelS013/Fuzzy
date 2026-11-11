import customtkinter as ctk
from PIL import Image

### BRAND
img_logo = ctk.CTkImage(light_image=Image.open("./src/icon/logo.png"), size=(80, 80))
img_settings = ctk.CTkImage(light_image=Image.open("./src/icon/settings.png"), size=(25, 25))
img_back = ctk.CTkImage(light_image=Image.open("./src/icon/back.png"), size=(25, 25))

### FOOTER
img_instagram = ctk.CTkImage(light_image=Image.open("./src/icon/instagram.png"), size=(50, 50))
img_facebook = ctk.CTkImage(light_image=Image.open("./src/icon/facebook.png"), size=(50, 50))
img_youtube = ctk.CTkImage(light_image=Image.open("./src/icon/youtube.png"), size=(50, 50))
img_tiktok = ctk.CTkImage(light_image=Image.open("./src/icon/tiktok.png"), size=(50, 50))
img_twitter = ctk.CTkImage(light_image=Image.open("./src/icon/x.png"), size=(50, 50))
