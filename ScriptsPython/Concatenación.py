# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 18:13:45 2023

@author: Client
"""

#Concatenación

x=5
str1="Python"
str2="Essentials"
space=" "
print(str1+space+str2)
#print(str1+space+str2+x+space+x)  #No se puede concatenar con un entero
print(str1+space+str2+space+str(x)) #Uso de función de conversión para imprimir varibale x