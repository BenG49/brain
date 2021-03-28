"""Brain class file."""
from brain.neuron import Neuron

import math


class Brain:
    """Brain class file."""
    NEURON_LABEL_THRESHOLD = 25

    def __init__(self, neuron_count: int, random_pos: bool) -> None:
        """Initiates a Brain object.

        Args:
            neuron_count (int): The number of Neuron objects that are
            initialized with the Brain object.
            random_pos (bool): To randomize the positions of the neurons.
        """
        self.neurons = []
        square_side = math.ceil(math.sqrt(neuron_count))
        for i in range(neuron_count):
            pos = None if random_pos else (
                int(i/square_side)/square_side,
                i%square_side/square_side
            )
            self.add_neuron(pos)

    def add_neuron(self, pos: tuple) -> None:
        """Adds a Neuron object to the brain."""
        self.neurons.append(Neuron(self, len(self.neurons), pos))

    def connect(self, id_a: int, id_b: int, weight: float) -> None:
        """Establishes a connection from neuron A to neuron B.

        Args:
            id_a (int): The ID of neuron A.
            id_b (int): The ID of neuron B.
            weight (float): The strength of the connection between the neurons.
        """
        self.neurons[id_a].connect(self.neurons[id_b], weight)

    def update(self) -> None:
        """Updates the states of the neurons."""
        for neuron in self.neurons:
            neuron.update()

    def update_display(self, screen, font) -> None:
        """Updates the states of the neurons and draw all of them to the screen.

        Args:
            screen (pygame.display): A pygame display.
            font (pygame.font): A pygame font.
        """
        for neuron in self.neurons:
            if len(self.neurons) < Brain.NEURON_LABEL_THRESHOLD:
                neuron.update_display(screen, font)
