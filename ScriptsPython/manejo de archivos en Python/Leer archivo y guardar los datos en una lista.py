# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:14:46 2023

@author: Client
"""
#Declaro una lista
lista=[]
#Abrir archivo
archivo=open("devices.txt")
for item in archivo:
    #Quitar saltos de línea
    item=item.strip()
    #Agregar los datos del archivo a la lista
    lista.append(item)
    print(item)
#Cerrar archivo
archivo.close=()