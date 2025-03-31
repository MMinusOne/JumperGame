import pygame 

resolution = (1280, 720)

pygame.init()


screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
running = True

colors = {
    'primary': 'red',
    'boost': 'blue',
    'double_jump': 'purple'
}

player_size = 50
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()-player_size*2+10)
player_color = colors.get('primary')

gravity = 50
dt = 0

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    screen.fill((0, 0, 0))  # Clear the screen

    player_obj = pygame.draw.circle(screen, player_color, player_pos, player_size)

    player_pos.y += gravity * dt

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt

    if player_pos.y+200 <= screen.get_height():
        player_pos.y = 200

    pygame.display.flip()

    dt = clock.tick(60) /1000
