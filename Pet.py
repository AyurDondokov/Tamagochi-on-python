import pygame

WIDTH = 1080
HEIGHT = 620

StraveSpeed = 1/60*30
SadSpeed = 1/60*30
FoodForce = 15
PlayForce = 15

class Pet():
    def __init__(self, screen, imageWay, __health, __happy):
        self.screen = screen
        self.image = pygame.image.load(imageWay)
        self.__rect = self.image.get_rect()
        self.__rect.x = WIDTH/2
        self.__rect.y = HEIGHT/2
        self.__maxHappy = __happy
        self.__maxHealth = __health
        self.__happy = __happy
        self.__health = __health
        self.__dirMove = 1
        self.__isLive = True

    def out(self):
        self.screen.blit(self.image, self.__rect)
    def die(self, title):
        if (self.__isLive):
            self.__isLive = False
            self.image = pygame.transform.flip(self.image, 0, 1)
            print(title)
    def straving(self):
        if (self.__isLive):
            if self.__health <= 0:
                self.die("OMG! You forget feed it!")
            else:
                self.__health -= StraveSpeed
    @property
    def getHealth(self):
        return self.__health
    @property
    def getHappy(self):
        return self.__happy

    @property
    def getMaxHealth(self):
        return self.__maxHealth
    @property
    def getMaxHappy(self):
        return self.__maxHappy

    def sading(self):
        if (self.__isLive):
            if self.__happy <= 0:
                self.die("OMG! It dies from cringe!")
            else:
                self.__happy -= SadSpeed
    def feed(self):
        if (self.__isLive):
            if (FoodForce+self.__health <= self.__maxHealth):
                self.__health += FoodForce
            else:
                self.__health = self.__maxHealth
            print("Health: ", self.__health)
        else:
            print("It dies! You can't feed it!")
    def play(self):
        if (self.__isLive):
            if (FoodForce+self.__happy <= self.__maxHappy):
                self.__happy += PlayForce
            else:
                self.__happy = self.__maxHappy
            print("Happy: ", self.__happy)
        else:
            print("YOU CAN'T PLAY WITH DEAD BODY!")

    def moveTo(self, speed):
        if (self.__isLive):
            if (self.__rect.x+self.__rect.width >= WIDTH or self.__rect.x <= 0):
                self.__dirMove *= -1
                self.image = pygame.transform.flip(self.image,1,0)
            self.__rect.x += speed * self.__dirMove