# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:18:10 2023

@author: Client
"""

#Uso de while

num_con=input("Ingrese el número al que debo contar: ") #Ingreso un dato string en variable num_con
num_con=int(num_con) #Convierto num_con a entero
contador=1 #Declaro una variable contador de tipo int
while (contador<=num_con): #Mientras contador sea menor que la variable ingresada se repetirá el ciclo
    print(contador) #Imprimo contador
    contador+=1 #Por cada ciclo contador irá aumentando en 1

