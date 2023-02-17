# Importamos las librerías necesarias:
import pygame
import numpy as np


# Para comenzar vamos a crear la pantalla de nuestro juego
pygame.init()

width = 600
height = 600

screem = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screem.fill(bg)

# Número de celdas
ncX, ncY = 50, 50

# Dimensiones de las celdas
dimCW = width / ncX
dimCH = height / ncY

# Estado de las celdas. Vivas = 1; Muertas = 0
gameState = np.zeros((ncX, ncY))

# Vamos a inlcuir alguna celda viva en el inicio para ver su comportamiento
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

while True:
    # Creamos un copia del gameState sobre la que haremos los cambios, para que se realicen a la vez en cada momento
    newGameState = np.copy(gameState)

    for y in range(0, ncX):
        for x in range(0, ncY):

            # Calculamos el número de vecinos cercanos
            n_neigh = gameState[(x - 1) % ncX, (y - 1) % ncY] + \
                      gameState[(x) % ncX, (y - 1) % ncY] + \
                      gameState[(x + 1) % ncX, (y - 1) % ncY] + \
                      gameState[(x - 1) % ncX, (y) % ncY] + \
                      gameState[(x + 1) % ncX, (y) % ncY] + \
                      gameState[(x - 1) % ncX, (y + 1) % ncY] + \
                      gameState[(x) % ncX, (y + 1) % ncY] + \
                      gameState[(x + 1) % ncX, (y + 1) % ncY]

            # Rule 1: Una celda muerta con exactamente 3 vecinas vivas, "revive".
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1

            # Rule 2: Una celda viva con menos de 2 o más de 3 celdas vivas alrededor muere.
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0

            # Creamos el polígono de cada celda a dibujar
            poly = [((x) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x) * dimCW, (y + 1) * dimCH)]

            # Y coloreamos la celda para cada par de X e Y.
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screem, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screem, (255, 255, 255), poly, 0)

    # Al final de bucle actualizaremos el estado de todas las celdas al mismo tiempo.
    gameState = np.copy(newGameState)

    # Actualizamos la pantalla
    pygame.display.flip()
