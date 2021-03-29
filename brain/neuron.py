"""Neuron class file."""
from __future__ import annotations

import random

import pygame


class Neuron:
    """Neuron class file."""
    def __init__(self, brain, neuron_id: int, pos: tuple=None) -> None:
        """Initiates a Neuron object.

        Args:
            brain (Brain): A Brain object of the brain that the neuron belongs
            to.
            neuron_id (int): The ID of the neuron in the brain.
            pos (tuple): A tuple representing a screen position from 0 to 1.
        """
        self.brain = brain
        self.neuron_id = neuron_id

        self.charge = 0
        self.links = {}
        self.pos = pos if pos else (random.random(), random.random())

    def connect(self, neuron: Neuron, weight: float) -> None:
        """Establishes a connection to another neuron.

        Args:
            neuron (Neuron): An object of the Neuron class.
            weight (float): The strength of the connection.
        """
        self.links[neuron.neuron_id] = weight

    def disconnect(self, neuron: Neuron) -> None:
        """Closes the connection from another neuron.

        Args:
            neuron (Neuron): An object of the Neuron class.
        """
        self.links.pop(neuron.neuron_id)

    def fire(self) -> None:
        """Fires a neuron."""
        self.charge = 1

    def update(self) -> None:
        """Updates a neuron and its connections' charges."""
        if self.charge >= 1:
            for neuron_id, weight in self.links.items():
                self.brain.neurons[neuron_id].charge += weight

        if self.charge > 0:
            self.charge = 0

    def update_display(self, screen, font) -> None:
        """Updates a neuron and its connections' charges, draws neuron to screen.

        Args:
            screen (pygame.display): A pygame display.
            font (pygame.font): A pygame font.
        """
        width, height = screen.get_size()
        pos = (self.pos[0] * width, self.pos[1] * height)

        # neuron circle
        pygame.draw.circle(screen, "white", pos, 1)

        # label
        if font:
            label = font.render(str(self.neuron_id), False, "white")
            screen.blit(label, pos)

        # neuron is firing
        if self.charge >= 1:
            pygame.draw.circle(screen, "white", pos, 3)

            for neuron_id, weight in self.links.items():
                neuron = self.brain.neurons[neuron_id]
                neuron.charge += weight

                if type(neuron) != OutputNeuron:
                    pygame.draw.line(screen,
                        "white",
                        pos,
                        (neuron.pos[0] * width, neuron.pos[1] * height)
                    )

        # only reset to resting state if not inhibitive
        if self.charge > 0:
            self.charge = 0

class OutputNeuron(Neuron):
    def __init__(self, brain, neuron_id: int, output_id: int):
        super(OutputNeuron, self).__init__(brain, neuron_id)

        self.output_id = output_id

    # NOTE: font unused
    def update_display(self, screen, font) -> None:
        """Updates a neuron and its connections' charges, draws neuron to screen.

        Args:
            screen (pygame.display): A pygame display.
        """

        # neuron is firing
        if self.charge >= 1:
            width, height = screen.get_size()
            RECT_FRAC = 10 # fraction of height/width rect will take up
            RECT_SIZE = (int(width/RECT_FRAC), int(height/RECT_FRAC))
            rect_pos = (
                width-int(RECT_SIZE[0]*int(self.output_id/RECT_FRAC))-RECT_SIZE[0],
                int(RECT_SIZE[1]*(self.output_id%RECT_FRAC))
            )

            pygame.draw.rect(screen, "white", pygame.Rect(rect_pos, RECT_SIZE), 0)

            for neuron_id, weight in self.links.items():
                self.brain.neurons[neuron_id].charge += weight


        # only reset to resting state if not inhibitive
        if self.charge > 0:
            self.charge = 0