import pygame


class Button:
    def __init__(self, screen, cord, image_way, function):
        self.__screen = screen
        self.__image = pygame.image.load(image_way)
        self.__rect = self.__image.get_rect()
        self.__rect.x = cord[0]
        self.__rect.y = cord[1]
        self._function = function

    def press(self, mouse):
        if self.__rect.x <= mouse[0] <= self.__rect.x + self.__rect.width \
                and self.__rect.y <= mouse[1] <= self.__rect.y + self.__rect.height:
            self._function()

    def out(self):
        self.__screen.blit(self.__image, self.__rect)


class ProgressBar:
    def __init__(self, screen, cord, size, color):
        self.__screen = screen
        self.__cord = cord
        self.__size = size
        self.__color = color
        self.__rect = [cord[0], cord[1], self.__size[0], self.__size[1]]

    def out(self, value, max_value):
        self.__rect[2] = self.__size[0] * (value / max_value)
        pygame.draw.rect(self.__screen, self.__color, self.__rect)

