from importlib.resources import Package
import pygame
from .player import player
from .obstacle import obstacle

pygame.init()

class game:
    def __init__(self):
        self.J1 = player(pygame.image.load('GAME/source/vaiseauV3.png'), 400, 400)
        self.J2 = player(pygame.image.load('GAME/source/J1vaiseauV2.png'), 400, 0)
        self.Obstacle = obstacle()
        self.pressed = {}
    
    def checkCollision(self, sprite, groupe):
        return pygame.sprite.spritecollide(sprite, groupe, False, pygame.sprite.collide_mask)

