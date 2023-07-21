import pygame

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player) and bullet.owner == 'enemy':
                game.increase_death_counter()
                game.playing = False
                pygame.time.delay(500)
                break
        #checking the bullet list
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

            #checking the enemy list
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy) and bullet.owner == 'player': 
                    game.enemy_manager.enemies.remove(enemy)
                    self.player_bullets.remove(bullet)
                    game.increase_score()
    
    def draw(self, screen):
        for bullet in self.enemy_bullets:
                bullet.draw(screen)
        for bullet in self.player_bullets:
                bullet.draw(screen)

    def add_bullet(self, bullet, skill):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 2:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player': #and len(self.player_bullets) < 1000:
            self.player_bullets.append(bullet)

        if skill == 1 and bullet.owner == 'player':
             self.player_bullets.append(bullet)

    def reset(self):
         self.player_bullets = []
         self.enemy_bullets = []      
