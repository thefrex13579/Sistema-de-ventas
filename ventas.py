from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Ventas(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):

        frame1 = tk.Frame(self, bg= "#dddddd", highlightbackground= "gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="VENTAS", bg= "#dddddd", font="sans 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, height=90)

        frame2 = tk.Frame(self, bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)
        
        lblframe = LabelFrame(frame2, text="Informacion de la venta", bg="#C6D9E3", font="sans 16 bold")
        lblframe.place(x=10, y=10, width=1060, height=80)

        label_numero_factura = tk.Label(lblframe, text="Numero de \nfactura", bg="#C6D9E3", font="sans 12 bold")
        label_numero_factura.place(x=10, y=5)

        self.numero_factura = tk.StringVar()

        self.entry_numero_factura = ttk.Entry(lblframe, textvariable=self.numero_factura, state="readonly", font="sans 12 bold")
        self.entry_numero_factura.place(x=100, y=5, width=80)