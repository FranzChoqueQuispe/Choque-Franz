import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)   #Titulo del juego
        pygame.display.set_icon(ICON)       #Icono del Juego                  
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10    #Velocidad del Juego
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()

    def run(self):      
        # Game loop: events - update - draw (Ciclo del Juego)
        self.playing = True     #Iniciando el Juego
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()   #Salir del Juego
        pygame.quit()

    def events(self):
        for event in pygame.event.get():    #Lista que devuelve los eventos
            if event.type == pygame.QUIT:   #Verifica si existe un evento (QUIT: Si se pulsa el boton de cerrar)
                self.playing = False        #Se cierra el juego

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))   #Fondo de pantalla
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
