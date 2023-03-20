# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:31:12 2023

@author: Client
"""

acl=int(input("Ingrese el # de ACL: ")) #Ingresar dato y convertir a entero
if acl>=1 and acl<=99: #Condición 1
    print("La ACL es estándar") #Impresión para condición1
elif acl>=100 and acl<=199:#Condición 2 (elif para añadir varias condiciones)
    print("La ACL es extendida") #Impresión para condición2
else: #Condición para falso
    print("El dato ingresado no es un ACL") #Impresión para else