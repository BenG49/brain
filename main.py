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
    alpha = math.log(100*sleep_time+1)*40+1

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

num = (100, 3)
cool_brain = Brain(False, num[0], num[1])

CLK_START = 0
CLK = 10

IN = 1

OUT_1 = num[0]
OUT_2 = num[0]+1
OUT_3 = num[0]+2

DELAY_START = 11
DELAY_END = 80

INTERMEDIATE = DELAY_END+1

cool_brain.connect(CLK_START, CLK)
cool_brain.connect(CLK, CLK_START)

cool_brain.connect(IN, OUT_1)

# delay
for i in range(DELAY_START, DELAY_END):
    cool_brain.connect(i, i+1)

cool_brain.connect(OUT_1, DELAY_START)
cool_brain.connect(OUT_1, OUT_3, -1) # inhibit output 3

cool_brain.connect(OUT_2, INTERMEDIATE)
cool_brain.connect(INTERMEDIATE, OUT_2, -1) # inhibit output 2
cool_brain.connect(INTERMEDIATE, DELAY_START)

cool_brain.connect(DELAY_END, OUT_2)
cool_brain.connect(DELAY_END, OUT_3)

main_display(cool_brain, 0.01)
