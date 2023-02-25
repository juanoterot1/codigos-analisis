import random
import timeit

def mergesort(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i, j = 0, 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado += izquierda[i:]
    resultado += derecha[j:]

    return resultado

# Generamos una lista de 10 números aleatorios entre 0 y 99
lista = [random.randint(0, 99) for i in range(10)]

# Imprimimos la lista desordenada
print("Lista desordenada:")
print(lista)

# Medimos el tiempo de ejecución de mergesort con timeit
tiempo = timeit.timeit(lambda: mergesort(lista), number=1000)

# Imprimimos la lista ordenada y el tiempo de ejecución en segundos
print("Lista ordenada:")
print(mergesort(lista))
print(f"Tiempo de ejecución: {tiempo} segundos")
