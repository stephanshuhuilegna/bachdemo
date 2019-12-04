import pygame
from random import randint
from math import sin

class Enemy:
    def __init__(self, x, y, img, width, height, speed, fire_rate, fire_count, life):
        self.x = x
        self.y = y
        self.img = img
        self.width = width
        self.height = height
        self.speed = speed
        self.fire_rate = fire_rate
        self.fire_count = fire_count
        self.life = life

def add_enemy(enemies, enemy_img):
    enemy = Enemy(x, y, enemy_img, width, height, speed, fire_rate, fire_count, life)
    enemies.append(enemy)
    return enemies

def update_enemies(enemies, enemy_shots):
    pass

def draw_enemies(screen, enemies):
    for enemy in enemies:
        screen.blit(enemy, (Enemy(x), Enemy(y)))
    return enemy

def update_shots(enemy_shots):
    pass

def draw_enemy_shots(screen, enemy_shots):
    pass


width = 800
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Enemies')
clock = pygame.time.Clock()
running = True
clock_tick = 0

# VARIABLES FOR ENEMIES
enemy_img = pygame.image.load('enemy.png').convert_alpha()
enemies = []
y = randint(25, 525)
x = width
fire_rate = 30
fire_count = 0
speed = 2
life = 1
enemy = Enemy(x, y, enemy_img, width, height, speed, fire_rate, fire_count, life)
# enemies.append(enemy)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # UPDATE ENEMIES

    # ADD ENEMIES

    # TESTING AREA

    pygame.display.update()
    clock.tick(60)
    clock_tick += 1
    add_enemy(enemies, enemy)
    draw_enemies(screen, enemies)
pygame.quit()