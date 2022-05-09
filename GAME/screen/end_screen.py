import pygame
from BDD.integration.game_controller import game_controller
import sqlite3
from sqlite3 import Error
import math

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    finally:
        return conn

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

class end_screen:
    def __init__(self, J_winner, J_loser, score_winner, score_loser):
        self.highscore = []
        self.winner = J_winner
        self.loser = J_loser
        self.score_winner = score_winner
        self.score_loser = score_loser
        self.button_list = []

    def prep_highscore(self):
        high_score = game_controller.get_best_game(create_connection("migration.db"))
        for i in high_score:
            self.highscore.append(i)
    
    def check_end_screen_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for button in self.button_list:
                if button.rect.collidepoint(mouse_x, mouse_y):
                    return True, button.text
        return False

    def draw_end_screen(self, screen):
        self.prep_highscore()
        font = pygame.font.SysFont(None, 30)
        restart_button = button('R', math.ceil(self.screen.get_width()/2.55), 180, 'GAME/source/button_start_1.jpg')
        self.button_list.append(restart_button)
        for i in self.highscore:
            text = font.render(i[0], True, (255, 255, 255))
            screen.blit(text, (50, i[1]))
        for button in self.button_list:
            screen.blit(button.sprite, button.rect)




        