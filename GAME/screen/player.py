import pygame

class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 4
        self.health_max = 4
        self.speed = 5
        self.fire = 5
        self.image = pygame.image.load('../source/spriteTest.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed