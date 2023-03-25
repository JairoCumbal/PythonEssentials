# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:21:21 2023

@author: Client
"""

def multi(num1,num2): #Definición de función con dos parámetros
    print("El resultado de multiplicar ",
          num1," * ",num2,
          " es: ",num1*num2) #Se multiplican los parámetros y se imprime el resultado
    return (num1*num2) #Función retorna un valor
multi(50, num2=6) #Formas de importar parámetros
multi(num1=15, num2=6) #Formas de importar parámetros
multi(4,5) #Formas de importar parámetros
resultado=multi(4,3)#Asignación del valor retornado por la función a la variable resultado
opt=resultado*1.12 #Operación con la variable resultado y se asigna a la variable opt
print(opt) #Impresión de la variable opt