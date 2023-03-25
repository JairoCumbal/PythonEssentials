# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:09:58 2023

@author: Client
"""

try:
    y=1/0
except ArithmeticError:
    print("Problema aritmético!")
except ZeroDivisionError:
    print("División por cero!")
print("Fin del código")