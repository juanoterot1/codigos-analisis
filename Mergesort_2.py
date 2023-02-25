import random
import time

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    
    # Creamos una lista auxiliar para evitar crear nuevas listas en cada llamada recursiva
    auxiliar = [None] * len(lista)
    
    # Llamamos recursivamente a mergesort para cada mitad de la lista
    mitad = len(lista) // 2
    izquierda = mergesort(lista[:mitad])
    derecha = mergesort(lista[mitad:])
    
    # Combinamos las dos mitades ordenadas en una lista ordenada utilizando la lista auxiliar
    i = j = k = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            auxiliar[k] = izquierda[i]
            i += 1
        else:
            auxiliar[k] = derecha[j]
            j += 1
        k += 1
    
    while i < len(izquierda):
        auxiliar[k] = izquierda[i]
        i += 1
        k += 1
    
    while j < len(derecha):
        auxiliar[k] = derecha[j]
        j += 1
        k += 1
    
    # Devolvemos la lista ordenada
    return auxiliar

# Generamos una lista de 10000 números aleatorios entre 0 y10
lista = [random.randint(0, 9999) for i in range(10)]

# Imprimimos la lista desordenada
print("Lista desordenada:")
print(lista)

# Ordenamos la lista usando mergesort y medimos el tiempo de ejecución
start_time = time.perf_counter()
ordenada = mergesort(lista)
end_time = time.perf_counter()

# Imprimimos la lista ordenada y el tiempo de ejecución en milisegundos
print("Lista ordenada:")
print(ordenada)
print(f"Tiempo de ejecución: {1000 * (end_time - start_time)} ms")
