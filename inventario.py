from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Inventario(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.pack()
        self.widgets()

    def widgets(self):

        frame1 = tk.Frame(self, bg= "#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="INVENTARIO", bg= "#dddddd", font="sans 30 bold", anchor="center")
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, height=90)


        frame2 = tk.Frame(self, bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)

        labelframe= tk.LabelFrame(frame2, text="Productos", font="sans 22 bold", bg="#C6D9E3") 
        labelframe.place(x=20, y=30, width=400, height=500)

        lblnombre = tk.Label(labelframe, text="Nombre: ", font="sans 14 bold", bg="#C6D9E3")
        lblnombre.place(x=10, y=20)
        self.nombre = ttk.Entry(labelframe, font="sans 14 bold")
        self.nombre.place(x=140, y=20, width=240, height=40)

        lblproveedor = tk.Label(labelframe, text="Proveedor: ", font="sans 14 bold", bg="#C6D9E3")
        lblproveedor.place(x=10, y=80)
        self.proveedor = ttk.Entry(labelframe, font="sans 14 bold")
        self.proveedor.place(x=140, y=80, width=240, height=40)

        lblprecio = tk.Label(labelframe, text="Precio: ", font="sans 14 bold", bg="#C6D9E3")
        lblprecio.place(x=10, y=140)
        self.precio = ttk.Entry(labelframe, font="sans 14 bold")
        self.precio.place(x=140, y=140, width=240, height=40)

        lblcosto = tk.Label(labelframe, text="Costo: ", font="sans 14 bold", bg="#C6D9E3")
        lblcosto.place(x=10, y=200)
        self.costo = ttk.Entry(labelframe, font="sans 14 bold")
        self.costo.place(x=140, y=200, width=240, height=40)

        lblstock = tk.Label(labelframe, text="Stock: ", font="sans 14 bold", bg="#C6D9E3")
        lblstock.place(x=10, y=260)
        self.stock = ttk.Entry(labelframe, font="sans 14 bold")
        self.stock.place(x=140, y=260, width=240, height=40)

        boton_agregar = tk.Button(labelframe, text="Ingresar", font="sans 14 bold", bg='#dddddd')
        boton_agregar.place(x=80, y=340, width=240, height=40)

        boton_editar = tk.Button(labelframe, text="Editar", font="sans 14 bold", bg='#dddddd')
        boton_editar.place(x=80, y=400, width=240, height=40)

        #TABLA
        treframe = tk.Frame(frame2, bg="White")
        treframe.place(x=440, y=50, width=620, height=400)

        scroll_y = ttk.Scrollbar(treframe)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x = ttk.Scrollbar(treframe, orient=HORIZONTAL)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tre = ttk.Treeview(treframe, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set, height=40,
                                columns=("ID", "PRODUCTO", "PROVEEDOR", "PRECIO", "COSTO", "STOCK"), show="headings")
        self.tre.pack(expand=True, fill=tk.BOTH)
        
        scroll_y.config(command=self.tre.yview)
        scroll_x.config(command=self.tre.xview)

        self.tre.heading("ID", text="id")
        self.tre.heading("PRODUCTO", text="Producto")
        self.tre.heading("PROVEEDOR", text="Proveedor")
        self.tre.heading("PRECIO", text="Precio")
        self.tre.heading("COSTO", text="Costo")
        self.tre.heading("STOCK", text="Stock")

        self.tre.column("ID", width=70, anchor="center")
        self.tre.column("PRODUCTO", width=100, anchor="center")
        self.tre.column("PROVEEDOR", width=100, anchor="center")
        self.tre.column("PRECIO", width=70, anchor="center")
        self.tre.column("COSTO", width=100, anchor="center")
        self.tre.column("STOCK", width=100, anchor="center")