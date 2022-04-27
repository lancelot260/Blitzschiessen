from shutil import move
from turtle import Screen
import pygame

from GAME.object.game import game

pygame.init()

screen = pygame.display.set_mode((800, 480))
pygame.display.update()
backgroud = pygame.image.load('GAME/source/BG2V2.jpg')

game = game()
#charcher le jueour


open = True
while open:

    screen.blit(backgroud, (0, 0))

    screen.blit(game.player.image, game.player.rect)

    for projectile in game.player.allProjectiles:
        projectile.move()

    game.player.allProjectiles.draw(screen)

    pygame.display.flip()

    if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y < screen.get_height() - game.player.rect.height:
        game.player.move_down()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < screen.get_width() - game.player.rect.width:
        game.player.move_right()
        

    game.player.allProjectiles.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.lightShoot()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        

pygame.quit()
quit()