import pygame

class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 0

    def draw(self, win, k):
        if self.color == 1:
            pygame.draw.rect(win, (0,0,0), (self.x*k, self.y*k, k, k))