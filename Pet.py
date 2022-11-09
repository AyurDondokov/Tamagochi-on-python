import pygame

WIDTH = 1080
HEIGHT = 620

STARVE_SPEED = 1 / 60 * 30
SAD_SPEED = 1 / 60 * 30
FEED_FORCE = 15
PLAY_FORCE = 15


class Pet:
    def __init__(self, screen, image_way, health, happy):
        self.__screen = screen
        self.__image = pygame.image.load(image_way)
        self.__rect = self.__image.get_rect()
        self.__rect.x = WIDTH/2
        self.__rect.y = HEIGHT/2
        self.__max_happy = happy
        self.__max_health = health
        self.__happy = happy
        self.__health = health
        self.__direction_of_move = 1
        self.__is_live = True

    def out(self):
        self.__screen.blit(self.__image, self.__rect)

    def die(self, title):
        if self.__is_live:
            self.__is_live = False
            self.__image = pygame.transform.flip(self.__image, False, True)
            print(title)

    def starving(self):
        if self.__is_live:
            if self.__health <= 0:
                self.die("OMG. You forget feed it.")
            else:
                self.__health -= STARVE_SPEED

    @property
    def get_health(self):
        return self.__health

    @property
    def get_happy(self):
        return self.__happy

    @property
    def get_max_health(self):
        return self.__max_health

    @property
    def get_max_happy(self):
        return self.__max_happy

    def sad(self):
        if self.__is_live:
            if self.__happy <= 0:
                self.die("OMG. It dies from cringe.")
            else:
                self.__happy -= SAD_SPEED

    def feed(self):
        if self.__is_live:
            if FEED_FORCE+self.__health <= self.__max_health:
                self.__health += FEED_FORCE
            else:
                self.__health = self.__max_health
            print("Health: ", self.__health)
        else:
            print("It dies. You can't feed it.")

    def play(self):
        if self.__is_live:
            if FEED_FORCE + self.__happy <= self.__max_happy:
                self.__happy += PLAY_FORCE
            else:
                self.__happy = self.__max_happy
            print("Happy: ", self.__happy)
        else:
            print("YOU CAN'T PLAY WITH DEAD BODY.")

    def moving_on_screen(self, speed):
        if self.__is_live:
            if self.__rect.x + self.__rect.width >= WIDTH or self.__rect.x <= 0:
                self.__direction_of_move *= -1
                self.__image = pygame.transform.flip(self.__image, True, False)
            self.__rect.x += speed * self.__direction_of_move
