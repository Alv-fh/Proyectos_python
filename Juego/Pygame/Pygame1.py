import pygame
import sys

pygame.init()


#Definir colores

BLACK       = (   0,   0,   0)
WHYTE       = ( 255, 255, 255)
BLUE        = (   0,   0, 255)
RED         = ( 255,   0,   0)
GREEN       = (   0, 255,   0)





syze = (820, 520)

#Crear ventana

screen = pygame.display.set_mode(syze)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #Poner color a pantalla
    screen.fill(BLUE)
    ### -----ZONA DE DIBUJO
    pygame.draw.line(screen, WHYTE, [400, 100], [100, 100], 5)
    







    ### -----ZONA DE DIBUJO
    #Actualizar pantalla

    pygame.display.flip()