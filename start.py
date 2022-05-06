import pygame
from GAME.screen.start_menu import main_menu
from GAME.object.game import game


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
                            game.update(screen)
                        else:
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
