from importlib.resources import Package
import pygame
from .player import player
from .obstacle import obstacle

pygame.init()

class game:
    def __init__(self):
        self.isPalying = False
        self.J1 = player(pygame.image.load('GAME/source/vaiseauV3.png'), 400, 400)
        self.J2 = player(pygame.image.load('GAME/source/J1vaiseauV2.png'), 400, 0)
        self.Obstacle = obstacle()
        self.pressed = {}
    
    def checkCollision(self, sprite, groupe):
        return pygame.sprite.spritecollide(sprite, groupe, False, pygame.sprite.collide_mask)
    
    def update(self, screen):

        screen.blit(self.J1.image, self.J1.rect)

        screen.blit(self.J2.image, self.J2.rect)

        screen.blit(self.Obstacle.image, self.Obstacle.rect)

        for projectile in self.J1.allProjectiles:
            projectile.move(1)
    
        for projectile in self.J2.allProjectiles:
            projectile.move(-1)

        self.J1.allProjectiles.draw(screen)
        self.J2.allProjectiles.draw(screen)
    
        if pygame.sprite.spritecollide(self.Obstacle, self.J1.allProjectiles, False, pygame.sprite.collide_mask):
            print("hit")
            print(self.Obstacle.health)
            self.Obstacle.gotHit()
            self.J1.allProjectiles.empty()
            if self.Obstacle.health == 0:
                self.Obstacle.kill()
                self.Obstacle.rect.x = 100000
    
        if pygame.sprite.spritecollide(self.Obstacle, self.J2.allProjectiles, False, pygame.sprite.collide_mask):
            print("hit")
            print(self.Obstacle.health)
            self.Obstacle.gotHit()
            self.J2.allProjectiles.empty()
            if self.Obstacle.health == 0:
                self.Obstacle.kill()
                self.Obstacle.rect.x = 100000

        if pygame.sprite.spritecollide(self.J2, self.J1.allProjectiles, False, pygame.sprite.collide_mask):
            print("hit")
            print(self.J2.health)
            self.J1.score += 50
            print("J1 score: " + str(self.J1.score))
            self.J2.gotHit()
            self.J1.allProjectiles.empty()
    
        if pygame.sprite.spritecollide(self.J1, self.J2.allProjectiles, False, pygame.sprite.collide_mask):
            print("hit")
            print(self.J1.health)
            self.J2.score += 50
            print("J2 score: " + str(self.J2.score))
            self.J1.gotHit()
            self.J2.allProjectiles.empty()

        pygame.display.flip()

        if self.J1.health == 0:
            self.J2.maxScore = 100 + self.J2.score
            self.J2.score = 0
            print("J2 wins, and his score is: " + str(self.J2.maxScore))
            open = False

        if self.J2.health == 0:
            self.J1.maxScore = 100 + self.J1.score
            self.J1.score = 0
            print("J1 wins, and his score is: " + str(self.J1.maxScore))
            open = False

        if self.pressed.get(pygame.K_UP) and self.J1.rect.y > 0:
            self.J1.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.J1.rect.y < screen.get_height() - self.J1.rect.height:
            self.J1.move_down()
        elif self.pressed.get(pygame.K_LEFT) and self.J1.rect.x > 0:
            self.J1.move_left()
        elif self.pressed.get(pygame.K_RIGHT) and self.J1.rect.x < screen.get_width() - self.J1.rect.width:
            self.J1.move_right()

        if self.pressed.get(pygame.K_z) and self.J2.rect.y > 0:
            self.J2.move_up()
        elif self.pressed.get(pygame.K_s) and self.J2.rect.y < screen.get_height() - self.J2.rect.height:
            self.J2.move_down()
        elif self.pressed.get(pygame.K_q) and self.J2.rect.x > 0:
            self.J2.move_left()
        elif self.pressed.get(pygame.K_d) and self.J2.rect.x < screen.get_width() - self.J2.rect.width:
            self.J2.move_right()    

        self.J1.allProjectiles.draw(screen)
        