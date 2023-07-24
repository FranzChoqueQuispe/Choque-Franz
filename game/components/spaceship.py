import pygame

from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE, EVOLUTION_TYPE
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):    #Clase Spaceship hereda (utiliza datos) de la clase Sprite
    SPACESHIP_WIDTH = 40
    SPACESHIP_HEIGHT = 60
    SPACESHIP_POS_X = SCREEN_WIDTH / 2
    SPACESHIP_POS_Y = 500
    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        self.type = ['shoot_1', 'shoot_2']
        self.has_power_up = False
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.shooting_time = 0


    def update(self, user_input, bullet_manager, game):
        if game.player.power_up_type != EVOLUTION_TYPE:
            current_time = pygame.time.get_ticks()
            if self.shooting_time <= current_time:      
                if  user_input[pygame.K_a]:
                    skill = 0
                    self.type = 'shoot_1'
                    self.shoot(bullet_manager, skill)
                    
                elif user_input[pygame.K_s] :
                    skill = 1
                    self.type = 'shoot_2'
                    self.shoot(bullet_manager, skill)
                
                self.shooting_time += 500
        else:
            if  user_input[pygame.K_a]:
                skill = 0
                self.type = 'shoot_1'
                self.shoot(bullet_manager, skill)
                        
            elif user_input[pygame.K_s] :
                skill = 1
                self.type = 'shoot_2'
                self.shoot(bullet_manager, skill)

        if user_input[pygame.K_LEFT]:
            self.rect.x -= 10
            if self.rect.left < -10:
                self.rect.x = SCREEN_WIDTH - 30

        elif user_input[pygame.K_RIGHT]:
            self.rect.x += 10
            if self.rect.right > SCREEN_WIDTH + 10:
                self.rect.x = -10

        elif user_input[pygame.K_UP] and self.rect.bottom > 300:
            self.rect.y -= 10
        elif user_input[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10 

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    # Disparo
    def shoot(self, bullet_manager, skill):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet, skill)

    def set_image(self, image = SPACESHIP, size = (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def reset(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SPACESHIP_WIDTH, self.SPACESHIP_HEIGHT))
        self.rect = self.image.get_rect(midbottom = (self.SPACESHIP_POS_X, self.SPACESHIP_POS_Y))
        self.power_up_type = DEFAULT_TYPE
