def mergesort(lista):
    # Comprobamos si la lista es vacía o solo tiene un elemento
    if len(lista) <= 1:
        return lista
    
    # Dividimos la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    
    # Aplicamos recursivamente mergesort a cada mitad
    izquierda = mergesort(izquierda)
    derecha = mergesort(derecha)
    
    # Combinamos las dos mitades ordenadas en una lista ordenada
    return merge(izquierda, derecha)
    
def merge(izquierda, derecha):
    # Combinamos las dos mitades ordenadas en una lista ordenada
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
