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

"""Definición de las funciones:

encontrar_primos(num): Esta función recibe un número entero positivo num y devuelve una lista con los números primos que dividen a num.
encontrar_factores_primos(num): Esta función recibe un número entero positivo num y devuelve una lista con la factorización prima de num.
Se le solicita al usuario que ingrese un número entero positivo utilizando la función input(), y se almacena su valor en la variable num.

Se llama a la función encontrar_primos(num) y se almacena su resultado en la variable primos.

Se imprime la lista de números primos que dividen a num utilizando la función print().

Se llama a la función encontrar_factores_primos(num) y se almacena su resultado en la variable factores_primos.

Se imprime la factorización prima del número num utilizando la función print(). Para ello, se recorre la lista factores_primos con un bucle for e imprime cada elemento con un asterisco * entre ellos, excepto el último elemento que se imprime sin el asterisco. Esto se logra mediante el uso de un condicional if y la función end de print()."""

