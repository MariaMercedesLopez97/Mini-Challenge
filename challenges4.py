#DIA 4
#Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.
def ordenar_lista():
    lista = []
    cantidad = int(input("Ingrese el numero:"))
    for i  in range(cantidad):
        num = int(input(f"Ingrese el numero {i + 1}:"))
        lista.append(num)
        lista.sort() #Se uliza para ordenar de forma automaticamente de forma ascendente
    print("La lista ordenada es:", lista)
ordenar_lista()
        

