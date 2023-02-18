#Ejercicio 3.7
"""Escribir un procedimiento que calcule el factorial de un número natural pasado como parámetro, en forma iterativa.
Realizar todas las validaciones que considere necesarias. """
#Juan David Otero, Juan Manuel Marmolejo, Andres Vivas
def factorial(n):
    if n < 0:
        return "El número debe ser un entero positivo o cero"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

n = int(input("Ingrese un número entero positivo o cero: "))
print("El factorial de", n, "es", factorial(n))

#Este código hace lo siguiente:

#1. Pide al usuario que ingrese un número.
#2. Convierte el valor ingresado en un entero y lo almacena en la variable num.
#3. Llamar a la función factorial y pasar num como argumento.
#4. Imprime el resultado.
