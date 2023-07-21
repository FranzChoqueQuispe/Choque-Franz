import pygame

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ICON
from game.components.menu import Menu

class Counter():

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.death_counter = 0 
        self.highest_score = 0
        self.menu = Menu(self.screen, 'Press any botton to start')

    def update(self, score):
        if score > self.highest_score:
            self.highest_score = score

    def draw_game_over(self):

        if self.death_counter > 0:
            icon = pygame.transform.scale((ICON), (80, 120))
            self.screen.blit(icon, ((SCREEN_WIDTH / 2) - 50, (SCREEN_HEIGHT / 2) - 150))
            messages_type = self.messages_game_over()
            self.menu.update_message(messages_type)

    def increase_death_counter(self):
        self.death_counter += 1

    def increase_score(self):
        self.score += 1

    def messages_game_over(self):
        messages_type = ['message_restart',
                    'message_score',
                    'message_highest_score',
                    'message_total_deaths']
        return messages_type