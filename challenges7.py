#DIA 7
#Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra,
#papel o tijeras contra la computadora.

import random # para que la eleccion sea aleatorio.
import time # para que el programa espere un poco antes de mostrar el resultado.

#Opciones a elegir
opciones = ["piedra", "papel", "tijeras"]# Define una lista con las opciones posibles en el juego: piedra, papel y tijeras.

#Funciona para obtener la  opcion de usuario
def obtener_opcion_usuario(): #Define una función llamada 
    elegir = input("Elige piedra, papel o tijeras:").lower() #Solicita al usuario que elija una opción y convierte la entrada a minúsculas.
    while elegir not in opciones: #Si la elección del usuario no está en la lista opciones, se ejecuta un bucle.
        elegir = input("Elija una opción válida (piedra, papel o tijeras:").lower()#Pide al usuario que ingrese una opción válida.
        return elegir #Devuelve la elección válida del usuario.
    
#Funcion para obtener la opcion de la computadora
def obtener_opcion_computadora(): #Define una función llamada
    return random.choice(opciones) #Selecciona aleatoriamente una opción de la lista opciones y la devuelve.

#Funcion para definir el ganador
def definir_ganador(usuario, computadora):
    #Define una función llamada definir_ganador que toma dos parámetros: usuario y computadora.
    if usuario == computadora: #Si la elección del usuario es igual a la de la computadora, es un empate.
        return "Empate"
    #Evalúa si el usuario gana. Gana si:
    elif (usuario == "piedra" and computadora == "tijeras") or \
        (usuario == "papel" and computadora == "piedra") or \
        (usuario == "tijeras" and computadora == "papel"):

        return "Ganaste"
    else: #Si no es empate y el usuario no gana, la computadora gana.
        return "Perdiste"
#Devuelve el resultado del juego según las condiciones evaluadas.

#Funcion principal para jugar 
def jugar(): #Define una función llamada jugar
    usuario = obtener_opcion_usuario() #Llama a la función obtener_opcion_usuario y almacena el resultado en la variable usuario
    computadora = obtener_opcion_computadora() #Llama a la función obtener_opcion_computadora y almacena el resultado en la variable computadora.
    print("Computadora está pensando...") # Imprime un mensaje indicando que la computadora está "pensando".
    time.sleep(2) #Pausa la ejecución del programa durante 2 segundos.
    print(f"Computadora elige: {computadora}") # Imprime la elección de la computadora.
    print(definir_ganador(usuario, computadora))# Llama a la función definir_ganador con las elecciones del usuario y la computadora, e imprime el resultado del juego.

#Ejecutar el juego
if __name__=="__main__":
#Esta línea asegura que el código dentro de este bloque solo se ejecutará si el archivo es ejecutado directamente,
#  no si es importado como un módulo en otro script.
    jugar()# Llama a la función jugar para iniciar el juego.