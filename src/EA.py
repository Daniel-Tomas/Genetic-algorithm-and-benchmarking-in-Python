from src.ImplementedClasses import *
from src.Population import Population
from src.Data import *
import random
import numpy as np
import matplotlib.pyplot as plt


# todo imprimir dos decimales (Ejemplo en fitness resultante)
# todo hacer memoria
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

        mutator = Rand1MutationOperator(self.population, self.bounds, 0.2)
        mixer = ExponentialCrossoverOperator(self.minfun)
        replacer = ElitistReplacementOperator()

        for _ in range(iterations):
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
        # print(f'Best Genome after: {self.best_genome.array}, fitness={"{0:.2f}".format(self.best_genome.fitness)} ')

    def best(self):
        """Returns the best genome

        Returns:
            best_genome (Genome): Optimal solution calculated by the algorithm.
        """
        self.population.descendent_sort()
        self.best_genome = self.population.collection[0]
        return self.best_genome


if __name__ == '__main__':
    def f(array):
        return our_fitness(array)


    def our_fitness(array):
        res = 0;
        if (sum(array) > study_hours):
            return -np.inf;
        for i in range(len(array)):
            mark = (array[i] * point_per_hour[i])
            if (random.random() <= revision_probability[i]):
                mark += revision_mark[i];
            if (mark > 10):
                mark = 10
            res += mark * credits[i]
        return res / sum(credits);


    mybounds = [(minimum_marks[i] / point_per_hour[i], 10 / point_per_hour[i]) for i in range(len(credits))]

    best_fitness = []
    values_myEA = []
    for i in range(box_plots):
        values = []
        myEA = EA(f, mybounds, 30)
        myEA.run(500)
        best = myEA.best()
        best_fitness.append(best.fitness)
        for i in myEA.population.collection:
            values.append(i.fitness)
        values_myEA.append(values)
    # meanpointprops = dict(marker='x', markeredgecolor='blue',
    #                      markerfacecolor='blue')
    fig1, ax1 = plt.subplots()
    ax1.set_title("Best fitness of each repetition")
    ax1.boxplot(best_fitness, showmeans=True, meanline=True)
    plt.show()
    fig2, ax2 = plt.subplots()
    ax2.set_title("Fitness of each repetition")
    ax2.boxplot(values_myEA, showmeans=True, meanline=True)
    plt.show()
