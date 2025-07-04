from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#C6D9E3")

        self.widgets()

    def show_frame(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False, False)

        top_level.transient(self.master)
        top_level.grab_set()
        top_level.focus_set()
        top_level.lift()


    def ventas(self):
        self.show_frame(Ventas)

    def inventario(self):
        self.show_frame(Inventario)

    def widgets(self):
        frame1 = tk.Frame(self, bg="#C6D9E3")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)

        btnventas = tk.Button(frame1, bg="#f4b400", fg="white", font= "sans 18 bold", text="Ir a ventas", command= self.ventas)
        btnventas.place(x=500, y=30, width=240, height=60)

        btninventario = tk.Button(frame1, bg="#c62e26", fg="white", font="sans 18 bold", text="Ir a inventario", command= self.inventario)
        btninventario.place(x=500, y=130, width=240, height=60)

        self.logo_image = Image.open("imagenes/registradora.png")
        self.logo_image = self.logo_image.resize((320,320))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C6D9E3")
        self.logo_label.place(x=100, y=30)

        copyright_label = tk.Label(frame1, text="@ 2025 Anamarshop. Derechos reservados", font="sans 12 bold", bg="#C6D9E3", fg="gray")
        copyright_label.place(x=180, y=350)