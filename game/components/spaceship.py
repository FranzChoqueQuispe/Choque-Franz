import pygame

from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):    #Clase Spaceship hereda (utiliza datos) de la clase Sprite
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SPACESHIP_POS_X = SCREEN_WIDTH / 2
    SPACESHIP_POS_Y = 500
#
    def __init__(self):
        self.image = SPACESHIP
        #self.image2 = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        #self.image2 = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        #self.rect2 = self.image2.get_rect(midbottom = (self.SPACESHIP_POS_X + SCREEN_WIDTH, self.SPACESHIP_POS_Y))

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.rect.x -= 10
            #if self.rect.left < 0:
            if self.rect.left < -10:
                self.rect.x = SCREEN_WIDTH - 30
                #self.rect.x += SCREEN_WIDTH - self.SPACESHIP_WIDTH

            """self.rect2.x -= 10
            if self.rect.left < -SCREEN_WIDTH:
                self.rect.x += 2*SCREEN_WIDTH       
            elif self.rect2.left < -SCREEN_WIDTH:
                self.rect2.x += 2*SCREEN_WIDTH"""
            

        elif user_input[pygame.K_RIGHT]:
            self.rect.x += 10
            #if self.rect.right < SCREEN_WIDTH:
            if self.rect.right > SCREEN_WIDTH + 10:
                self.rect.x = -10
                #self.rect.x = 0

            """self.rect2.x += 10
            if self.rect.right > 2*SCREEN_WIDTH:
                self.rect.x = -40
            elif self.rect2.right > 2*SCREEN_WIDTH:
                self.rect2.x = -40"""

        elif user_input[pygame.K_UP] and self.rect.bottom > 300:
            self.rect.y -= 10
        elif user_input[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10   


    def draw(self,screen):
        screen.blit(self.image, self.rect)
        #screen.blit(self.image2, self.rect2)