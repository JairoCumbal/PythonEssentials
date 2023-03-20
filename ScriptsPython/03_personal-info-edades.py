# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:43:06 2023

@author: Client
"""


nombre=input("Ingrese el nombre: ") #Ingreso de dato string
apellido=input("Ingrese el apellido: ") #Ingreso de dato string
direccion=input("Ingrese la direccion: ") #Ingreso de dato string
edad=int(input("Ingrese la edad: ")) #Ingreso de dato y conversión a entero
print("\n") #Impresión salto de línea
space=" " #Declaro una variable string
if edad>=0 and edad<=5: #Condición1
    print(nombre+space+apellido+space+"de"+space+str(edad)+space+"años"+space+"con domicilio en"
          +space+direccion+space+"está en la primera infancia") #impresión y concatenación para condición1
elif edad>=6 and edad<=11: #Condición2
    print(nombre+space+apellido+space+"de"+space+str(edad)+space+"años"+space+"con domicilio en"
          +space+direccion+space+"está en la infancia") #impresión y concatenación para condición2
elif edad>=12 and edad<=18: #Condición3
    print(nombre+space+apellido+space+"de"+space+str(edad)+space+"años"+space+"con domicilio en"
          +space+direccion+space+" está en la adolescencia") #impresión y concatenación para condición3
else: #Condición para falso
    print("Dato inválido") #Impresión para else



