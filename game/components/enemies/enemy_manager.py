import random

from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.list_enemies = [ENEMY_1, ENEMY_2, ENEMY_3]
    
    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
                
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        
    def add_enemy(self):
        if len(self.enemies) < 4:
            image = random.choice(self.list_enemies)
            enemy_width = random.randint(40,70)
            enemy_height = random.randint(40, 70)
            speed_on_x = random.randint(3,6)
            speed_on_y = random.randint(1,6)
            enemy = Enemy(image, enemy_width, enemy_height, speed_on_x, speed_on_y)
            self.enemies.append(enemy)

    def reset(self):
        self.enemies = []
