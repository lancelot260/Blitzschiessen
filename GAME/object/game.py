from importlib.resources import Package
import pygame
import random
from .player import Player
from .obstacle import Obstacle

pygame.init()

class game:
    def __init__(self):
        self.isPalying = True
        self.J1 = Player(pygame.image.load('GAME/source/vaiseauV3.png'), 400, 400)
        self.J2 = Player(pygame.image.load('GAME/source/J1vaiseauV2.png'), 400, 0)
        self.round = 0
        self.J1Limite = 300
        self.J2Limite = 200
        self.allObstacles = []
        for _ in range(random.randint(5, 10)):
            obstacle = Obstacle()
            self.allObstacles.append(obstacle)
        self.pressed = {}
    
    def end(self):
        return self.J1.score, self.J2.score

    def update(self, screen):

        screen.blit(self.J1.image, self.J1.rect)

        screen.blit(self.J2.image, self.J2.rect)

        for i in self.allObstacles:
            screen.blit(i.image, i.rect)

        for projectile in self.J1.allProjectiles:
            projectile.move(1)
    
        for projectile in self.J2.allProjectiles:
            projectile.move(-1)

        self.J1.allProjectiles.draw(screen)
        self.J2.allProjectiles.draw(screen)
    
        for obstacle in self.allObstacles:
            for projectile in self.J1.allProjectiles:
                if pygame.sprite.collide_rect(projectile, obstacle):
                    print("hit obstacle")
                    print(obstacle.health)
                    obstacle.gotHit(projectile.firepower)
                    self.J1.allProjectiles.empty()
                    if obstacle.health <= 0:
                        obstacle.kill()
                        obstacle.rect.x = 100000
            for projectile in self.J2.allProjectiles:
                if pygame.sprite.collide_rect(projectile, obstacle):
                    print("hit obstacle")
                    print(obstacle.health)
                    obstacle.gotHit(projectile.firepower)
                    self.J2.allProjectiles.empty()
                    if obstacle.health <= 0:
                        obstacle.kill()
                        obstacle.rect.x = 100000
                

        if pygame.sprite.spritecollide(self.J2, self.J1.allProjectiles, False, pygame.sprite.collide_mask):
            self.J1.score += 50
            self.J2.gotHit(projectile.firepower)
            self.J1.allProjectiles.empty()
    
        if pygame.sprite.spritecollide(self.J1, self.J2.allProjectiles, False, pygame.sprite.collide_mask):
            self.J2.score += 50
            self.J1.gotHit(projectile.firepower)
            self.J2.allProjectiles.empty()

        pygame.display.flip()

        
        if self.J1.health == 0 or self.J2.health == 0:
            print("new roud")
            print("round: " + str(self.round +1))
            print("J1 health: " + str(self.J1.health))
            print("J2 health: " + str(self.J2.health))
            self.J1.rect.x = 400
            self.J1.rect.y = 400
            self.J2.rect.x = 400
            self.J2.rect.y = 0
            self.J1.allProjectiles.empty()
            self.J2.allProjectiles.empty()
            if self.J1.health == 0:
                self.J1.health = 4
                self.J2.score += 100
            elif self.J2.health == 0:
                self.J2.health = 4
                self.J1.score += 100
            self.round += 1
        
        if self.round == 3:
            self.isPalying = False
            self.end(self)
            

        if self.pressed.get(pygame.K_UP) and self.J1.rect.y > self.J1Limite:
            self.J1.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.J1.rect.y < screen.get_height() - self.J1.rect.height:
            self.J1.move_down()
        elif self.pressed.get(pygame.K_LEFT) and self.J1.rect.x > 0:
            self.J1.move_left()
        elif self.pressed.get(pygame.K_RIGHT) and self.J1.rect.x < screen.get_width() - self.J1.rect.width:
            self.J1.move_right()

        if self.pressed.get(pygame.K_z) and self.J2.rect.y > 0:
            self.J2.move_up()
        elif self.pressed.get(pygame.K_s) and self.J2.rect.y < self.J2Limite - self.J2.rect.height:
            self.J2.move_down()
        elif self.pressed.get(pygame.K_q) and self.J2.rect.x > 0:
            self.J2.move_left()
        elif self.pressed.get(pygame.K_d) and self.J2.rect.x < screen.get_width() - self.J2.rect.width:
            self.J2.move_right()    

        self.J1.allProjectiles.draw(screen)
        