import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720)) # crea una ventana
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) # mueve esta línea antes del bucle while

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: # verifica qué tecla se presiona
                player_pos.y -= 10 # ajusta la velocidad de movimiento
            elif event.key == pygame.K_s:
                player_pos.y += 10
            elif event.key == pygame.K_a:
                player_pos.x -= 10
            elif event.key == pygame.K_d:
                player_pos.x += 10
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255)) # "red" se cambia a una tupla de valores RGB
    pygame.draw.circle(screen, (240, 0, 212), (int(player_pos.x), int(player_pos.y)), 40) # se convierten las coordenadas a enteros
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 10
    if keys[pygame.K_s]:
        player_pos.y += 10
    if keys[pygame.K_a]:
        player_pos.x -= 10
    if keys[pygame.K_d]:
        player_pos.x += 10
    
    pygame.display.flip()

    clock.tick(60)  # limita los FPS a 60

pygame.quit()
