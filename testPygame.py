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

    screen.blit(game.J1.image, game.J1.rect)

    screen.blit(game.J2.image, game.J2.rect)

    screen.blit(game.Obstacle.image, game.Obstacle.rect)

    for projectile in game.J1.allProjectiles:
        projectile.move(1)
    
    for projectile in game.J2.allProjectiles:
        projectile.move(-1)

    game.J1.allProjectiles.draw(screen)
    game.J2.allProjectiles.draw(screen)
    
    if pygame.sprite.spritecollide(game.Obstacle, game.J1.allProjectiles, False, pygame.sprite.collide_mask):
        print("hit")
        print(game.Obstacle.health)
        game.Obstacle.gotHit()
        game.J1.allProjectiles.empty()
        if game.Obstacle.health == 0:
            game.Obstacle.kill()
            game.Obstacle.rect.x = 100000
    
    if pygame.sprite.spritecollide(game.Obstacle, game.J2.allProjectiles, False, pygame.sprite.collide_mask):
        print("hit")
        print(game.Obstacle.health)
        game.Obstacle.gotHit()
        game.J2.allProjectiles.empty()
        if game.Obstacle.health == 0:
            game.Obstacle.kill()
            game.Obstacle.rect.x = 100000

    if pygame.sprite.spritecollide(game.J2, game.J1.allProjectiles, False, pygame.sprite.collide_mask):
        print("hit")
        print(game.J2.health)
        game.J1.score += 50
        print("J1 score: " + str(game.J1.score))
        game.J2.gotHit()
        game.J1.allProjectiles.empty()
    
    if pygame.sprite.spritecollide(game.J1, game.J2.allProjectiles, False, pygame.sprite.collide_mask):
        print("hit")
        print(game.J1.health)
        game.J2.score += 50
        print("J2 score: " + str(game.J2.score))
        game.J1.gotHit()
        game.J2.allProjectiles.empty()

    pygame.display.flip()

    if game.J1.health == 0:
        game.J2.maxScore = 100 + game.J2.score
        game.J2.score = 0
        print("J2 wins, and his score is: " + str(game.J2.maxScore))
        open = False

    if game.J2.health == 0:
        game.J1.maxScore = 100 + game.J1.score
        game.J1.score = 0
        print("J1 wins, and his score is: " + str(game.J1.maxScore))
        open = False

    if game.pressed.get(pygame.K_UP) and game.J1.rect.y > 0:
        game.J1.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.J1.rect.y < screen.get_height() - game.J1.rect.height:
        game.J1.move_down()
    elif game.pressed.get(pygame.K_LEFT) and game.J1.rect.x > 0:
        game.J1.move_left()
    elif game.pressed.get(pygame.K_RIGHT) and game.J1.rect.x < screen.get_width() - game.J1.rect.width:
        game.J1.move_right()

    if game.pressed.get(pygame.K_z) and game.J2.rect.y > 0:
        game.J2.move_up()
    elif game.pressed.get(pygame.K_s) and game.J2.rect.y < screen.get_height() - game.J2.rect.height:
        game.J2.move_down()
    elif game.pressed.get(pygame.K_q) and game.J2.rect.x > 0:
        game.J2.move_left()
    elif game.pressed.get(pygame.K_d) and game.J2.rect.x < screen.get_width() - game.J2.rect.width:
        game.J2.move_right()    

    game.J1.allProjectiles.draw(screen)
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

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        

pygame.quit()
quit()