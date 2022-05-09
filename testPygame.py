from shutil import move
from turtle import Screen
import pygame
from GAME.object.game import game
from GAME.screen.start_menu import main_menu

pygame.init()

screen = pygame.display.set_mode((800, 480))
pygame.display.update()
backgroud = pygame.image.load('GAME/source/BG2V2.jpg')

game = game()

clock = pygame.time.Clock()


open = True
while open:

    #arriere plan
    screen.blit(backgroud, (0, 0))

    if game.isPalying:
        game.update(screen)
    else:
        open = False

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.J1.lightShoot()
            elif event.key == pygame.K_TAB:
                game.J2.lightShoot()
            elif event.key == pygame.K_RCTRL:
                game.J1.heavyShoot()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False        

pygame.quit()
quit()