class Genome:
    def __init__(self, array, fitness):
        self.array = array
        self.fitness = fitness

    def __eq__(self, other):
        return self.array == other.array and self.fitness == other.fitness
