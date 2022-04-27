import pygame
from .projectile import Projectile

class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 4
        self.health_max = 4
        self.speed = 2
        self.fire = 5
        self.allProjectiles = pygame.sprite.Group()
        self.image = pygame.image.load('GAME/source/vaiseauV3.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
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
    