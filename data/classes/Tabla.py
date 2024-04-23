# Tabla.py
import pygame
from .Patrat import Patrat

class Tabla:
    def __init__(self):
        self.dimensiune = 8
        self.litere = 'abcdefgh'
        self.width = 800
        self.height = 800

        pygame.init()

        self.canvas = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Chess - 2 Players")
        self.icon = pygame.image.load('data/imgs/chess.png')
        pygame.display.set_icon(self.icon)

        self.gameOn = True

        square_size = self.width // self.dimensiune

        for i in range(self.dimensiune):
            for j in range(self.dimensiune):
                # p = Patrat(i, j, self.width, self.height)
                # pygame.draw.rect(self.canvas, p.color, p.rect)
                x_abs = i * square_size  # Calculate the absolute x position of the square
                y_abs = j * square_size  # Calculate the absolute y position of the square
                p = Patrat(i, j, square_size, square_size)  # Create a Patrat instance
                pygame.draw.rect(self.canvas, p.color, (x_abs, y_abs, square_size, square_size))  # Draw the square



        while self.gameOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOn = False
            pygame.display.update()


