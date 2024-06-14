#DIA 3
#Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.
def vocales():
    contador = 0
    cadena = input("Ingrese una palabra o frase:")
    for letra in cadena:
        if letra in ["a","e","i","o","u"]:
            contador = contador +1  
            print(contador)

vocales()

