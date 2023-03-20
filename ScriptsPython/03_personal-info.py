# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:31:31 2023

@author: Client
"""

nombre=input("Ingrese el nombre: ") #Ingresar nombre de tipo string
apellido=input("Ingrese el apellido: ") #Ingresar apellido de tipo string
direccion=input("Ingrese la direccion: ") #Ingresar direccion de tipo string
edad=int(input("Ingrese la edad: ")) #Ingresar edad y convertir a entero
email=input("Ingrese el email: ") #Ingresar email de tipo string
print("\n") #Imprimir salto de línea
space=" " #Declaro una variable de tipo string
print("El comprobante electrónico de "+nombre+space+apellido+space+"de"+space+str(edad)+space+"años"+space+"con domicilio en"
      +space+direccion+space+"ha sido enviado al correo"+space+email) #Impresión y concatenación de los datos ingresados