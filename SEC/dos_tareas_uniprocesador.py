'''
Dos tareas no pueden dibujarse al mismo tiempo

PASO 1:
Con los datos predeterminados (sin solicitarlos por pantalla)
Partimos de tarea_periodica.py

PASO 2:
Piendo los datos.

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
pygame.display.set_caption('Codigo 3: Tareas en exlusión.')

# VARIABLES DE LAS TAREAS
y1 = 10 # tamaño del cuadrado verticalmente
x1 = 10 # tamapo del cuadrado hoizontalmente
sep = 10 # donde se dibuja el siguiente cuadrado (negro si esta vacio)
tareaX = 0

#tarea1X = 0 # lateral izquierdo
tarea1Y = WIN_HEIGHT / 2 # mitad de la ventana
computo1 = 1
periodo1 = 4

#tarea2X = 0
tarea2Y = WIN_WIDTH / 2 + 20 # debajo de la tarea 1 con una separacion de 10
computo2 = 2
periodo2 = 8

lista_cont = [0,0,0]
lista_computo = [computo1, computo2]
#Semaforo
sem1 = False # Rojo

# Minimo comum multiplo
def f_mcm(x,y):
    z = max(x,y)
    while True:
        if (z % x == 0) and (z % y == 0):
            return z
        z += 1

mcm = f_mcm(periodo1, periodo2)
# LOOP INFINITO
while True:



    if lista_cont[0] < mcm: # mcm = 8

        if lista_computo[0] > 0:
            pygame.draw.rect(surface, (255, 255, 255), (tareaX,int(tarea1Y), x1, y1))
            lista_computo[0] -= 1
            sem1 = False
            print("T1")
        elif lista_computo[0] == 0:
            pygame.draw.rect(surface, (100, 100, 100), (tareaX, tarea1Y, x1, y1))
            sem1 = True

        if lista_computo[1] > 0 and sem1 == True:
            pygame.draw.rect(surface, (255, 255, 255), (tareaX, int(tarea1Y + 20), x1, y1))
            lista_computo[1] -= 1
            print("    T2")

        tareaX += sep
        lista_cont[0] += 1
    else:
        tareaX += sep
        lista_cont[0] = 0
        lista_computo= [computo1,computo2]

    # EVENTO PARA SALIR
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    # ESPERA DE REFRESCO (VEL DE EJECUCION)
    #print(lista_cont[0])
    pygame.time.wait(1000) # 1s
    pygame.display.update()