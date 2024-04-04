import pygame
from pygame.locals import *
import random

pygame.init()

# create the window
width = 600
height = 600
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Racer')

# colors
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)


#game settings
gameover = False
speed = 2
score = 0

#game loop
clock = pygame.time.Clock()
fps = 120
runnung = True
while runnung:

    clock.tick(fps)
    for  event in pygame.event.get():
        if event.type == QUIT:
            running = False

            # draw the grass
            screen.fill(green)
            pygame.display.update()
            pygame.quit()