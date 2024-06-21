#DIA 8
#Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de
#  longitud variable (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas,
#  números y símbolos.
import random #proporciona funciones para generar números aleatorios.

def contraseña_segura(longitud):
# Define una función llamada generar_contraseña_segura que toma un argumento longitud, que representa la longitud deseada de la contraseña
    
    if longitud < 8 or longitud > 16: #Comprueba si la longitud proporcionada es menor que 8 o mayor que 16.
        return False, "La contraseña debe tener entre 8 y 16 caracteres" #Si la longitud no está en el rango permitido, la función devuelve un mensaje de error y termina su ejecución.
    #Define una lista llamada conjuntos que contiene cuatro cadenas de caracteres:
    conjuntos = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", #Letras mayusculas
            "abcdefghijklmnopqrstuvwxyz", #Letras minusculas
            "0123456789", # Digitos
            "!@#$%^&*()_+-=[]{}|;:',.<>/?"] #Simbolos

    contraseña = "" #Inicializa una cadena vacía llamada contraseña que se irá llenando con los caracteres generados.

    while longitud > 0: #Inicia un bucle while que continuará ejecutándose mientras longitud sea mayor que 0.
        tipo_caracter = random.randint(1, len(conjuntos))
#Genera un número entero aleatorio entre 1 y la longitud de la lista conjuntos (que es 4).
#  Este número determinará cuál conjunto de caracteres se seleccionará.
        conjunto_seleccionado = conjuntos[tipo_caracter - 1]
#Selecciona uno de los conjuntos de caracteres basado en el número aleatorio generado.
#  tipo_caracter - 1 se usa porque los índices de lista en Python comienzan en 0.
        indice = random.randint(0, len(conjunto_seleccionado) - 1)
#Genera un número entero aleatorio entre 0 y la longitud del conjunto_seleccionado menos 1. 
# Este número determinará qué carácter específico se seleccionará del conjunto.        
        contraseña += conjunto_seleccionado[indice]
#Añade el carácter seleccionado a la variable contraseña.      
        longitud -= 1
#Decrementa la longitud en 1. Esto asegura que el bucle se ejecutará exactamente el número de veces especificado
#  originalmente por longitud.
    return contraseña #Cuando el bucle termina (cuando longitud llega a 0), la función devuelve la contraseña
    #generada.
print(f"La contraseña segura es:") # Muestra el mensaje "La contraseña segura es:"
print(contraseña_segura(12)) #Llama a la función generar_contraseña_segura con una longitud de 12 y imprime
#la contraseña generada.

    



