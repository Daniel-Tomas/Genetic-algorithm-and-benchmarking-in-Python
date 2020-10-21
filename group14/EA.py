from group14.ImplementedClasses import *
from group14.Population import Population


class EA(object):
    """docstring for EA
    """

    def __init__(self, minfun, bounds, p_size):
        """It initialize the attributes.

        Args:
            minfun (function): Function used to calculate the fitness of a genome.
            bounds (list): It contains the minimum and maximum values that each variable can take from a candidate
                solution.
            p_size (int): Maximum size of our population.
        """
        self.minfun = minfun
        self.bounds = bounds
        self.population = Population(minfun, bounds, p_size)

    def run(self, iterations):
        """Runs the Differential Evolution algorithm.

        Args:
            iterations (int): Number of iterations to be made by the algorithm.
        """
        print(f'Antes:\n {self.population}\n')

        selector = UniformSelectionOperator()
        mutator = Rand1MutationOperator()
        mixer = ExponentialCrossoverOperator()
        replacer = ElitistReplacementOperator()

        for _ in range(iterations):
            for target in self.population.collection:
                # List with genomes who will be the donors
                donors = selector.apply(target, self.population)
                # Genome modified (mutant)
                mutant = mutator.apply(self.minfun, donors, self.bounds)
                # Genome modified by replacing a few random positions
                candidate = mixer.apply(self.minfun, target, mutant)
                # target is replaced by candidate from the population if candidate has less fitness than target
                replacer.apply(self.population, target, candidate)

        print(f'Despues:\n {self.population}\n')


if __name__ == '__main__':
    def f(array):
        return array[0] ** 2 + array[1] ** 2

    mybounds = [(0, 10), (0, 10)]

    myEA = EA(f, mybounds, 50)

    myEA.run(10000)
