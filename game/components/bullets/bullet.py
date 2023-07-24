import pygame

from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT, BULLET_4

class Bullet(Sprite):
    PLAYER_IMAGE_2 = pygame.transform.scale(BULLET_4, (30, 40))
    PLAYER_IMAGE = pygame.transform.scale(BULLET, (10, 20))
    ENEMY_IMAGE = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    BULLET_TYPES = {'shoot_1': PLAYER_IMAGE, 'enemy': ENEMY_IMAGE, 'shoot_2': PLAYER_IMAGE_2 }
    SPEED = 10

    def __init__(self, spaceship):
        self.image = self.BULLET_TYPES[spaceship.type]
        self.rect = self.image.get_rect(center = spaceship.rect.center)
        self.owner = spaceship.type

    def update(self, bullets):
        if self.owner == 'enemy':
            self.rect.y += self.SPEED
            if self.rect.top > SCREEN_HEIGHT:
                bullets.remove(self)
        
        if self.owner == 'shoot_2' or self.owner == 'shoot_1':
            self.rect.y -= self.SPEED
            if self.rect.top < 0:
                bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
