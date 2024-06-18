#DIA 5
#Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas:
#  una de claves y otra de valores.

#Cree dos listas claves y valores
claves = ["nombre", "edad", "ciudad"]
valores = ["Maria", 26, "Iturbe-Guaira"]

#Crear un diccionario vacio
diccionario = ""

#Recorrer las listas y agregar al diccionario
for i in range(len(claves)):
    diccionario = dict(zip(claves, valores))
#Imprimir 
print (diccionario)
