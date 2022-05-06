import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.speed = 2
        self.firepower = 1
        self.image = pygame.image.load('GAME/source/shootUpSpriteV2.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + player.rect.width / 2 - self.rect.width / 2
        self.rect.y = player.rect.y

    def move(self, direction):
        self.rect.y -= self.speed * direction
        
        if self.rect.y < 0 and self.rect.y > -50:
            self.kill()