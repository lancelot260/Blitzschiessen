from asyncio import events
import pygame
from .projectile import Projectile
from .obstacle import Obstacle

class Player(Obstacle):

    def __init__(self, image, vecX, vecY):
        super().__init__()
        self.health_max = 4
        self.health = self.health_max
        self.speed = 2
        self.score = 0
        self.maxScore = 0
        self.dashCD = pygame.time.Clock()
        self.allProjectiles = pygame.sprite.Group()
        self.image = image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.x = vecX
        self.rect.y = vecY
        self.original_image = self.image

    def lightShoot(self):
        firepower = 1
        speed = 2
        self.allProjectiles.add(Projectile(self, firepower, speed,'GAME/source/shootUpSpriteV2.png'))
    
    def heavyShoot(self):
        firepower = 2
        speed = 0.5
        self.allProjectiles.add(Projectile(self, firepower, speed,'GAME/source/heavyShootJ1.png'))

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed
    
    def move_left(self):
        self.rect.x -= self.speed
    
    def move_right(self):
        self.rect.x += self.speed
    
    def dash(self, clock):
        cooldownTracker += clock.get_time()
        if cooldownTracker > 4000:
            self.rect.x += 10
