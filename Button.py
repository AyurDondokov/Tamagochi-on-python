import pygame, sys
class Button():
    def __init__(self, screen, cord, imageWay, func):
        self.screen = screen
        self.image = pygame.image.load(imageWay)
        self.rect = self.image.get_rect()
        self.rect.x = cord[0]
        self.rect.y = cord[1]
        self.func = func
    def press(self, mouse):
        if self.rect.x <= mouse[0] <= self.rect.x + self.rect.width and self.rect.y <= mouse[1] <= self.rect.y + self.rect.height:
            self.func()
    def out(self):
        self.screen.blit(self.image, self.rect)

class ProgressBar():
    def __init__(self, screen, cord, size, color):
        self.screen = screen
        self.cord = cord
        self.size = size
        self.color = color
        self.rect = [cord[0], cord[1], self.size[0], self.size[1]]

    def out(self, value, maxValue):
        self.rect[2] = self.size[0] * (value/maxValue)
        pygame.draw.rect(self.screen, self.color, self.rect)

