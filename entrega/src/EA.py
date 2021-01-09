from ImplementedClasses import *
from Population import Population
from benchmarks import functions as fun


class EA(object):
    """This class is the entry point to the execution of the algorithm.

    Attributes:
        minfun (function): Function used to calculate the fitness of a genome.
        bounds (list): Contains the minimum and maximum values that each variable can take from a candidate
            solution.
        population (Population): Object which contains a list of genomes.
        best_genome (Genome): Optimal solution calculated by the algorithm.


    Args:
        minfun_ (function): The function to be set.
        bounds_ (list): List of values to be set.
        p_size (int): Maximum size of our population.
    """

    def __init__(self, minfun_, bounds_, p_size):
        self.minfun = minfun_
        self.bounds = bounds_
        self.population = Population(minfun_, bounds_, p_size)
        self.best_genome = None

    def run(self, iterations):
        """Runs the Differential Evolution algorithm.

        Args:
            iterations (int): Number of iterations to be made by the algorithm.
        """
        # print(f'Before:\n {self.population}\n')
        # self.best()
        # print(f'Best Genome before: {self.best_genome.array}, fitness={self.best_genome.fitness} ')

        mutator = Best1MutationOperator(self.population, self.bounds, 0.2)
        mixer = BinomialCrossoverOperator(self.minfun)
        replacer = ElitistReplacementOperator()

        for _ in range(iterations):
            self.population.ascendent_sort()
            candidate_population = Population(None, None, 0)
            for target in self.population.collection:
                # List with genomes who will be the donors
                mutant = mutator.apply(target)
                # Genome modified by replacing a few random positions
                candidate_genome = mixer.apply(target, mutant)

                candidate_population.add(candidate_genome)

            # Targets are replaced by candidates from the population if candidate has less fitness than target
            self.population = replacer.apply(self.population, candidate_population)

        # print(f'After:\n {self.population}\n')
        # self.best()
        # print(f'Best Genome after: {self.best_genome.array}, fitness={self.best_genome.fitness} ')

    def best(self):
        """Gets the best genome

        Returns:
            best_genome (Genome): Optimal solution calculated by the algorithm.
        """
        self.population.ascendent_sort()
        self.best_genome = self.population.collection[0]
        return self.best_genome


if __name__ == '__main__':
    def f(array):
        return fun.sphere(array)


    mybounds = [(-100, 100)] * 10

    myEA = EA(f, mybounds, 30)

    myEA.run(250)

    myEA.best()
