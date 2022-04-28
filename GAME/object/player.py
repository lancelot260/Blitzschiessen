from re import I
import pygame
from .projectile import Projectile
from .obstacle import obstacle

class player(obstacle):

    def __init__(self, image, vecX, vecY):
        super().__init__()
        self.health = 4
        self.health_max = 4
        self.speed = 2
        self.score = 0
        self.maxScore = 0
        self.allProjectiles = pygame.sprite.Group()
        self.image = image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = vecX
        self.rect.y = vecY
        self.original_image = self.image
        self.angle = 0

    def lightShoot(self):
        self.allProjectiles.add(Projectile(self))  

    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed
    