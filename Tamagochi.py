import pygame, math, sys
import random
import Controls
from Pet import *
from Button import *

WIDTH = 1080
HEIGHT = 620
FPS = 60

#Pet values
petHealth = 100
petHappy = 100

#Forces
FoodForce = 15
PlayForce = 15

#Ways for files
btnPlayWay = "sprites/btn_Play.png"
btnFeedWay = "sprites/btn_Feed.png"

#Position for UI
btnPlayPos = (100, 150)
btnFeedPos = (100, 20)
PBHappyPos = (250, 170)
PBHealthPos = (250, 40)

PBSize = (350, 70)

PBHappyColor = (0, 205, 4)
PBHealthColor = (234, 0, 0)

def Run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chicken Pet!")
    clock = pygame.time.Clock()

    screenColor = (234, 255, 208)

    chik = Pet(screen, "sprites/chicken.png", petHealth, petHappy)
    btn_Feed = Button(screen, btnFeedPos, btnFeedWay, chik.feed)
    btn_Play = Button(screen, btnPlayPos, btnPlayWay, chik.play)
    pb_Happy = ProgressBar(screen, PBHappyPos, PBSize, PBHappyColor)
    pb_Health = ProgressBar(screen, PBHealthPos, PBSize, PBHealthColor)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                btn_Feed.press(pygame.mouse.get_pos())
                btn_Play.press(pygame.mouse.get_pos())

        screen.fill(screenColor)
        clock.tick(FPS)

        chik.out()
        chik.moveTo(10)
        chik.straving()
        chik.sading()

        btn_Feed.out()
        btn_Play.out()

        pb_Happy.out(chik.getHappy, chik.getMaxHappy)
        pb_Health.out(chik.getHealth, chik.getMaxHealth)
        pygame.display.flip()



Run()

pygame.quit()