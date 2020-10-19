import numpy as np


class Genome:
    """Basic class

    It creates a pair, formed by an array and its fitness, in that order.

    Atributes:
            array (list): set of values of a function
            fitness (int): solution´s quality
    """

    def __init__(self, bounds=None, minfun=None, array=None, fitness=None):
        # self.array = []
        # for i in range(len(bounds)):
        #     self.array.append( random.uniform(bounds[i][0], bounds[i][1], 1)[0] )

        # if (bounds and not minfun) or (not bounds and minfun) or (array and (bounds or minfun)):
        #     if not minfun:
        #         raise BaseException("Parametros erroneos")

        if bounds and minfun:
            self.array = np.random.uniform(bounds[0][0], bounds[0][1], len(bounds))
            self.fitness = minfun(self.array)
        elif array is not None:
            self.array = array
            if fitness:
                self.fitness = fitness
            else:
                self.fitness = 0

    def __eq__(self, other):
        """Compare if `other` contains the same values as `self`

        Args:
            other (Genome): Object which the self object will be compared to.

        Returns:
            boolean: True if both objects contain the same array and fitness.
            False otherwise.
        """
        return np.array_equal(self.array, other.array) and self.fitness == other.fitness
