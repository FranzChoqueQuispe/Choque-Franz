import pygame

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_STYLE

class Menu:
    SCREEN_HALF_HEIGHT = SCREEN_HEIGHT / 2
    SCREEN_HALF_WIDTH = SCREEN_WIDTH / 2
    SPACE_LINES = 30
    MESSAGE_TYPES = {'message_restart': SCREEN_HALF_HEIGHT,
                     'message_score': SCREEN_HALF_HEIGHT + SPACE_LINES,
                     'message_highest_score': SCREEN_HALF_HEIGHT + 2 * SPACE_LINES,
                     'message_total_deaths': SCREEN_HALF_HEIGHT + 3 * SPACE_LINES}
    MESSAGE = {'message_restart': 'Game Over: Press any key to restart',
                'message_score': 'Your Score: ',
                'message_highest_score': 'Heighest Score',
                'message_total_deaths': 'Total Deaths:'}
    count = 0

    def __init__(self, screen, message):
        self.reset_screen(screen)
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, False, 'Black')
        self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, self.SCREEN_HALF_HEIGHT)) 
        self.message = message

    def update(self, game):
        pygame.display.update()
        self.handle_events(game)

    def draw(self, screen):
        screen.blit(self.text, self.rect)

    def handle_events(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            if event.type == pygame.KEYDOWN:
                game.run()
    
    def reset_screen(self, screen):
        screen.fill('White')

    def update_message(self, messages_type):
            while self.count<5000:
                self.count += 1
                for message_type in messages_type:
                    height_message = self.MESSAGE_TYPES[message_type]
                    message = self.MESSAGE[message_type]
                    #self.SPACE_LINES += 0.4
                    self.text = self.font.render(message, False, 'Black')
                    self.rect = self.text.get_rect(center = (self.SCREEN_HALF_WIDTH, height_message)) #+ self.SPACE_LINES))

                

