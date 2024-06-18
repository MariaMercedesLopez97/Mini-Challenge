#DIA 6
#Conversión de Temperatura: Escribe un programa que convierta una temperatura dada en grados Celsius a
#  grados Fahrenheit.

def temperatura(celsius):
    #Formula para convertir Celsius a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#Solicitar al usuario la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

#Realizar la conversion
fahrenheit = temperatura(celsius)

#Mostrar el resultado
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")
