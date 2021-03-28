import pygame
import random

class Brain:
    NEURON_LABEL_THRESHOLD = 25

    def __init__(self, neurons:list):
        self.neurons = neurons
    
    def addNeuron(self):
        self.neurons.append(Neuron(self, len(self.neurons)))
    
    def makeLink(self, idA, idB, weight):
        self.neurons[idA].makeLink(self.neurons[idB], weight)
    
    def update(self):
        for n in self.neurons:
            n.update()
    
    def updateDisplay(self, screen, font):
        for n in self.neurons:
            n.updateDisplay(screen, font if len(self.neurons) < Brain.NEURON_LABEL_THRESHOLD else None)
    
    def toString(self):
        out = ""
        for n in self.neurons:
            out += n.toString()
            out += '\n'
        
        return out
    
    @staticmethod
    def brainInit(neuronCount:int):
        b = Brain([])

        for i in range(neuronCount):
            b.addNeuron()
        
        return b

class Neuron:
    NEURON_THRESHOLD = 30

    def __init__(self, brain, id):
        self.brain = brain
        self.id = id

        self.state = 0
        self.links = {}
        self.pos = (random.random(), random.random())
    
    def makeLink(self, other, weight:int):
        self.links[other.id] = weight
    
    def removeLink(self, other):
        del links[other.id]
    
    def fire(self):
        self.state = Neuron.NEURON_THRESHOLD
    
    def update(self):
        # neuron is firing
        if self.state >= Neuron.NEURON_THRESHOLD:
            for id, weight in self.links.items():
                self.brain.neurons[id].state += weight

            self.state = 0
    
    def updateDisplay(self, screen, font):
        w, h = screen.get_size()
        pos = (self.pos[0]*w, self.pos[1]*h)
        
        # neuron circle
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), pos, 1)
        # label (if not None, meaning too many neurons)
        label = font.render(str(self.id), False, (255, 255, 255))
        screen.blit(label, pos)

        # neuron is firing
        if self.state >= Neuron.NEURON_THRESHOLD:
            pygame.draw.circle(screen, pygame.Color(255, 255, 255), pos, 3)

            for id, weight in self.links.items():
                other = self.brain.neurons[id]
                other.state += weight

                pygame.draw.line(screen, pygame.Color(255, 255, 255), pos, (other.pos[0]*w, other.pos[1]*h))

            self.state = 0

    def toString(self):
        return str(self.id) + " | " + str(self.state) + " | " + str(self.links)

def checkInput(brain):
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            # fire neuron number 0-9
            if event.key > 47 and event.key < 58:
                try:
                    brain.neurons[event.key-48].fire()
                except IndexError:
                    pass

def mainDisplay(brain):
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Cascadia Code', 12)

    size = (400, 400)
    screen = pygame.display.set_mode((size[0], size[1]))

    try:
        while True:
            checkInput(brain)
            brain.updateDisplay(screen, font)

            # add fade so you can actually see firing
            background = pygame.Surface(screen.get_size())
            background.set_alpha(1)
            background.fill('black')
            screen.blit(background, (0,0))
        
            pygame.display.update()
    except KeyboardInterrupt:
        pass

b = Brain.brainInit(10)
b.makeLink(0, 1, 30)
b.makeLink(1, 2, 30)
b.makeLink(1, 3, 30)
b.makeLink(1, 4, 30)

mainDisplay(b)