// Juan David Otero - Juan Manuel Marmolejo - Andres Felipe Vivas

import random

def tirar_dado():
    return random.randint(1,6)

def jugar_blackjack():
    print("¡Bienvenido al juego de Blackjack!\n")
    
    # Tira los dados iniciales del jugador
    dado1 = tirar_dado()
    dado2 = tirar_dado()
    total_jugador = dado1 + dado2
    print("Tiraste un %d y un %d. Tu total es %d.\n" % (dado1, dado2, total_jugador))
    
    # Tira los dados iniciales de la máquina
    dado1 = tirar_dado()
    dado2 = tirar_dado()
    dado3 = tirar_dado()
    total_maquina = dado1 + dado2 + dado3
    print("La máquina tiró un %d, un %d y un %d. Su total es %d.\n" % (dado1, dado2, dado3, total_maquina))
    
    # Juega el jugador
    while total_jugador < 21:
        continuar = input("¿Quieres tirar un dado adicional? (s/n): ")
        if continuar == 's':
            dado_nuevo = tirar_dado()
            total_jugador += dado_nuevo
            print("Tiraste un %d. Tu total es %d.\n" % (dado_nuevo, total_jugador))
            # Tira los dados de la máquina después de la tirada del jugador
            if total_maquina < 18:
                print("La máquina decide seguir jugando.")
                dado_nuevo = tirar_dado()
                total_maquina += dado_nuevo
                print("La máquina tiró un %d. Su total es %d.\n" % (dado_nuevo, total_maquina))
            else:
                print("La máquina decide no jugar más.")
        else:
            break
    
    # Juega la máquina
    while total_maquina < 18:
        print("La máquina decide seguir jugando.")
        dado_nuevo = tirar_dado()
        total_maquina += dado_nuevo
        print("La máquina tiró un %d. Su total es %d.\n" % (dado_nuevo, total_maquina))
    
    # Determina quién ganó
    if total_jugador > 21:
        print("¡Te pasaste de 21! La máquina gana.")
    elif total_maquina > 21:
        print("¡La máquina se pasó de 21! Tú ganas.")
    elif total_jugador > total_maquina:
        print("¡Tú ganas!")
    elif total_maquina > total_jugador:
        print("La máquina gana.")
    else:
        print("Es un empate.")
        
jugar_blackjack()



// Explicacion del algortimo

"""Primero se definen dos funciones: "tirar_dado()" y "jugar_blackjack()". La primera función simplemente devuelve un número aleatorio entre 1 y 6, que simula un dado.

La segunda función es la que lleva a cabo toda la dinámica del juego. Comienza imprimiendo un mensaje de bienvenida y luego tira dos dados para el jugador y tres para la máquina, imprimiendo el resultado de ambos.

A continuación, se inicia un bucle "while" que permite al jugador seguir tirando dados hasta que decida parar o hasta que su total supere 21. En cada iteración del bucle, se le pregunta al jugador si quiere tirar un dado adicional y se actualiza su total. Si el total del jugador supera 21, el juego termina y la máquina gana automáticamente.

Luego de que el jugador haya terminado de tirar dados, se inicia otro bucle "while" que simula los tiros de la máquina. En cada iteración, la máquina decide aleatoriamente si sigue tirando o no y tira un dado adicional si decide seguir. Este proceso continúa hasta que el total de la máquina supere 18.

Finalmente, se determina quién ganó. Si el total del jugador es mayor a 21, la máquina gana automáticamente. Si el total de la máquina es mayor a 21, el jugador gana automáticamente. Si ninguno de los dos supera los 21, el que tenga el total más alto gana. Si ambos tienen el mismo total, es un empate.

En la versión modificada que escribí, después de cada tiro del jugador, se imprime el total actual de la máquina. Además, si la máquina decide seguir tirando, se imprime un mensaje indicando que lo hizo y el resultado del nuevo tiro."""
