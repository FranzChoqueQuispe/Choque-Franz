import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, SCREEN_HEIGHT, SCREEN_WIDTH, ENEMY_2

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEGHT = 60
    X_POS = 200
    Y_POS = 0
    X_POS_RANGE = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    SPEED_ON_Y = 1
    SPEED_ON_X = 10
    MOVES = {0: 'left', 1: 'right', 2: 'teleport'}
    """#Enemy 2
    ENEMY_2_WIDTH = 75
    ENEMY_2_HEGHT = 100
    SPEED_ON_Y_ENEMY_2 = 2
    SPEED_ON_X_ENEMY_2 = 5"""
    
    


    def __init__(self):
        self.image = ENEMY_1
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEGHT))
        self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0,1)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)

        """#Enemy 2
        self.image2 = ENEMY_2
        self.image2 = pygame.transform.scale(self.image2, (self.ENEMY_2_WIDTH, self.ENEMY_2_HEGHT))
        self.rect2 = self.image2.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction_enemy_2 = self.MOVES[random.randint(0,2)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)"""

    def update(self, enemies):
        self.rect.y += self.SPEED_ON_Y 

        if self.direction == self.MOVES[0]:
            self.rect.x -= self.SPEED_ON_X
        elif self.direction == self.MOVES[1]:
            self.rect.x += self.SPEED_ON_X

        self.handle_direction()

        if self.rect.top > SCREEN_HEIGHT:
            enemies.remove(self)

        """#Enemy 2 
        self.rect2.y += self.SPEED_ON_Y_ENEMY_2 

        if self.direction_enemy_2 == self.MOVES[0]:
            self.rect2.x -= self.SPEED_ON_X_ENEMY_2
        elif self.direction_enemy_2 == self.MOVES[1]:
            self.rect2.x += self.SPEED_ON_X_ENEMY_2
        elif self.direction_enemy_2 == self.MOVES[2]:
            self.rect2.x += 20

        self.handle_direction()

        if self.rect.top > SCREEN_HEIGHT and self.rect2.top > SCREEN_HEIGHT:
            enemies.remove(self)"""

    

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #screen.blit(self.image2, self.rect2) #Enemy 2
    
    def handle_direction(self):
        self.movement_count += 1

        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
            #self.direction_enemy_2 = self.MOVES[0]
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]
            #self.direction_enemy_2 = self.MOVES[1]

        if self.movement_count >= self.moves_before_change:
            self.movement_count = 0
