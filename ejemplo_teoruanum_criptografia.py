# Función para cifrar un mensaje utilizando el cifrado César
def cifrado_cesar(mensaje, desplazamiento):
    cifrado = '' # Variable para almacenar el mensaje cifrado
    for letra in mensaje:
        if letra.isalpha(): # Si la letra es una letra del alfabeto
            num = ord(letra) # Obtener el código ASCII de la letra
            num += desplazamiento # Añadir el desplazamiento al código ASCII
            if letra.isupper(): # Si la letra es mayúscula
                if num > ord('Z'): # Si el código ASCII resultante está fuera del rango de las letras mayúsculas
                    num -= 26 # Restar 26 para volver al rango de las letras mayúsculas
                elif num < ord('A'): # Si el código ASCII resultante está fuera del rango de las letras mayúsculas
                    num += 26 # Sumar 26 para volver al rango de las letras mayúsculas
            elif letra.islower(): # Si la letra es minúscula
                if num > ord('z'): # Si el código ASCII resultante está fuera del rango de las letras minúsculas
                    num -= 26 # Restar 26 para volver al rango de las letras minúsculas
                elif num < ord('a'): # Si el código ASCII resultante está fuera del rango de las letras minúsculas
                    num += 26 # Sumar 26 para volver al rango de las letras minúsculas
            cifrado += chr(num) # Convertir el código ASCII cifrado en letra y añadir a la variable de mensaje cifrado
        else:
            cifrado += letra # Añadir la letra al mensaje cifrado sin cifrar
    return cifrado

# Función para descifrar un mensaje cifrado utilizando el cifrado César
def descifrado_cesar(mensaje_cifrado, desplazamiento):
    return cifrado_cesar(mensaje_cifrado, -desplazamiento) # Llamar a la función de cifrado César con el desplazamiento negativo para descifrar el mensaje

# Ejemplo de uso
mensaje_original = "Este es un mensaje secreto"
desplazamiento = 3
mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento) # Cifrar el mensaje original
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrado_cesar(mensaje_cifrado, desplazamiento) # Descifrar el mensaje cifrado
print("Mensaje descifrado:", mensaje_descifrado)


"""Primero, se define la función cifrado_cesar que toma dos argumentos: mensaje, el mensaje que se quiere cifrar, y desplazamiento, el número de caracteres que se quiere desplazar en el alfabeto para cifrar el mensaje. Dentro de la función, se inicializa una variable vacía cifrado que se utilizará para almacenar el mensaje cifrado.

Luego, se itera sobre cada letra del mensaje utilizando un ciclo for. Si la letra es una letra del alfabeto (es decir, si letra.isalpha() devuelve True), se obtiene el código ASCII de la letra utilizando la función ord(letra). Luego se le suma el desplazamiento para cifrar la letra.

Después, se verifica si la letra es mayúscula o minúscula utilizando los métodos letra.isupper() y letra.islower() respectivamente. Si es mayúscula, se verifica si el código ASCII resultante está fuera del rango de las letras mayúsculas (ord('Z') y ord('A')). En caso afirmativo, se resta o suma 26 al código ASCII para volver al rango de las letras mayúsculas. Si es minúscula, se realiza el mismo proceso pero para el rango de las letras minúsculas.

Por último, se convierte el código ASCII resultante en letra utilizando la función chr(num) y se añade a la variable cifrado. Si la letra no es una letra del alfabeto, se añade al mensaje cifrado sin cifrar.

La función descifrado_cesar es simplemente una función que llama a la función cifrado_cesar con el desplazamiento negativo para descifrar el mensaje.

En el ejemplo de uso, se define una variable mensaje_original que contiene el mensaje que se quiere cifrar. Se define también la variable desplazamiento con un valor de 3. Luego, se llama a la función cifrado_cesar con estos argumentos y se guarda el resultado en la variable mensaje_cifrado. Finalmente, se imprime en pantalla el mensaje cifrado utilizando la función print.

Después, se llama a la función descifrado_cesar con el mensaje cifrado y el desplazamiento utilizado previamente, y se guarda el resultado en la variable mensaje_descifrado. Finalmente, se imprime en pantalla el mensaje descifrado utilizando la función print."""
