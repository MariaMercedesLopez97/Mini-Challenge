#Pide al usario que ingrese el numero que sea saber
numero = int(input("Ingrese el numero que seas saber de la tabla de multiplicar:"))
print(f"Tabla de multiplicar del {numero}:") 
# Generar la tabla de multiplicar usando un bucle for
for i in range(1, 11): 
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")





