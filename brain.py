class Brain:
    def __init__(self, neurons:list):
        self.neurons = neurons
    
    def addNeuron(self):
        self.neurons.append(Neuron(self, len(self.neurons)))
    
    def update(self):
        for n in self.neurons:
            n.update()
    
    def toString(self):
        out = ""
        for n in self.neurons:
            out += n.toString()
            out += '\n'
        
        return out

class Neuron:
    NEURON_THRESHOLD = 30

    def __init__(self, brain, id):
        self.brain = brain
        self.id = id

        self.state = 0
        self.links = {}
    
    def makeLink(self, other, weight:int):
        self.links[other.id] = weight
    
    def removeLink(self, other):
        del links[other.id]
    
    def fire(self):
        self.state = Neuron.NEURON_THRESHOLD
    
    def update(self):
        if self.state >= Neuron.NEURON_THRESHOLD:
            for id, weight in links:
                self.brain.get(id).state += weight

            self.state = 0
    
    def toString(self):
        out = ""
        out += str(self.id)
        out += " | "
        out += str(self.state)
        out += " | "
        out += str(self.links)

        return out

b = Brain([])
b.addNeuron()
print(b.toString())
# TODO: graphics