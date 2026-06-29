from tkinter import Menu

import pygame

from code.Const import WINDOW_HEIGHT, WINDOW_WIDTH
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
         while True:
            menu = Menu(self.window)
            menu.run()
            pass


