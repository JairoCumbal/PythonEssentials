# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:58:59 2023

@author: Client
"""
#Abrir archivo
archivo=open("devices.txt")
for item in archivo:
    item=item.strip()
    print(item)
#Cerrar archivo
archivo.close=()