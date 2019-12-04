import pygame
from random import randint

def add_star(stars, width, height):
    x = width
    y = randint(0, height)
    radius = randint(0, 5)
    speed = radius / 5
    colour = (radius * 50, radius * 50, radius * 50)
    stars.append([x, y, radius, speed, colour])
    return stars


def draw_stars(stars, screen):
    for i in range(len(stars)):
        x, y, radius, speed, colour = stars[i]
        stars[i][0] -= speed
        pygame.draw.circle(screen, colour, (int(x), int(y)), radius)

    return stars

def remove_stars(stars):
    for star in stars:
        if star[0] < 0:
            stars.remove(star)
    return stars

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Starfield')
clock = pygame.time.Clock()
running = True

stars = [[800, 300, 1, 0.2, (250, 250, 250)],
         [800, 500, 5, 0.5, (250, 250, 250)],
         [800, 340, 3, 0.3, (250, 250, 250)]]
x = 100
clock_tick = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    stars = draw_stars(stars, screen)
    stars = remove_stars(stars)
    print(len(stars))

    pygame.display.update()
    clock.tick(60)
    clock_tick += 1
    if clock_tick % 30 == 0:
        stars = add_star(stars, width, height)
pygame.quit()

