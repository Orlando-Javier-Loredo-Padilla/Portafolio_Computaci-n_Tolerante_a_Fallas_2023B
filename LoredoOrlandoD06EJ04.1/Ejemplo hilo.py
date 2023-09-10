# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 21:09:19 2023

@author: orlando
"""
import threading
import time

def primera_descarga(something):
    for i in range (0, 51):
        print("+Descarga en progreso:", i*2, "%")
        if i == 50: 
             print("+++++Descarga finalizada++++++++++ \n") 
        time.sleep(1) 

def segunda_descarga(something):
    for i in range (0, 26):
        print("-Actualización de datos: ",  i*4, "%")
        if i == 25: 
            print("-------Actualización finalizada--------\n")
        time.sleep(3) 

t = threading.Thread(target=primera_descarga, args=("hello",))
t2 = threading.Thread(target=segunda_descarga, args=("hello",))
print("Iniciando procesos \n")
t.start()
t2.start()  
for j in range (0, 11):
       print("/Subida de archivos: ", j*10, "%")
       if j == 10: 
         print("///////Archivo subido////////")  
       time.sleep(10)

t.join()
t2.join()
print("Procesos finalizados")