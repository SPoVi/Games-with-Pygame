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
x1 = 10
sep = 10
# Donde empieza el cuadrado
tareaX = 0
tareaY = WIN_HEIGHT / 2


surface.fill((0,0,0)) # Fondo negro

# PEDIR DATOS
print("Periodo de la tarea: ")
periodo = int(input())
print("Tiempo de computo de la tarea (tiempo max de ejecución): ")
computo = int(input())


cont = 0

# loop infinito
while True:

    #Param del rect: (ventana, color, x0, y0, x1, y1)
    if cont < computo:
        pygame.draw.rect(surface, (255, 255, 255), (tareaX, tareaY, x1, y1))  # Duracion (blanco)
        tareaX+= 10
        cont+= 1
    elif cont == computo:
        pygame.draw.rect(surface, (0, 0, 0), (tareaX, tareaY, x1, y1))  # Espacio (negro)
        tareaX += 10
        cont = 0

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    pygame.time.wait(1000) # 1s
    pygame.display.update()
