# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:40:13 2023

@author: Client
"""

#Uso de listas

lista=["1",2,3.7,False,"b"] #para declarar una lista va entre corchetes
print(type(lista))
print(lista[0]) #Impresión de la lista[posición 0]
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista[-5])
print(lista[-4])
print(lista[-3])
print(lista[-2])
print(lista[-1])
lista[1]="abc"
print(lista[1])
del lista[4] #para borrar un índice de la lista
#print(lista[-6]) no hay ese índice en la lista