# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:33:11 2023

@author: Client
"""

num_con=input("Ingrese el número al que debo contar: ") #ingreso un dato string
num_con=int(num_con) #Convierto a entero
contador=1 #Declaro una variable int
print("Antes del while") #Impresión de string
while (True): #Utlizo True para bucle infinito
    print(contador) #Imprimo la variable contador
    contador+=1 #Variable contador se incrementa en 1
    if contador>num_con: #Uso de condicional if
        #pass Usado para quitar errores de identación
        break #Para detener la ejecución de código
    print("dentro del bucle") #Impresión de string
print("fin del programa") #Impresión de string


"""
num_con=input("Ingrese el número al que debo contar: ")
num_con=int(num_con)
contador=1
print("Antes del while")
while (True):
    print(contador)
    contador+=1
    if contador>num_con:
        pass
    break
    print("dentro del bucle")
print("fin del programa")
"""