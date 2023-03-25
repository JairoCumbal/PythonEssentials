# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:16:16 2023

@author: Client
"""
#Abrir archivo
archivo=open("devices.txt","a",1,encoding="utf-8")
while True:
    d=input("Ingrese un dato: ")
    if d=="exit":
        print("Todo hecho") 
        break
    else:
        archivo.write("\n"+d)
#Cerrar archivo
archivo.close=()       
"""for item in archivo:
    item=item.strip()
    print(item)"""

