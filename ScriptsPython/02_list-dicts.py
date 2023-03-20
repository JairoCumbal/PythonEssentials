# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3
 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary

#Ejercicio 1


print(country) #Impresión de la lista country
print("\n") #Impresión de salto de línea

#s=", " #Asigno un string a una variable
#print("Países: "+country[0]+s+country[1]+s+country[2]+s+country[3]+s+country[4]) #Imprimo los países concatenando con un string y la variable s 

#Ejercicio 2

print(capitals) #Impresión del diccionario capitals
print("\n") #Impresión de salto de línea

#sa=capitals["South Africa"] #Asigno a la variable sa la lista South Africa almacenada en el diccionario capitals
#print("Ciudades: "+capitals["Brazil"]+s+capitals["Russia"]+s+capitals["India"]+s+capitals["China"]+s+sa[0]+s+sa[1]+s+sa[2]) #Imprimo el diccionario capitals y la lista sa declarada, concateno con un string y la variable s

"""
What response did you get?
Why did the list and dictionary
 contents not print?
Fix the code and run the script again.
"""

#Ejercicio 3

print( capitals["South Africa"][1] ) #Impresión de la capital Cape Town


#print("Sudáfrica - pos. 1: "+sa[1]) #Imprimo el índice 1 de la lista South Africa previamente asignada en variable sa y concateno con un string

"""
Why did you get an error for the
 2nd capital of South Africa?
Hint: Check the syntax for the 
index value.
"""
