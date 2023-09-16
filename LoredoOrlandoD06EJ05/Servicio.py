"""
Created on Wed Sep 13 17:38:10 2023

@author: orlando
"""
import sys
import os
import subprocess
import psutil
import time 

def check_arguments():
    if len(sys.argv) == 1:
    	print('Este programa no funciona sin argumentos')
    	sys.exit(0)

def get_targets():
    targets = sys.argv[1:]
    i = 0
    while i < len(targets):
    	if not targets[i].endswith('.exe'):
    		targets[i] = targets[i] + '.exe'
    	i += 1
    return targets

def lock(target):
    j = 0
    h = 0
    respuesta = ' '
    for proc in psutil.process_iter():
        #Caso donde el programa solicitado se esta ejecutando
        if proc.name().lower() == target.lower():    
            j += 1
            for proc in psutil.process_iter():
                  #Caso donde blender se esta ejecutando
                  if proc.name().lower() == 'blender.exe':
                      h += 1
                      if h == 1: 
                          print(targets, "y blender se estan ejecutando")
                          respuesta = input('Deseas cerrar blender S/N: ')
                          #El programa se cerrará
                          if respuesta == "S":
                              proc.kill()
                              print("Blender se cerró")   
                          #El programa se ejecutará
                          if respuesta == "N":
                              print("Blender seguirá activado")  
            #Caso donde nuestro programa se esta ejecutando pero blender no
            if h == 0:
                h += 2
                print(targets, "se está ejcutando pero blender no")
                respuesta = input('Deseas abrir blender S/N: ')
                #El programa se ejecutará
                if respuesta == "S":
                    print("Blender se ejecutará")
                    subprocess.run(r"E:\Orlando\Programas\Blender\blender.exe")
                #El programa no se ejecutará
                if respuesta == "N":
                    print("Blender seguirá desactivado")          
    #Caso donde el programa ni blender se estan ejecutando   
    if j == 0:
        print(targets, "ni blender se estan ejecutando")
            
if __name__ == '__main__':
    check_arguments()
    targets = get_targets()
    while True:
        for target in targets:
    	    lock(target)
        print("########################################################")
        time.sleep(25) #25 segundos para testear
        #time.sleep(300) #5 minutos para el programa