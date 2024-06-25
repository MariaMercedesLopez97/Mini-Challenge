//DIA 11
//Palíndromo: Escribir un programa que determine si una cadena de caracteres ingresada por el usuario es un palíndromo ¡Pero hazlo en C++! :)#include <iostream>

#include <iostream> // Incluye la biblioteca de entrada y salida estándar de C++.
#include <string> // Incluye la biblioteca para el manejo de cadenas de caracteres.
#include <algorithm> // Incluye la biblioteca para funciones de algoritmos estándar, como reverse y transform.

using namespace std; // Utiliza el espacio de nombres estándar para evitar escribir std:: antes de cada objeto estándar.

// Función que verifica si una cadena es un palíndromo utilizando funciones de la biblioteca estándar.
bool esPalindromoSTD(const string& cadena) {
    string cadenaReversa = cadena; // Crea una copia de la cadena original.
    reverse(cadenaReversa.begin(), cadenaReversa.end()); // Invierte la cadena copiada.
    return cadena == cadenaReversa; // Compara la cadena original con la cadena invertida y devuelve true si son iguales, false en caso contrario.
}

int main() {
    string cadena; // Declara una variable para almacenar la cadena ingresada por el usuario.
    cout << "Ingresa una cadena de caracteres: "; // Solicita al usuario que ingrese una cadena.
    getline(cin, cadena); // Lee la cadena completa, incluidos los espacios, desde la entrada estándar.

    // Convertir a minúsculas y eliminar espacios en blanco
    transform(cadena.begin(), cadena.end(), cadena.begin(), ::tolower); // Convierte todos los caracteres de la cadena a minúsculas.
    cadena.erase(remove(cadena.begin(), cadena.end(), ' '), cadena.end()); // Elimina todos los espacios en blanco de la cadena.

    if (esPalindromoSTD(cadena)) {
        // Si la cadena es un palíndromo
        cout << "La cadena es un palíndromo." << endl; // Imprime que la cadena es un palíndromo.
    } else {
        // Si la cadena no es un palíndromo
        cout << "La cadena no es un palíndromo." << endl; // Imprime que la cadena no es un palíndromo.
    }

    return 0; // Devuelve 0 para indicar que el programa terminó correctamente.
}
#include <iostream> // Incluye la biblioteca de entrada y salida estándar de C++.
#include <string> // Incluye la biblioteca para el manejo de cadenas de caracteres.
#include <algorithm> // Incluye la biblioteca para funciones de algoritmos estándar, como reverse y transform.

using namespace std; // Utiliza el espacio de nombres estándar para evitar escribir std:: antes de cada objeto estándar.

// Función que verifica si una cadena es un palíndromo utilizando funciones de la biblioteca estándar.
bool esPalindromoSTD(const string& cadena) {
    string cadenaReversa = cadena; // Crea una copia de la cadena original.
    reverse(cadenaReversa.begin(), cadenaReversa.end()); // Invierte la cadena copiada.
    return cadena == cadenaReversa; // Compara la cadena original con la cadena invertida y devuelve true si son iguales, false en caso contrario.
}

int main() {
    string cadena; // Declara una variable para almacenar la cadena ingresada por el usuario.
    cout << "Ingresa una cadena de caracteres: "; // Solicita al usuario que ingrese una cadena.
    getline(cin, cadena); // Lee la cadena completa, incluidos los espacios, desde la entrada estándar.

    // Convertir a minúsculas y eliminar espacios en blanco
    transform(cadena.begin(), cadena.end(), cadena.begin(), ::tolower); // Convierte todos los caracteres de la cadena a minúsculas.
    cadena.erase(remove(cadena.begin(), cadena.end(), ' '), cadena.end()); // Elimina todos los espacios en blanco de la cadena.

    if (esPalindromoSTD(cadena)) {
        // Si la cadena es un palíndromo
        cout << "La cadena es un palíndromo." << endl; // Imprime que la cadena es un palíndromo.
    } else {
        // Si la cadena no es un palíndromo
        cout << "La cadena no es un palíndromo." << endl; // Imprime que la cadena no es un palíndromo.
    }

    return 0; // Devuelve 0 para indicar que el programa terminó correctamente.
}
