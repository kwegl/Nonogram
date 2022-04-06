import pygame

class Grid:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win, WIDTH, HEIGHT, k, maxR=0, maxC=0):
        for i in range(self.x+1):
            if i % 5 == 0:
                size = 2
            else:
                size = 1
            pygame.draw.line(win, (100,100,100), (i*k + maxC,0), (i*k + maxC, HEIGHT), size)
        for j in range(self.y+1):
            if j % 5 == 0:
                size = 2
            else:
                size = 1
            pygame.draw.line(win, (100,100,100), (0,j*k + maxR), (WIDTH, j*k + maxR), size)