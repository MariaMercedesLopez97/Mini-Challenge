//DIA 10
//Ordenamiento de un Array: Escribir un programa que ordene un array de enteros utilizando ¡Pero hazlo en C++!

#include <iostream> // Incluye la biblioteca de entrada y salida estándar de C++.
using namespace std; // Utiliza el espacio de nombres estándar para evitar escribir std:: antes de cada objeto estándar.

void bubbleSort(int arr[], int n) {
    // Función que ordena un arreglo de enteros utilizando el algoritmo Bubble Sort.
    
    for (int i = 0; i < n-1; i++) {
        // Ciclo exterior para realizar n-1 pasadas a través del arreglo.
        
        for (int j = 0; j < n-i-1; j++) {
            // Ciclo interior para comparar y ordenar los elementos adyacentes.
            // En cada pasada, el mayor elemento se desplaza hacia el final.
            
            if (arr[j] > arr[j+1]) {
                // Si el elemento actual es mayor que el siguiente, se intercambian.
                
                int temp = arr[j]; // Guarda el valor de arr[j] en una variable temporal.
                arr[j] = arr[j+1]; // Asigna el valor de arr[j+1] a arr[j].
                arr[j+1] = temp; // Asigna el valor temporal a arr[j+1].
            }
        }
    }
}

void printArray(int arr[], int size) {
    // Función que imprime todos los elementos de un arreglo de enteros.
    
    for (int i = 0; i < size; i++)
        // Recorre todos los elementos del arreglo.
        cout << arr[i] << " "; // Imprime cada elemento seguido de un espacio.
    cout << endl; // Imprime una nueva línea al final de la impresión del arreglo.
}

int main() {
    // Función principal del programa.
    
    int arr[] = {20, 350, 80, 55, 67, 11, 32}; // Define e inicializa un arreglo de enteros.
    int n = sizeof(arr)/sizeof(arr[0]); // Calcula el número de elementos en el arreglo.
    
    cout << "Array original: \n"; // Imprime el mensaje "Array original:" seguido de una nueva línea.
    printArray(arr, n); // Llama a la función printArray para imprimir el arreglo original.
    
    bubbleSort(arr, n); // Llama a la función bubbleSort para ordenar el arreglo.
    
    cout << "Array ordenado: \n"; // Imprime el mensaje "Array ordenado:" seguido de una nueva línea.
    printArray(arr, n); // Llama a la función printArray para imprimir el arreglo ordenado.
    
    return 0; // Devuelve 0 para indicar que el programa terminó correctamente.
}
