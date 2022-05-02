import math
from numpy import append
import pygame

class button:
    def __init__(self, text, x, y, sprite):
        self.text = text
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, (160, 60))
        self.rect = self.sprite.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        

class main_menu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.button_list = []
        self.font = pygame.font.SysFont(None, 48)
        self.prep_main_menu()

    def prep_main_menu(self):
        #2.45 nous permet de centrer le bouton ne largeur
        start_button = button('Start', math.ceil(self.screen.get_width()/2.45), 180, 'GAME/source/button_start_1.jpg')
        setting_button = button('Settings', math.ceil(self.screen.get_width()/2.45), 270, 'GAME/source/button_settingV3.png')
        self.button_list.append(start_button)
        self.button_list.append(setting_button)

    def check_main_menu_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for button in self.button_list:
                if button.rect.collidepoint(mouse_x, mouse_y):
                    return True, button.text
        return False

    def draw_main_menu(self):
        for button in self.button_list:
            self.screen.blit(button.sprite, button.rect)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    main_menu = main_menu(screen)
    while True:
        for event in pygame.event.get():
            main_menu.draw_main_menu()
            pygame.display.flip()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if main_menu.check_main_menu_events(event):
                if main_menu.check_main_menu_events(event)[1] == 'Start':
                    print('Start')
                elif main_menu.check_main_menu_events(event)[1] == 'Settings':
                    print('Settings')
        
        