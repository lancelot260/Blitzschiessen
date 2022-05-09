from unittest import result
import pygame
from GAME.screen.start_menu import main_menu
from GAME.object.game import game
from BDD.integration.game_controller import game_controller
from GAME.screen.end_screen import end_screen
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    finally:
        return conn

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((800, 480))
    bg_image = pygame.image.load('GAME/source/bg.jpg')
    bg_image = pygame.transform.scale(bg_image, (800, 480))
    start_menu = main_menu(screen)
    screen.blit(bg_image, (0, 0))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if start_menu.check_main_menu_events(event):
                if start_menu.check_main_menu_events(event)[1] == 'Start':
                    start = True
                    game = game()
                    backgroud = pygame.image.load('GAME/source/BG2V2.jpg')
                    clock = pygame.time.Clock()
                    while start == True:
                        screen.blit(backgroud, (0, 0))

                        if game.isPalying:

                            resultat = game.end()
                            game_controller.create_game(create_connection("migration.db"),'blue', 'red', resultat[0], resultat[1])
                            if game.J1.score > game.J2.score:
                                J_winner = game.J1
                                J_winner.name = 'J1'
                                J_winner.score = game.J1.score
                                J_looser = game.J2
                                J_looser.name = 'J2'
                                J_looser.score = game.J2.score
                            else:
                                J_winner = game.J2
                                J_winner.name = "J2"
                                J_winner.score = game.J2.score
                                J_looser = game.J1
                                J_looser.name = "J1"
                                J_looser.score = game.J1.score
                            end = end_screen(J_winner.name, J_looser.name, J_winner.score, J_looser.score)

                            if end.check_end_screen_events(event):
                                if end.check_end_screen_events(event)[1] == 'Quit':
                                    start = False
                                    pygame.quit()
                                    quit()
                                if end.check_end_screen_events(event)[1] == 'Restart':
                                    start = True

                        else:
                            bg_image = pygame.image.load('GAME/source/bg.jpg')
                            bg_image = pygame.transform.scale(bg_image, (800, 480))
                            screen.blit(bg_image, (0, 0))
                            pygame.display.flip()
                            start = False
                        
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
                                    game.J1.dash(clock)

                            elif event.type == pygame.KEYUP:
                                game.pressed[event.key] = False  

                elif start_menu.check_main_menu_events(event)[1] == 'Settings':
                    print('Settings')

            start_menu.draw_main_menu()
            pygame.display.flip()
