"""Brain class file."""
from brain.neuron import Neuron, OutputNeuron

import math


class Brain:
    """Brain class file."""
    NEURON_LABEL_THRESHOLD = 25

    def __init__(self, random_pos: bool, neuron_count: int, output_count: int=0) -> None:
        """Initiates a Brain object.

        Args:
            neuron_count (int): The number of Neuron objects that are
            initialized with the Brain object.
            random_pos (bool): To randomize the positions of the neurons.
        """
        self.neurons = []

        # add all neurons
        DISPLAY_BUFFER = 0.1
        square_side = math.ceil(math.sqrt(neuron_count))
        divisor = square_side-1+DISPLAY_BUFFER*2
        for i in range(neuron_count):
            self.add_neuron(None if random_pos else (
                int(i/square_side)/divisor+DISPLAY_BUFFER/divisor,
                i%square_side/divisor+DISPLAY_BUFFER/divisor
            ))

        # add all output neurons
        for i in range(output_count):
            self.add_output_neuron(i)

    def add_neuron(self, pos: tuple) -> None:
        """Adds a Neuron object to the brain."""
        self.neurons.append(Neuron(self, len(self.neurons), pos))
    
    def add_output_neuron(self, id: int) -> None:
        """Adds an OutputNeuron object to the brain."""
        self.neurons.append(OutputNeuron(self, len(self.neurons), id))

    def connect(self, id_a: int, id_b: int, weight: float=1) -> None:
        """Establishes a connection from neuron A to neuron B.

        Args:
            id_a (int): The ID of neuron A.
            id_b (int): The ID of neuron B.
            weight (float): The strength of the connection between the neurons.
        """
        self.neurons[id_a].connect(self.neurons[id_b], weight)

    def update(self) -> None:
        """Updates the charge of the neurons."""
        for neuron in self.neurons:
            neuron.update()

    def update_display(self, screen, font) -> None:
        """Updates the charge of the neurons and draw all of them to the screen.

        Args:
            screen (pygame.display): A pygame display.
            font (pygame.font): A pygame font.
        """
        for neuron in self.neurons:
            neuron.update_display(screen, font if len(self.neurons) < Brain.NEURON_LABEL_THRESHOLD else None)
