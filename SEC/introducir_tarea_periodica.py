'''
Partimos de tarea_periodica.py

PASO 1:
A diferencia del otro codigo aqui los datos de la tarea se introducen por el terminal

PASO 2:
Introducir otra tarea

PASO 3:
Crear una clase "Tarea"
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

# TERMINAL
print("Introduce la cantidad de tareas: ")
numTareas = int(input())
i = 0
lista_periodo = list()
lista_computo = list()

for i in range(0,numTareas):
    # PEDIR DATOS
    print(f"Periodo de la tarea {i+1}: ")
    periodo = int(input())
    print(f"Tiempo de computo de la tarea (tiempo max de ejecución) {i}: ")
    computo = int(input())

    lista_periodo.append(periodo)
    lista_computo.append(computo)

# Variables cosntantes de la tareas
y1 = 10
x1 = 10
sep = 10 # separacion entre dibujos cada segundo

print("Entrando en posicionamiento inicial")
# Donde empieza el cuadrado
lista_TareaX = list()
lista_TareaY = list()
lista_cont = list()
for i in range(0,numTareas):
    tareaX = 0
    tareaY = WIN_HEIGHT / 2 + 20*(i-1)

    lista_TareaX.append(tareaX)
    lista_TareaY.append(tareaY)
    lista_cont.append(0)


surface.fill((0,0,0)) # Fondo negro

# loop infinito
while True:
    # Param del rect: (ventana, color, x0, y0, x1, y1)
    for i in range(0,numTareas):

        if lista_cont[i] < lista_computo[i]: # Duracion (blanco)
            pygame.draw.rect(surface, (255, 255, 255), (int(lista_TareaX[i]), int(lista_TareaY[i]), x1, y1))
            lista_TareaX[i] += sep
            lista_cont[i] += 1
        elif lista_cont[i] == lista_computo[i]:
            pygame.draw.rect(surface, (0, 0, 0), (int(lista_TareaX[i]), int(lista_TareaY[i]), x1, y1))
            lista_TareaX[i] += sep
            lista_cont[i] = 0

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    pygame.time.wait(1000) # 1s
    pygame.display.update()
