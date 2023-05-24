import pygame

# setup
pygame.init()
screen = pygame.display.set_mode((1280, 720)) #hace una ventana
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            player_pos.y += 300
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("red")
    player_pos = pygame.Vector2( screen.get_width()/2, screen.get_height()/2)
    pygame.draw.circle(screen, "blue", player_pos, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300
    if keys[pygame.K_s]:
        player_pos.y += 300
    if keys[pygame.K_a]:
        player_pos.x -= 300
    if keys[pygame.K_d]:
        player_pos.x += 300
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
