from turtle import Screen
import pygame
from game import game

pygame.init()






screen = pygame.display.set_mode((1080, 720))
pygame.display.update()

game = game()
#charcher le jueour


open = True
while open:

    screen.blit(game.player.image, game.player.rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.player.move_up()
            elif event.key == pygame.K_DOWN:
                game.player.move_down()
            elif event.key == pygame.K_LEFT:
                game.player.move_left()
            elif event.key == pygame.K_RIGHT:
                game.player.move_right()
pygame.quit()
quit()