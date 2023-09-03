# -*- coding: utf-8 -*-
"""
@author: Orlando
"""

from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import tkinter
import contextlib
import io
from tkinter import font
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import *
from tkinter import ttk
import os

global alt 
alt = 240
global b
b = 0

ventana = tkinter.Tk()
ventana.title("Registro de usuario")
ventana.geometry("700x600+50+50")

image = tk.PhotoImage(file="portada2.png")
Ifon = ttk.Label(image=image)
Ifon.place(x = 0, y = 0) 

#####################################################

def verificacion():
    Boton.place_forget()
    with open("Respaldo.txt") as archivo:
        res = archivo.readline(1)
        
    if res == "1":
            respaldo()
    else:
            file = open("Respaldo.txt", "a")
            file.write("1" + "\n") 
            file.close()  
            pantalla()


########################################################

def respaldo():
    global alt, b
    with open("Respaldo.txt") as archivo:
        for linea in archivo:
           # print(linea) 
            if b == 1: 
                entry_c1.insert(tk.INSERT, linea)
            if b == 2: 
                entry_c2.insert(tk.INSERT, linea)
            if b == 3: 
                entry_c3.insert(tk.INSERT, linea)
            if b == 4: 
                entry_c4.insert(tk.INSERT, linea)
            alt = alt + 60
            b = b + 1
    alt = alt - 60
    b = b - 1
    file = open("Respaldo.txt", "a")
    file.write("") 
    pantalla()
    

def pantalla():
    label1.place(x=80, y=220)
    entry_c1.place(x=80, y=240)
    ##################################################
    label2.place(x=80, y=280)
    entry_c2.place(x=80, y=300)
    ##################################################
    label3.place(x=80, y=340)
    entry_c3.place(x=80, y=360)
    #####################################################
    label4.place(x=80, y=400)
    entry_c4.place(x=80, y=420)
    
    if b == 0:
        Boton1 = tkinter.Button(ventana, text="Guardar", command=lambda: datos(entry_c1.get()))
        Boton1.place(x = 200, y = alt)
    if b == 1: 
        Boton2 = tkinter.Button(ventana, text="Guardar", command=lambda: datos(entry_c2.get()))
        Boton2.place(x = 200, y = alt) 
    if b == 2: 
        Boton3 = tkinter.Button(ventana, text="Guardar", command=lambda: datos(entry_c3.get()))  
        Boton3.place(x = 200, y = alt) 
    if b == 3: 
        Boton4 = tkinter.Button(ventana, text="Guardar", command=lambda: datos(entry_c4.get()))
        Boton4.place(x = 200, y = alt)  
    if b == 4: 
        Boton5.place(x = 200, y = alt)
        
    def datos(n): 
        global alt, b
        alt = alt + 60
        b = b + 1
          
        file = open("Respaldo.txt", "a")
        file.write(n + "\n") 
        file.close()  
        
        if b == 1: 
            Boton1.place_forget()
            pantalla()
        if b == 2:
            Boton2.place_forget()  
            pantalla()
        if b == 3:  
            Boton3.place_forget()
            pantalla() 
        if b == 4: 
            Boton4.place_forget()
            Boton5.place(x = 200, y = alt)

            
def mostrar():
    global b
    b = 0
    print("Fin") 
    Boton5.place_forget()
    men = tkinter.Label(ventana, text="Datos del usuario")
    men.place(x = 350, y = 230)
    view = tk.Text(ventana, height = 15,  width = 25)  
    view.place(x=350, y=250)
    with open("Respaldo.txt") as archivo:
        for linea in archivo: 
                if b == 1: 
                    view.insert(tk.INSERT, "Nombre: " + linea + "\n")
                if b == 2: 
                    view.insert(tk.INSERT, "Correo: " + linea + "\n")
                if b == 3: 
                    view.insert(tk.INSERT,"CURP: " + linea + "\n")
                if b == 4: 
                     view.insert(tk.INSERT,"Telefono: " + linea + "\n")   
                b = b + 1
    file = open("Respaldo.txt", "w")
    file.write("") 
    
###Ventana principal#########################################################################
label1 = tkinter.Label(ventana, text="Nombre:")
entry_c1 = Entry(ventana)
entry_c1.focus()

########################################################
label2 = tkinter.Label(ventana, text="Correo:")
entry_c2 = Entry(ventana)
entry_c2.focus()

######################################################
label3 = tkinter.Label(ventana, text="CURP:")
entry_c3 = Entry(ventana)
entry_c3.focus()

#######################################################
label4 = tkinter.Label(ventana, text="Telefono:")
entry_c4 = Entry(ventana)
entry_c4.focus()

######################################################
Boton5 = tkinter.Button(ventana, text="Confirmar", command=lambda: mostrar())
Boton = tkinter.Button(ventana, text="Iniciar registro", font=("arial", 15), command=lambda: verificacion())
Boton.place(x = 260, y = 300) 

ventana.mainloop()