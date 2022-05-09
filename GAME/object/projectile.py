from email.mime import image
import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player, firepower, speed, sprite):
        super().__init__()
        self.speed = speed
        self.firepower = firepower
        self.image = pygame.image.load(sprite)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width / 2 - self.rect.width / 2
        self.rect.y = player.rect.y

    def move(self, direction):
        self.rect.y -= self.speed * direction