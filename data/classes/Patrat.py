# Patrat.py
import pygame

class Patrat:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width // 8
        self.height = height // 8
        self.x_abs = x * width
        self.y_abs = y * height

        if (x + y) % 2 == 0:
            self.color = (87, 36, 25)
        else:
            self.color = (228, 213, 207)


        self.rect = pygame.Rect(
            self.x_abs,
            self.y_abs,
            self.width,
            self.height
       )


