import pygame
from random import randint

def update_ship(ship_x, ship_y, ship_speed, controls):
    if controls[0] == True:
        ship_x -= ship_speed
    if controls[1] == True:
        ship_x += ship_speed
    if controls[2] == True:
        ship_y -= ship_speed
    if controls[3] == True:
        ship_y += ship_speed
    return(ship_x, ship_y)

def draw_ship(screen, ship, ship_x, ship_y, is_hit):
    screen.blit(ship, (ship_x, ship_y))
    return ship

def update_controls(controls, key, value):
    if key == pygame.K_SPACE:
        controls[4] = value
    elif key == pygame.K_LEFT:
        controls[0] = value
    elif key == pygame.K_RIGHT:
        controls[1] = value
    elif key == pygame.K_UP:
        controls[2] = value
    elif key == pygame.K_DOWN:
        controls[3] = value
    return controls

def update_bullets(ship_x, ship_y, bullets, controls, width):
    if controls[4] == True:
        bullets.append([ship_x + 80, ship_y + 25])
    for bullet in bullets:
        bullet[0] += 20
        if bullet[0] > width:
            bullets.remove(bullet)
    return bullets

def draw_bullets(screen, bullets):
    for bullet in bullets:
        x, y = bullet[0], bullet[1]
        pygame.draw.circle(screen, (155, 52, 235), (int(x), int(y)), 2)


width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ship & Shooting')
clock = pygame.time.Clock()
running = True

# VARIABLES SECTION
ship_x = 20
ship_y = int(height/2)
ship_speed = 5
ship = pygame.image.load('ship.png').convert_alpha()
controls = [False, False, False, False, False]
#           left   right   up    down  shoot
bullets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # EVENTS SECTION
        elif event.type == pygame.KEYDOWN:
            controls = update_controls(controls, event.key, True)
        elif event.type == pygame.KEYUP:
            controls = update_controls(controls, event.key, False)

    # UPDATE SECTION
    screen.fill((0, 0, 0))
    is_hit = False
    draw_ship(screen, ship, ship_x, ship_y, is_hit)
    ship_x, ship_y = update_ship(ship_x, ship_y, ship_speed, controls)
    bullets = update_bullets(ship_x, ship_y, bullets, controls, width)
    draw_bullets(screen, bullets)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
