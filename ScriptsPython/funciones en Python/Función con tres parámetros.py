# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:47:54 2023

@author: Client
"""

def direccion(calle, ciudad, numCasa):
    print("Su dirección es:", calle, "Ciudad:", ciudad, "Casa N°:",numCasa)

d=input("Calle principal: ")
n=input("Número casa: ")
c=input("Ciudad: ")
print("\n")
direccion(d,c,n)