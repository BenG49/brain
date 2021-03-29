"""Brein"""
import pygame

import time
import math

from brain.brain import Brain


def check_input(brain: Brain):
    """Handles user input.

    Args:
        brain (Brain): An object of the Brain class.
    """
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN and 47 < event.key < 58:
            # fire neuron number 0-9
            try:
                brain.neurons[event.key - 48].fire()
            except IndexError:
                pass


def main_display(brain: Brain, sleep_time: int=0):
    """Handles the main display of the Brain with Pygame.

    Args:
        brain (Brain): An object of the Brain class.
    """
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("Cascadia Code", 12)

    size = (400, 400)
    screen = pygame.display.set_mode((size[0], size[1]))

    # desmos is pog
    alpha = min(math.log(100*sleep_time+1)*40+1, 150)

    try:
        while True:
            check_input(brain)
            brain.update_display(screen, font)

            # Fade for visible firing
            background = pygame.Surface(screen.get_size())
            background.set_alpha(alpha)
            background.fill("black")
            screen.blit(background, (0, 0))

            pygame.display.update()

            if sleep_time > 0:
                time.sleep(sleep_time)
    except KeyboardInterrupt:
        pass

count = 6
cool_brain = Brain(False, count, 2)

IN = 0

ACLK_0 = 1
ACLK_1 = 2
BCLK_0 = 3
BCLK_1 = 4
BCLK_2 = 5

cool_brain.connect(IN, ACLK_0)
cool_brain.connect(IN, BCLK_0)

cool_brain.connect(ACLK_0, ACLK_1)
cool_brain.connect(ACLK_1, ACLK_0)

cool_brain.connect(BCLK_0, BCLK_1)
cool_brain.connect(BCLK_1, BCLK_2)
cool_brain.connect(BCLK_2, BCLK_0)

main_display(cool_brain, 1)
