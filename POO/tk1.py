from _tkinter import *
from re import X
import tkinter
class interfaz:
    def __init__(self,contenedor):
        self.e1=tkinter.Label(contenedor,text="etiqueta 1", fg="black", bg="white")
        self.e2=tkinter.Label(contenedor,text="etiqueta 1", fg="black", bg="white")
        self.e3=tkinter.Label(contenedor,text="etiqueta 1", fg="black", bg="white")
        self.e1.pack(side=tkinter.TOP)
        self.e2.pack(side=tkinter.RIGHT)
        self.e3.pack(side=tkinter.BOTTOM,fill=X)
        
        ventana=tkinter.Tk()
        miinterfaz=miinterfaz(ventana)
        ventana.mainloop()