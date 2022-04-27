from importlib.resources import Package
import pygame
from .player import player

pygame.init()

class game:
    def __init__(self):
        self.player = player()
        self.pressed = {}
