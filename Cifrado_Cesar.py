def cifrado_cesar(texto, clave):
    # Definición del alfabeto en mayúsculas
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Inicialización de la variable de texto cifrado
    texto_cifrado = ''
    # Recorrido de cada letra del texto
    for letra in texto:
        # Comprobación de si la letra está en el alfabeto
        if letra.upper() in alfabeto:
            # Cálculo del índice de la letra cifrada
            indice = (alfabeto.index(letra.upper()) + clave) % len(alfabeto)
            # Agregado de la letra cifrada al texto cifrado
            if letra.isupper():
                texto_cifrado += alfabeto[indice]
            else:
                texto_cifrado += alfabeto[indice].lower()
        else:
            # Agregado de la letra original sin cifrar
            texto_cifrado += letra
    # Devolución del texto cifrado
    return texto_cifrado

# Solicitud del mensaje y la clave de cifrado al usuario
mensaje = input("Introduce el mensaje que deseas cifrar: ")
clave = int(input("Introduce la clave de cifrado: "))
# Llamado a la función de cifrado y almacenamiento del resultado
mensaje_cifrado = cifrado_cesar(mensaje, clave)
# Impresión del mensaje cifrado
print("Mensaje cifrado:", mensaje_cifrado)


mensaje = input("Introduce el mensaje que deseas cifrar: ")
clave = int(input("Introduce la clave de cifrado: "))
mensaje_cifrado = cifrado_cesar(mensaje, clave)
print("Mensaje cifrado:", mensaje_cifrado)
