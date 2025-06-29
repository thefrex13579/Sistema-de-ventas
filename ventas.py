from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Ventas(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

    def widgets(self):

        frame1 = tk.Frame(bg= "#dddddd")
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)
        
