#DIA 8
#Escribir un programa que pida al usuario dos numeros y los sume. °Pero esta vez hazlo en C++! 

#include <iostream> //Esta linea incluye la biblioteca estandar de entrada y salida de C++. 
//Permite utilizar std::cout y std::cin para mostrar mensajes en la pantalla y recibir entradas del usuario, respectivamente.


int main() {
    // Variables para almacenar los numeros ingresados por el usuario
    int num1, num2; //Declara dos variables de tipo entero (int) llamadas num1 y num2.
    // Estas variables se usaran para almacenar los n√∫meros ingresados por el usuario.

    // Solicitar al usuario el primer numero
    std::cout << "Ingrese el primer numero: ";
    std::cin >> num1;

    // Solicitar al usuario el segundo numero
    std::cout << "Ingrese el segundo numero: ";
    std::cin >> num2;

    // Sumar los dos numeros
    int suma = num1 + num2;

    // Mostrar el resultado de la suma
    std::cout << "La suma de " << num1 << " y " << num2 << " es " << suma << std::endl;

    return 0;
}
