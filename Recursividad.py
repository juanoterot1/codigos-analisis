#Ejercio 4.4
"""Dado un arreglo constituido de números enteros y que contiene N elementos siendo N >= 1, devolver el elemento
mayor."""
# Realizado por Juan David Otero - Juan Manuel Marmolejo - Andres Vivas.
def elemento_mayor(arreglo, n):
    if n == 1:
        return arreglo[0]
    else:
        return max(arreglo[n-1], elemento_mayor(arreglo, n-1))

arreglo = [int(x) for x in input("Ingrese los elementos del arreglo separados por espacio: ").split()]
n = len(arreglo)
print("El número más grande en el arreglo es", elemento_mayor(arreglo, n))

#Este código hace lo siguiente:

#1. Pide al usuario que ingrese los elementos de la lista.
#2. Convierte los valores ingresados en enteros y los almacena en la lista arr.
#3. Calcula la longitud de la lista y la almacena en la variable n.
#4. Llamar a la función max_element y pasar arr y n como argumentos.
#5. Imprime el resultado.

"""¿Donde se demuestra la recursion en este codigo?
la recursión en este código se ve en la llamada a la función "elemento_mayor" dentro de sí misma.
 La función toma dos argumentos:
 una lista de números enteros y un entero que representa la longitud de la lista.
La función verifica si la longitud de la lista es igual a 1. Si es así, la función devuelve el primer elemento de la lista.
 Esta es la condición que detiene la recursión.
"""
