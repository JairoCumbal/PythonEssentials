# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:47:17 2023

@author: Client
"""
while True:
    x=input("Ingrese un número: ")
    if x=="q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
            print(y)
            y=y+1
            if y>x:
                break
    