// Juan David Otero - Juan Manuel Marmolejo - Andres Felipe Vivas
// Encontrar numeros primos mediante la division sucesiva
// Este código tiene como objetivo encontrar los números primos que dividen a un número entero positivo dado por el usuario, así como también su factorización prima.
//-----------Juan David Otero----------------------------
def encontrar_primos(num):
    # Lista para almacenar los números primos
    primos = []
    
    # Dividir por 2 hasta que el número sea impar
    while num % 2 == 0:
        primos.append(2)
        num = num // 2
    
    # Dividir por los demás números primos impares
    # Desde 3 hasta la raíz cuadrada del número
    for i in range(3, int(num**0.5)+1, 2):
        while num % i == 0:
            primos.append(i)
            num = num // i
    
    # Si queda algún número mayor que 2, es primo
    if num > 2:
        primos.append(num)
    
    return primos
//----------------Andres Felipe Vivas-------------------------------------------------
def encontrar_factores_primos(num):
    # Lista para almacenar los factores primos
    factores_primos = []
    
    # Dividir por 2 hasta que el número sea impar
    while num % 2 == 0:
        factores_primos.append(2)
        num = num // 2
    
    # Dividir por los demás números primos impares
    # Desde 3 hasta la raíz cuadrada del número
    for i in range(3, int(num**0.5)+1, 2):
        while num % i == 0:
            factores_primos.append(i)
            num = num // i
    
    # Si queda algún número mayor que 2, es primo
    if num > 2:
        factores_primos.append(num)
    
    return factores_primos
//-----------------Juan Manuel Marmolejo--------------------------
# Pedir al usuario el número a factorizar
num = int(input("Ingrese un número entero positivo: "))

# Encontrar los números primos que dividen al número
primos = encontrar_primos(num)

# Imprimir los números primos
print("Los números primos que dividen a", num, "son:", primos)

# Encontrar la factorización prima del número
factores_primos = encontrar_factores_primos(num)

# Imprimir la factorización prima
print("La factorización prima de", num, "es:", end=" ")
for i in range(len(factores_primos)):
    if i == len(factores_primos) - 1:
        print(factores_primos[i])
    else:
        print(factores_primos[i], "*", end=" ")
        
        
 // Comentarios

""" (Juan David Otero) Esta parte del código define una función llamada "encontrar_primos" que recibe como parámetro un número entero positivo "num". Esta función tiene como objetivo encontrar todos los números primos que dividen al número "num".

Primero, se crea una lista vacía llamada "primos" que será utilizada para almacenar los números primos que dividen a "num".

Luego, se utiliza un bucle "while" para dividir sucesivamente el número "num" entre 2 hasta que sea impar. Cada vez que se divide entre 2, se agrega el número primo 2 a la lista "primos" y se actualiza el valor de "num" dividiéndolo entre 2.

Después, se utiliza un bucle "for" que va desde 3 hasta la raíz cuadrada de "num" (inclusive) en incrementos de 2. Dentro de este bucle, se utiliza otro bucle "while" para dividir sucesivamente el número "num" por cada número impar que sea primo. Cada vez que se encuentra un número primo que divide a "num", se agrega a la lista "primos" y se actualiza el valor de "num" dividiéndolo por el número primo encontrado.

Finalmente, si el número "num" que queda es mayor que 2, entonces también es un número primo y se agrega a la lista "primos".

La función retorna la lista "primos" con todos los números primos que dividen al número "num".

-----------------------------------------------------------------------------------

(Andres Felipe Vivas) Esta función encontrar_factores_primos también utiliza la estrategia de división sucesiva para encontrar los factores primos del número num. Primero, se crea una lista vacía factores_primos donde se almacenarán los factores primos encontrados.

Luego, al igual que en la función encontrar_primos, se divide num por 2 hasta que sea impar. Después, se itera desde 3 hasta la raíz cuadrada de num en pasos de 2, buscando números que sean divisores de num. Si se encuentra un divisor, se agrega a la lista factores_primos y se actualiza num dividiéndolo por el divisor encontrado.

Finalmente, si num es mayor que 2, entonces es un número primo y se agrega a la lista factores_primos. La función retorna la lista factores_primos que contiene los factores primos del número num.

-----------------------------------------------------------------------------------

(Juan Manuel Marmolejo) En esta parte del código, se le pide al usuario que ingrese un número entero positivo utilizando la función input() y se almacena en la variable num.

Luego, se llama a la función encontrar_primos(num) para encontrar los números primos que dividen a num y se almacenan en la variable primos.

A continuación, se imprime en la consola la lista de números primos que dividen a num mediante la función print().

Luego, se llama a la función encontrar_factores_primos(num) para encontrar la factorización prima del número num y se almacena en la variable factores_primos.

Finalmente, se imprime en la consola la factorización prima de num utilizando un ciclo for y la función print(), donde se recorre cada elemento de la lista factores_primos y se imprime junto con un asterisco como separador. Si es el último elemento, se imprime sin el asterisco y se agrega un salto de línea al final.
"""

