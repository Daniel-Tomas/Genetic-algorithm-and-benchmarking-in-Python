from group14.ImplementedClasses import *
from group14.Population import Population
from benchmarks import functions as fun


class EA(object):
    """This class is the entry point to the execution of the algorithm.

    Attributes:
            minfun (function): Function used to calculate the fitness of a genome.
            bounds (list): It contains the minimum and maximum values that each variable can take from a candidate
                solution.
            p_size (int): Maximum size of our population.
    """

    def __init__(self, minfun, bounds, p_size):
        self.minfun = minfun
        self.bounds = bounds
        self.population = Population(minfun, bounds, p_size)
        self.best_genome = None

    def run(self, iterations):
        """Runs the Differential Evolution algorithm.

        Args:
            iterations (int): Number of iterations to be made by the algorithm.

        Returns:
            best_genome (Genome): Optimal solution calculated by the algorithm
        """
        # print(f'Before:\n {self.population}\n')
        selector = UniformSelectionOperator()
        mutator = Rand1MutationOperator(0.2)
        mixer = ExponentialCrossoverOperator(self.minfun)
        replacer = ElitistReplacementOperator()

        for _ in range(iterations):
            for target in self.population.collection:
                # List with genomes who will be the donors
                donors = selector.apply(target, self.population)
                # Genome modified (mutant)
                mutant = mutator.apply(donors, self.bounds)
                # Genome modified by replacing a few random positions
                candidate = mixer.apply(target, mutant)
                # target is replaced by candidate from the population if candidate has less fitness than target
                replacer.apply(self.population, target, candidate)

        # print(f'After:\n {self.population}\n')

        self.population.descendent_sort()
        self.best_genome = self.population.collection[0]
        # print(f'Best Genome: {self.best_genome.array}, fitness={self.best_genome.fitness} ')

    def best(self):
        return self.best_genome


# if __name__ == '__main__':
#     def f(array):
#         return fun.ackley(array)
#
#
#     mybounds = [(0, 10), (10, 20), (20, 30), (30, 40)]
#
#     myEA = EA(f, mybounds, 4)
#
#     bestGenome = myEA.run(10000)
