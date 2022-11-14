#Wyatt Lowe
# 11/9/22
#First Game(Drop Down Shooter)

import pygame
import random

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    K_SPACE,
    QUIT
)

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

class Player(pygame.sprite.Sprite):
    moveCount = 0
    isMoving = False
    speed = 5
    Level = 1
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('./plane_2_green.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH / 200, SCREEN_HEIGHT / 2))

    def update(self, pressed_keys):
        # playerAnimation = ['Frame1', 'Frame2', 'Frame3', 'etc.']

        # if self.moveCount > len(playerAnimation) - 1:
            # self.moveCount = 0
        # self.surf = pygame.image.load(playerAnimation[self.moveCount]).convert_alpha()

        if pressed_keys[K_UP]:
            self.rect.move_ip(0 ,-self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)

        # This might keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_HEIGHT

# Initializing the game
pygame.init()
# This is a temporary sub for a sky background I have
black = (0, 0, 0)
red = 135
green = 206
blue = 235
myFont = pygame.font.SysFont('Comicsans', 40)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Childs Top Gun')

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.isMoving = True
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.isMoving = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill((red, green, blue))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
    clock.tick(60)
