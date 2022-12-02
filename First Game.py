#Wyatt Lowe
# 11/9/22
#First Game(Side scroller?)

import pygame
import random as rd

from pygame.locals import *

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
background = pygame.image.load("./images/SKY.png")

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

        if pressed_keys[K_UP]:
            self.rect.move_ip(0 ,-self.speed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)

        # This keeps player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


pygame.init()
Lives = 10
# This is a temporary sub for a sky background I have
black = (0, 0, 0)
myFont = pygame.font.SysFont('Comicsans', 40)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Childs Top Gun')

player = Player()

all_sprites = pygame.sprite.Group()
weapon_sprites = pygame.sprite.Group()
all_sprites.add(player)




class Weapon(pygame.sprite.Sprite):
    def __int__(self):
        super(Weapon,self).__init__()
        self.FireCount = 0
        self.surf = pygame.image.load("images/fire_ball_1.png").convert_alpha()
        self.rect = self.surf.get_rect(
            center=((player.rect.left + 200),(player.rect.right- 2)),
        )
        self.speed = rd.randint(4,10)

    def update(self):
            if self.rect.right <= 0:
                self.kill()
            else:
                self.rect.move_ip(0, -self.speed)


class Enemy(pygame.sprite.Sprite):
    def __int__(self):
        super(Enemy,self).__init__()
        self.ESpeed = rd.randint(3, 5)
        self.ECount = 0
        self.surf = pygame.image.load("images/plane_2_red.png").convert_alpha()
        self.rect = self.surf.get_rect(
            center=(
                (rd.randint(200,SCREEN_WIDTH-200)),
                (rd.randint(-2,0))
            )
        )

    def update(self):
        EAnimation = ["images/plane_2_red.png"]
        if self.ECount > len(EAnimation) - 1:
            self.Enemycount = 0
        self.surf = pygame.image.load(EAnimation[self.ECount]).convert_alpha()
        self.ECount += 1
        self.rect.move_ip(0, self.ESpeed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

running = True
while running:
    scoreText = myFont.render(('                                                                     '
                               '        Health: ' + str(Lives)), True, (215, 255, 255))
    scoreRect = scoreText.get_rect()
    scoreRect.center = (300, 25)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT or event.key == K_RIGHT:
                player.isMoving = True
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                print('print running ')
                player.isMoving = False

            if event.key == K_RIGHT:
                weapon = Weapon()
                weapon_sprites.add(weapon)
                all_sprites.add(weapon)
                weapon_sprites.update()

        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    screen.blit(scoreText, scoreRect)
    weapon_sprites.update()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()
    clock.tick(100)

player = Player()

all_sprites = pygame.sprite.Group()
weapon_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

all_sprites.add(player)

shotcount = 0
