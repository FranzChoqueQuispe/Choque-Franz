import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.evolution import Evolution
from game.utils.constants import SPACESHIP_SHIELD, SPACESHIP_EVOLUTION, SHIELD_TYPE, EVOLUTION_TYPE

class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3000, 5000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_up_type = power_up.type
                game.player.power_up_time_up = power_up.start_time + self.duration

                if self.icon_power_up == 'Shield':
                    game.player.set_image(SPACESHIP_SHIELD, (65, 75))
                elif self.icon_power_up == 'Evolution':
                    game.player.set_image(SPACESHIP_EVOLUTION, (65, 75))

                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        self.icon_power_up = random.choice(['Shield', 'Evolution'])
        icon = {'Shield': Shield(), 'Evolution': Evolution()}
        power_up = icon[self.icon_power_up]
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(now + 5000, now + 10000)