import pygame

class obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.MaxHealth = 3
        self.image = pygame.image.load('GAME/source/obstacleV2.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500