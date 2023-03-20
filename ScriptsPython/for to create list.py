# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:26:41 2023

@author: Client
"""
#Uso de for para crear una lista

lista2=[] #Declaro una variable lista2 de tipo lista
lista=["R1","R2","R3",
       "S1","S2","S3"] #Declaro una lista
print(len(lista)) #Impresión del tamaño de lista

for item in lista:
    if "S" in item:
        lista2.append(item) #Mediante for se va llenando lista2 con las posiciones de lista que contengan la letra S
        #print(lista2)
        #print(item,end=" * ") #Mediante for
print(lista2) #impresión de lista2