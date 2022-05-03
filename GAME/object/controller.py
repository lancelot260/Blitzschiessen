import pygame

class Controller:
    def __init__(self, id):
        self.joystick = pygame.joystick.Joystick(id)
        self.button_list = []
        self.axes_list = []

    def add_button(self, button):
        self.button_list.append(button)
    
    def add_axis(self, axis):
        self.axes_list.append(axis)

    def get_axes_number(self):
        return self.joystick.get_numaxes()

    def get_button_number(self):
        return self.joystick.get_numbuttons()
    
    def get_axes_value(self, axes):
        axes_value = self.joystick.get_axis(axes)
        return axes_value

    def get_button_value(self, button):
        button_value = self.joystick.get_button(button)
        return button_value
