import pygame

from game.utils.constants import SHIELD_TYPE

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player) and bullet.owner == 'enemy':
                if game.player.power_up_type != SHIELD_TYPE:
                    game.death_counter.update()
                    game.playing = False
                    pygame.time.delay(500)
                    break
        #checking the bullet list
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

            #checking the enemy list
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy) and (bullet.owner == 'shoot_2' or bullet.owner == 'shoot_1'):
                    game.enemy_manager.enemies.remove(enemy)
                    self.player_bullets.remove(bullet)
                    game.score.update()
    
    def draw(self, screen):
        for bullet in self.enemy_bullets:
                bullet.draw(screen)
        for bullet in self.player_bullets:
                bullet.draw(screen)

    def add_bullet(self, bullet, skill):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 2:
            self.enemy_bullets.append(bullet)
        if bullet.owner == 'shoot_2' or bullet.owner == 'shoot_1':
            self.player_bullets.append(bullet)

        if skill == 1 and bullet.owner == 'shoot_2' or bullet.owner == 'shoot_1':
            self.player_bullets.append(bullet)    

    def reset(self):
         self.player_bullets = []
         self.enemy_bullets = []      
