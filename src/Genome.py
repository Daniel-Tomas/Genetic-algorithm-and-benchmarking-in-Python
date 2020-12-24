import numpy as np


class Genome:
    """Basic class

    Creates a pair, formed by a list and its fitness, in that order.

    Attributes:
        array (list): set of values of a function.
        fitness (int): solution´s quality.

    Args:
        bounds (list): Contains the minimum and maximum values that each variable can take from a candidate
            solution.
        minfun (function): Function used to calculate the fitness of a genome.
        array (list): List of values to be set.
        fitness (int): Int to be set.
    """

    def __init__(self, bounds=None, minfun=None, array=None, fitness=None):
        # if (bounds and not minfun) or (not bounds and minfun) or (array and (bounds or minfun)):
        #     if not minfun:
        #         raise BaseException("Parametros erroneos")

        if bounds and minfun:
            self.array = []
            for i in range(len(bounds)):
                self.array = np.append(self.array, np.random.uniform(bounds[i][0], bounds[i][1], 1))
            self.fitness = minfun(self.array)
        elif array is not None:
            self.array = np.copy(array)
            if fitness:
                self.fitness = fitness

    # def __eq__(self, other):
    #     """Compare if 'other' contains the same values as 'self'
    #
    #     Args:
    #         other (Genome): Object which the self object will be compared to.
    #
    #     Returns:
    #         bool: True if both objects contain the same elements in its lists and fitness.
    #         False otherwise.
    #     """
    #     return np.array_equal(self.array, other.array) and self.fitness == other.fitness
