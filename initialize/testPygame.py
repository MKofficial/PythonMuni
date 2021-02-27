#!/usr/bin/python3

"""
Author: Matthew Kriz
Module Name: testPygame
Date: 27/02/2021
"""

# import pygame module ->
import pygame

# initialize pygame module ->
pygame.init()

# initialize window and give it a size ->
size = (700, 500)
screen = pygame.display.set_mode(size)

# display a caption of the window ->
caption = "My First Game"
pygame.display.set_caption(caption)

# colors ->
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up pygame's clock ->
clock = pygame.time.Clock()

# create main loop ->
run = True
while run:

    # check for user input ->
    for event in pygame.event.get():

        # if user input is the button quit displayed above a window, then close this window ->
        if event.type == pygame.QUIT:
            run = False

    # create some random shapes ->
    pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # update the window ->
    pygame.display.flip()

    # set a limit to 60 frames per second ->
    clock.tick(60)

# once the while loop is broken, end pygame ->
pygame.quit()
