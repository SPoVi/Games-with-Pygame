''' CODIGO 1: Creacion de tarea periodica

PASO 1:
Crear un cuadrado que vaya apareciendo y desapareciendo dejando un espacio
de su mismo tamaño entre dos cuadrados consecutivos.
Debe empezar en la mitad vertcial y el origen de la ventana.

PASO 2:
Añadir una segunda tarea que se visualize debajo de la primera.
Su duracion de ejecucion sera el doble de la primera y las separacion sera de 1s
igual que en con la tarea anterior.

'''

import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

# Pygame Variables
pygame.init()
clock = pygame.time.Clock()

# Variables constantes Ventana
WIN_WIDTH = 1000
WIN_HEIGHT = 500

surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # ventana
pygame.display.set_caption('Codigo 1: Tarea Periodica. Per = 2 , Duracion = 1')

# Variables de la tareas
y1 = 10
sep = 10
    # Donde empieza el cuadrado
tarea1X = 0
tarea1Y = WIN_HEIGHT / 2
tarea1_D= 10

tarea2X = 0
tarea2Y = WIN_HEIGHT / 2 + 20
tarea2_D = 30 # 3s

surface.fill((0,0,0)) # Fondo negro

count = 0

while True:

    #(ventana, color, x0, y0, x1, y1)
    # Mediante la diferencia entre x1-x0 se determina la duracion de la tarea.
    pygame.draw.rect(surface,(255,255,255),(tarea1X,tarea1Y, tarea1_D, y1)) # Duracion
    tarea1X += tarea1_D + sep  # Periodo. Cuando aparece el proximo cuadrado

    # Ejecutar cada (tarea2_D + sep)/10 , en este caso cada (30+10)/ 10 = 4s
    if count % 2 == 0:
        pygame.draw.rect(surface, (0, 255, 255), (tarea2X, tarea2Y, tarea2_D, y1))  # Duracion
        tarea2X += tarea2_D + sep  # Periodo. Cuando aparece el proximo cuadrado

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    pygame.time.wait(1000) # 1s
    count += 1
    pygame.display.update()
