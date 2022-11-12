import sys
from Pet import *
from Button import *
from pygame.locals import RESIZABLE

# Game values
GAME_NAME = "Tamagochi: Chicken Pet"
WIDTH = 1080
HEIGHT = 620
FPS = 60
SCREEN_COLOR = (234, 255, 208)

# Pet values
PET_HEALTH = 100
PET_HAPPY = 100
PET_MOVING_SPEED = 10
PET_FILE_WAY = "sprites/chicken.png"

# Forces
FOOD_FORCE = 15
PLAY_FORCE = 15

# Ways for files
BUTTON_PLAY_FILE_WAY = "sprites/btn_Play.png"
BUTTON_FEED_FILE_WAY = "sprites/btn_Feed.png"

# UI
BUTTON_PLAY_POS = (100, 150)
BUTTON_FEED_POS = (100, 20)
PROGRESS_BAR_HAPPY_POS = (250, 170)
PROGRESS_BAR_HEALTH_POS = (250, 40)
PROGRESS_BAR_SIZE = (350, 70)
PROGRESS_BAR_HAPPY_COLOR = (0, 205, 4)
PROGRESS_BAR_HEALTH_COLOR = (234, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

chicken = Pet(screen, PET_FILE_WAY, PET_HEALTH, PET_HAPPY)
btn_feed = Button(screen, BUTTON_FEED_POS, BUTTON_FEED_FILE_WAY, chicken.feed)
btn_play = Button(screen, BUTTON_PLAY_POS, BUTTON_PLAY_FILE_WAY, chicken.play)
pb_happy = ProgressBar(screen, PROGRESS_BAR_HAPPY_POS, PROGRESS_BAR_SIZE, PROGRESS_BAR_HAPPY_COLOR)
pb_health = ProgressBar(screen, PROGRESS_BAR_HEALTH_POS, PROGRESS_BAR_SIZE, PROGRESS_BAR_HEALTH_COLOR)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            btn_feed.press(pygame.mouse.get_pos())
            btn_play.press(pygame.mouse.get_pos())

    screen.fill(SCREEN_COLOR)
    clock.tick(FPS)

    chicken.out()
    chicken.moving_on_screen(PET_MOVING_SPEED)
    chicken.starving()
    chicken.sad()

    btn_feed.out()
    btn_play.out()

    pb_happy.out(chicken.get_happy, chicken.get_max_happy)
    pb_health.out(chicken.get_health, chicken.get_max_health)
    pygame.display.flip()
