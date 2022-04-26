from turtle import Screen
import pygame

pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.update()

background = pygame.color.rgb(0,50,0)

open = True
while open:

    screen.bgcolor(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
pygame.quit()
quit()