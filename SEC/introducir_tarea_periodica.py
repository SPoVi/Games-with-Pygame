'''
Partimos de tarea_periodica.py

A diferencia del otro codigo aqui los datos de la tarea se introducen por el terminal
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
pygame.display.set_caption('Codigo 2: Tarea Periodica.')

# Variables cosntantes de la tareas
y1 = 10
sep = 10
# Donde empieza el cuadrado
tarea1X = 0
tarea1Y = WIN_HEIGHT / 2


surface.fill((0,0,0)) # Fondo negro

# PEDIR DATOS
print("Duracion de la tarea?: ")
tarea1_Duration = int(input())


# loop infinito
while True:

    #(ventana, color, x0, y0, x1, y1)
    # Mediante la diferencia entre x1-x0 se determina la duracion de la tarea.
    pygame.draw.rect(surface,(255,255,255),(tarea1X,tarea1Y, tarea1_Duration, y1)) # Duracion
    tarea1X += tarea1_Duration + sep  # Periodo. Cuando aparece el proximo cuadrado

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    pygame.time.wait(1000) # 1s
    pygame.display.update()
