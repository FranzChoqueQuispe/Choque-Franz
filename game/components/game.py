import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.counter import Counter

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)   #Titulo del juego
        pygame.display.set_icon(ICON)       #Icono del Juego                  
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False    #Se inicio la ventana
        #self.score = False      #Score                      ###
        self.game_speed = 10    #Velocidad del Juego
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        #self.death_counter = 0                              ###
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu(self.screen, 'Press any botton to start')  #######
        self.counter = Counter(self.screen)

    def execute(self):
        self.running = True
        while self.running and not self.playing:
            self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self): 
        self.score = 0     #Reseteo del score   
        self.bullet_manager.reset()
        self.enemy_manager.reset()  
        # Game loop: events - update - draw (Ciclo del Juego)
        self.playing = True     #Iniciando el Juego
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.display.quit()   #Salir del Juego
        #pygame.quit()  #Se quitan para mostarar el menu a traves del execute

    def events(self):
        for event in pygame.event.get():    #Lista que devuelve los eventos
            if event.type == pygame.QUIT:   #Verifica si existe un evento (QUIT: Si se pulsa el boton de cerrar)
                self.playing = False        #Se cierra el juego

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager) #probar con solo self en lugar de sel.bullet_manager
        self.enemy_manager.update(self)
        self.bullet_manager.update(self, self.counter)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))   #Fondo de pantalla
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
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

    def show_menu(self):
        self.menu.draw(self.screen)
        self.menu.update(self)

        self.menu.reset_screen(self.screen)
        self.counter.draw_game_over()

        """if self.death_counter > 0:
            icon = pygame.transform.scale((ICON), (80, 120))
            self.screen.blit(icon, ((SCREEN_WIDTH / 2) - 50, (SCREEN_HEIGHT / 2) - 150))
            messages_type = self.messages_game_over()
            self.menu.update_message(messages_type)
            #self.menu.draw(self.screen)"""

        self.menu.draw(self.screen)
        self.menu.update(self)

    #def increase_death_counter(self):
    #    self.death_counter += 1

    #def increase_score(self):
    #    self.score +=1

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', False, 'White')
        text_rect = text.get_rect(topright = (SCREEN_WIDTH - 30, 30))
        self.screen.blit(text, text_rect)