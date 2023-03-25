# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 19:58:22 2023

@author: Client
"""
#Se debe colocar el try siempre con al menos una excepción
try:
    x=int(input("Ingrese un número: "))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("No se puede dividir por cero")
except ValueError:
    print("Debes ingresar un número")
#Excepción sin nombre siempre irá al final
except:
    print("Algo no está bien")
print("Fin del código")