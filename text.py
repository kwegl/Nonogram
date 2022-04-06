import pygame

class Text:
    def __init__(self, k):
        self.font = pygame.font.SysFont("Arial", k-1)

    def makeSurfaces(self, columnLines, rowLines, k):
        columnSurfaces = []
        for i in range(len(columnLines)):
            if len(columnLines[i]) != 0:
                surface = pygame.Surface((k, len(columnLines[i])*k))
            else:
                surface = pygame.Surface((1, 1))
            surface.fill((255,255,255))

            for j in range(len(columnLines[i])):
                text = self.font.render(str(columnLines[i][j]), False, (0,0,0))
                surface.blit(text, (2, j*k))
            columnSurfaces.append(surface)
        
        rowSurfaces = []
        for i in range(len(rowLines)):
            if len(rowLines[i]) != 0:
                surface = pygame.Surface((len(rowLines[i])*k, k))
            else:
                surface = pygame.Surface((1, 1))
            surface.fill((255,255,255))

            for j in range(len(rowLines[i])):
                text = self.font.render(str(rowLines[i][j]), False, (0,0,0))
                surface.blit(text, (j*k, 0))
            rowSurfaces.append(surface)

        return columnSurfaces, rowSurfaces

    def getMax(self, columnSurfaces, rowSurfaces):
        maxColumnHeight = 0
        maxRowWidth = 0
        for s in columnSurfaces:
            if s.get_height() > maxColumnHeight:
                maxColumnHeight = s.get_height()
        for s in rowSurfaces:
            if s.get_width() > maxRowWidth:
                maxRowWidth = s.get_width()
        
        return maxColumnHeight, maxRowWidth

        
    def draw(self, win, k, columnSurfaces, rowSurfaces, maxColumnHeight, maxRowWidth):
        for i in range(len(columnSurfaces)):
            win.blit(columnSurfaces[i], (maxRowWidth + i*k, 0))
        
        for i in range(len(rowSurfaces)):
            win.blit(rowSurfaces[i], (0, maxColumnHeight + i*k))

        
