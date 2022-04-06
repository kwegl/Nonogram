import pygame
from grid import Grid
from square import Square
from text import Text
pygame.init()



def renderImage(text, win, k, columnLines, rowLines, grid, WIDTH, HEIGHT):
    columnSurfaces, rowSurfaces = text.makeSurfaces(columnLines, rowLines, k)
    maxC, maxR = text.getMax(columnSurfaces, rowSurfaces)
    WIDTH += maxR
    HEIGHT += maxC
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    win.fill((255,255,255))
    text.draw(win, k, columnSurfaces, rowSurfaces, maxC, maxR)
    grid.draw(win, WIDTH, HEIGHT, k, maxC, maxR)
    pygame.image.save(win, "grid.png")
    pygame.display.update()


def count(x, y, squares):
    columns = [[] for _ in range(x)]
    rows = [[] for _ in range(y)]
    for i in range(x):
        for j in range(y):
            columns[i].append(squares[i][j].color)
            rows[j].append(squares[i][j].color)

    line = 0
    columnLines = [[] for _ in range(len(columns))]
    for i in range(len(columns)):
        for j in range(len(columns[i])):
            if columns[i][j] == 1:
                line += 1
                if j == len(columns[i])-1:
                    columnLines[i].append(line)
                    line = 0
            elif line != 0:
                columnLines[i].append(line)
                line = 0

    line = 0
    rowLines = [[] for _ in range(len(rows))]
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == 1:
                line += 1
                if j == len(rows[i])-1:
                    rowLines[i].append(line)
                    line = 0
            elif line != 0:
                rowLines[i].append(line)
                line = 0
    return columnLines, rowLines
                

def redraw(win, WIDTH, HEIGHT, k, grid, x, y, squares):
    win.fill((255,255,255))
    mouseButton = pygame.mouse.get_pressed()
    mx, my = pygame.mouse.get_pos()
    mx = mx // k
    my = my // k
    if mouseButton[0]:
        squares[mx][my].color = 1
    elif mouseButton[2]:
        squares[mx][my].color = 0

    for i in range(x):
        for j in range(y):
            squares[i][j].draw(win, k)

    grid.draw(win, WIDTH, HEIGHT, k)
    pygame.display.update()


def main():
    
    x, y = input("grid size X×Y: ").split(' ')
    x = int(x)
    y = int(y)
    k = int(input("square size: "))
    grid = Grid(x, y)
    squares = [[Square(i, j) for j in range(y)] for i in range(x)]
    text = Text(k)
    
    WIDTH = x*k+2
    HEIGHT = y*k+2
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Nonogram')
    clock = pygame.time.Clock()

    run = True
    while run:

        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_SPACE]:
            if not hold:
                hold = True
                for i in range(x):
                    for j in range(y):
                        squares[i][j].color = abs(squares[i][j].color-1)

        else:
            hold = False
            
        
        if keys[pygame.K_RETURN]:
            pygame.image.save(win, "solution.png")
            columnLines, rowLines = count(x, y, squares)
            renderImage(text, win, k, columnLines, rowLines, grid, WIDTH, HEIGHT)
            pygame.time.delay(1000)
            run = False

        redraw(win, WIDTH, HEIGHT, k, grid, x, y, squares)
        clock.tick(30)

main()