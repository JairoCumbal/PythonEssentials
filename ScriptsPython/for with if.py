# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:21:26 2023

@author: Client
"""

lista=["R1","R2","R3",
       "S1","S2","S3"] #Declaro una lista
print(len(lista)) #Impresión del tamaño de la lista

for item in lista:
    if "S" in item:
        print(item,end=" * ") #Mediante for se imprime las posiciones de la lista que contengan la letra S y se termina con un dato string