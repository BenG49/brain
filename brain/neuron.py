"""Neuron class file."""
from __future__ import annotations

import random

import pygame


class Neuron:
    """Neuron class file."""
    def __init__(self, brain, neuron_id: int) -> None:
        """Initiates a Neuron object.

        Args:
            brain (Brain): A Brain object of the brain that the neuron belongs
            to.
            neuron_id (int): The ID of the neuron in the brain.
        """
        self.brain = brain
        self.neuron_id = neuron_id

        self.state = 0
        self.links = {}
        self.pos = (random.random(), random.random())

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
        self.state = 1

    def update(self) -> None:
        """Updates a neuron and its connections' states."""
        if self.state >= 1:
            for neuron_id, weight in self.links.items():
                self.brain.neurons[neuron_id].state += weight

            self.state = 0

    def update_display(self, screen, font) -> None:
        """Updates a neuron and its connections' states, draws neuron to screen.

        Args:
            screen (pygame.display): A pygame display.
            font (pygame.font): A pygame font.
        """
        width, height = screen.get_size()
        pos = (self.pos[0] * width, self.pos[1] * height)

        # neuron circle
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), pos, 1)

        # label
        if font:
            label = font.render(str(self.neuron_id), False, (255, 255, 255))
            screen.blit(label, pos)

        # neuron is firing
        if self.state >= 1:
            pygame.draw.circle(screen, pygame.Color(255, 255, 255), pos, 3)

            for neuron_id, weight in self.links.items():
                neuron = self.brain.neurons[neuron_id]
                neuron.state += weight

                pygame.draw.line(screen, pygame.Color(
                    255, 255, 255),
                    pos,
                    (neuron.pos[0] * width, neuron.pos[1] * height)
                )

            self.state = 0
