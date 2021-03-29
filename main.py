"""Brein"""
import pygame

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


def main_display(brain: Brain):
    """Handles the main display of the Brain with Pygame.

    Args:
        brain (Brain): An object of the Brain class.
    """
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("Cascadia Code", 12)

    size = (400, 400)
    screen = pygame.display.set_mode((size[0], size[1]))

    try:
        while True:
            check_input(brain)
            brain.update_display(screen, font)

            # Fade for visible firing
            background = pygame.Surface(screen.get_size())
            background.set_alpha(1)
            background.fill("black")
            screen.blit(background, (0, 0))

            pygame.display.update()
    except KeyboardInterrupt:
        pass


cool_brain = Brain(False, 3, 1)
cool_brain.connect(0, 1)
cool_brain.connect(1, 2)
cool_brain.connect(2, 3)

cool_brain.connect(0, 2, -1)

main_display(cool_brain)

# clock, output=2, fire 0 to start
# cool_brain.connect(0, 1)
# cool_brain.connect(1, 0)
# cool_brain.connect(1, 2, 0.001)
