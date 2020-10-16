from numpy import random


class Genome:
    """Basic class

    It creates a pair, formed by an array and its fitness, in that order.

    Atributes:
            array (list): set of values of a function
            fitness (int): solution´s quality
    """

    def __init__(self, minfun, bounds):
        # self.array = []
        # for i in range(0, len(bounds)):
        #     self.array.append( random.uniform(bounds[i][0], bounds[i][1], 1)[0] )
        self.array = list(random.uniform(bounds[0][0], bounds[0][1], len(bounds)))
        self.fitness = minfun(self.array)

    def __eq__(self, other):
        """Compare if `other` contains the same values as `self`

        Args:
            other (Genome): Object which the self object will be compared to.

        Returns:
            boolean: True if both objects contain the same array and fitness.
            False otherwise.
        """
        return self.array == other.array and self.fitness == other.fitness
